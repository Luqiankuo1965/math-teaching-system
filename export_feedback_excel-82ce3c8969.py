#!/usr/bin/env python3
"""
学生反馈数据Excel导出工具
功能：从GitHub Issues中提取反馈数据，生成Excel报表
"""

import json
import os
from datetime import datetime, timedelta
from github import Github

# 初始化GitHub客户端
token = os.environ.get('GITHUB_TOKEN')
if not token:
    print("❌ 错误：未找到GITHUB_TOKEN环境变量")
    exit(1)

repo_name = os.environ.get('GITHUB_REPOSITORY', os.environ.get('REPO_NAME', ''))
if not repo_name:
    print("❌ 错误：未找到GITHUB_REPOSITORY环境变量")
    exit(1)

g = Github(token)
repo = g.get_repo(repo_name)

print(f"📊 开始导出反馈数据到Excel...")
print(f"📂 仓库：{repo_name}")

# 获取所有反馈Issues
print("🔍 获取反馈Issues...")
issues = repo.get_issues(state='all', labels=['反馈'])

# 准备数据结构
feedback_data = []
course_stats = {}
student_stats = {}

# 遍历Issues
for issue in issues:
    # 跳过非反馈Issue
    if not any(label.name == '反馈' for label in issue.labels):
        continue
    
    # 解析Issue内容
    body = issue.body or ''
    created_at = issue.created_at
    updated_at = issue.updated_at
    
    # 提取信息
    course = '未知课程'
    chapter = '未知章节'
    student_name = '匿名学生'
    student_id = ''
    difficulty = 3
    feedback_type = '课程反馈'
    content = body
    
    # 解析字段
    for line in body.split('\n'):
        line = line.strip()
        if '课程名称' in line or '课程' in line:
            if '：' in line or ':' in line:
                parts = line.split('：') if '：' in line else line.split(':')
                if len(parts) > 1:
                    course = parts[-1].strip()
        elif '章节' in line or 'Chapter' in line.lower():
            if '：' in line or ':' in line:
                parts = line.split('：') if '：' in line else line.split(':')
                if len(parts) > 1:
                    chapter = parts[-1].strip()
        elif '姓名' in line or '学生' in line or 'Name' in line.lower():
            if '：' in line or ':' in line:
                parts = line.split('：') if '：' in line else line.split(':')
                if len(parts) > 1:
                    student_name = parts[-1].strip()
        elif '学号' in line or 'ID' in line:
            if '：' in line or ':' in line:
                parts = line.split('：') if '：' in line else line.split(':')
                if len(parts) > 1:
                    student_id = parts[-1].strip()
        elif '难度' in line or 'Difficulty' in line.lower():
            if '：' in line or ':' in line:
                parts = line.split('：') if '：' in line else line.split(':')
                if len(parts) > 1:
                    try:
                        difficulty = int(parts[-1].strip().replace('分', '').replace('分', ''))
                        difficulty = max(1, min(5, difficulty))
                    except:
                        difficulty = 3
        elif '反馈类型' in line or 'Type' in line.lower():
            if '：' in line or ':' in line:
                parts = line.split('：') if '：' in line else line.split(':')
                if len(parts) > 1:
                    feedback_type = parts[-1].strip()
    
    # 构建反馈记录
    record = {
        'Issue编号': issue.number,
        '标题': issue.title,
        '课程名称': course,
        '章节': chapter,
        '学生姓名': student_name,
        '学号': student_id,
        '反馈类型': feedback_type,
        '难度评分': difficulty,
        '难度等级': get_difficulty_label(difficulty),
        '反馈内容': clean_content(body),
        '状态': issue.state,
        '创建时间': created_at.strftime('%Y-%m-%d %H:%M:%S'),
        '最后更新': updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        'GitHub链接': issue.html_url
    }
    
    feedback_data.append(record)
    
    # 统计课程数据
    if course not in course_stats:
        course_stats[course] = {
            '反馈数': 0,
            '平均难度': 0,
            '学生数': set(),
            '难度分布': {'容易': 0, '一般': 0, '困难': 0, '非常困难': 0, '极难': 0}
        }
    
    course_stats[course]['反馈数'] += 1
    course_stats[course]['学生数'].add(student_name)
    course_stats[course]['难度分布'][get_difficulty_label(difficulty)] += 1
    
    # 统计学生数据
    student_key = f"{student_name}_{student_id}" if student_id else student_name
    if student_key not in student_stats:
        student_stats[student_key] = {
            '姓名': student_name,
            '学号': student_id,
            '反馈次数': 0,
            '平均难度': 0,
            '难度列表': []
        }
    
    student_stats[student_key]['反馈次数'] += 1
    student_stats[student_key]['难度列表'].append(difficulty)

# 计算平均难度
for course in course_stats:
    stats = course_stats[course]
    if stats['反馈数'] > 0:
        total_difficulty = sum([
            (1 * stats['难度分布']['容易']) +
            (2 * stats['难度分布']['一般']) +
            (3 * stats['难度分布']['困难']) +
            (4 * stats['难度分布']['非常困难']) +
            (5 * stats['难度分布']['极难'])
        ])
        stats['平均难度'] = round(total_difficulty / stats['反馈数'], 2)
    stats['学生数'] = len(stats['学生数'])

for student_key in student_stats:
    stats = student_stats[student_key]
    if stats['难度列表']:
        stats['平均难度'] = round(sum(stats['难度列表']) / len(stats['难度列表']), 2)
    del stats['难度列表']

# 生成Excel文件
export_to_excel(feedback_data, course_stats, student_stats)

print("✅ Excel导出完成！")

def get_difficulty_label(difficulty):
    """将数字难度转换为文字标签"""
    mapping = {
        1: '容易',
        2: '一般',
        3: '困难',
        4: '非常困难',
        5: '极难'
    }
    return mapping.get(difficulty, '困难')

def clean_content(content):
    """清理反馈内容，移除格式字段"""
    lines = []
    skip_fields = ['课程', '章节', '姓名', '学号', '难度', '反馈类型']
    
    for line in content.split('\n'):
        line = line.strip()
        if line and not any(field in line for field in skip_fields):
            lines.append(line)
    
    return '\n'.join(lines)

def export_to_excel(feedback_data, course_stats, student_stats):
    """导出数据到Excel文件"""
    try:
        import pandas as pd
        from datetime import datetime
    except ImportError:
        print("❌ 错误：未安装pandas和openpyxl库")
        print("请运行：pip install pandas openpyxl")
        exit(1)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = 'data/excel'
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. 创建反馈明细工作簿
    print("📝 生成反馈明细表...")
    df_feedback = pd.DataFrame(feedback_data)
    
    # 按创建时间排序
    df_feedback = df_feedback.sort_values(by='创建时间', ascending=False)
    
    # 调整列顺序
    column_order = [
        '创建时间', 'Issue编号', '课程名称', '章节', '学生姓名', '学号',
        '反馈类型', '难度评分', '难度等级', '标题', '反馈内容', '状态', 'GitHub链接'
    ]
    df_feedback = df_feedback[column_order]
    
    # 2. 创建课程统计表
    print("📚 生成课程统计表...")
    course_data = []
    for course, stats in course_stats.items():
        course_data.append({
            '课程名称': course,
            '反馈总数': stats['反馈数'],
            '参与学生数': stats['学生数'],
            '平均难度': stats['平均难度'],
            '容易（1分）': stats['难度分布']['容易'],
            '一般（2分）': stats['难度分布']['一般'],
            '困难（3分）': stats['难度分布']['困难'],
            '非常困难（4分）': stats['难度分布']['非常困难'],
            '极难（5分）': stats['难度分布']['极难']
        })
    
    df_course = pd.DataFrame(course_data)
    df_course = df_course.sort_values(by='反馈总数', ascending=False)
    
    # 3. 创建学生统计表
    print("👥 生成学生统计表...")
    student_data = []
    for student_key, stats in student_stats.items():
        student_data.append({
            '学生姓名': stats['姓名'],
            '学号': stats['学号'],
            '反馈次数': stats['反馈次数'],
            '平均难度': stats['平均难度']
        })
    
    df_student = pd.DataFrame(student_data)
    df_student = df_student.sort_values(by='反馈次数', ascending=False)
    
    # 4. 生成每日趋势数据
    print("📈 生成每日趋势表...")
    daily_trends = {}
    for record in feedback_data:
        date = record['创建时间'].split(' ')[0]
        if date not in daily_trends:
            daily_trends[date] = {'反馈数': 0, '总难度': 0, '计数': 0}
        
        daily_trends[date]['反馈数'] += 1
        daily_trends[date]['总难度'] += record['难度评分']
        daily_trends[date]['计数'] += 1
    
    trend_data = []
    for date in sorted(daily_trends.keys(), reverse=True):
        trends = daily_trends[date]
        avg_difficulty = round(trends['总难度'] / trends['计数'], 2) if trends['计数'] > 0 else 0
        trend_data.append({
            '日期': date,
            '反馈数量': trends['反馈数'],
            '平均难度': avg_difficulty
        })
    
    df_trend = pd.DataFrame(trend_data)
    
    # 5. 创建Excel文件
    print("📊 生成Excel文件...")
    excel_path = os.path.join(output_dir, f'反馈数据报表_{timestamp}.xlsx')
    
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        # 写入各个工作表
        df_feedback.to_excel(writer, sheet_name='反馈明细', index=False)
        df_course.to_excel(writer, sheet_name='课程统计', index=False)
        df_student.to_excel(writer, sheet_name='学生统计', index=False)
        df_trend.to_excel(writer, sheet_name='每日趋势', index=False)
        
        # 格式化各工作表
        format_sheet(writer, '反馈明细', feedback_data)
        format_sheet(writer, '课程统计', course_data)
        format_sheet(writer, '学生统计', student_data)
        format_sheet(writer, '每日趋势', trend_data)
    
    print(f"✅ Excel文件已生成：{excel_path}")
    print(f"📊 数据统计：")
    print(f"   - 反馈总数：{len(feedback_data)}")
    print(f"   - 课程数量：{len(course_stats)}")
    print(f"   - 学生数量：{len(student_stats)}")
    print(f"   - 时间跨度：{len(trend_data)}天")
    
    return excel_path

def format_sheet(writer, sheet_name, data):
    """格式化工作表样式"""
    worksheet = writer.sheets[sheet_name]
    
    # 设置列宽
    if sheet_name == '反馈明细':
        column_widths = {
            'A': 20,  # 创建时间
            'B': 12,  # Issue编号
            'C': 25,  # 课程名称
            'D': 15,  # 章节
            'E': 15,  # 学生姓名
            'F': 12,  # 学号
            'G': 12,  # 反馈类型
            'H': 10,  # 难度评分
            'I': 12,  # 难度等级
            'J': 30,  # 标题
            'K': 50,  # 反馈内容
            'L': 10,  # 状态
            'M': 40   # GitHub链接
        }
    elif sheet_name == '课程统计':
        column_widths = {
            'A': 25,  # 课程名称
            'B': 12,  # 反馈总数
            'C': 12,  # 参与学生数
            'D': 12,  # 平均难度
            'E': 15,  # 容易
            'F': 15,  # 一般
            'G': 15,  # 困难
            'H': 18,  # 非常困难
            'I': 12   # 极难
        }
    elif sheet_name == '学生统计':
        column_widths = {
            'A': 15,  # 学生姓名
            'B': 15,  # 学号
            'C': 12,  # 反馈次数
            'D': 12   # 平均难度
        }
    else:  # 每日趋势
        column_widths = {
            'A': 15,  # 日期
            'B': 12,  # 反馈数量
            'C': 12   # 平均难度
        }
    
    # 应用列宽
    for col, width in column_widths.items():
        worksheet.column_dimensions[col].width = width
    
    # 冻结首行
    worksheet.freeze_panes = 'A2'
    
    # 添加筛选
    worksheet.auto_filter.ref = worksheet.dimensions

if __name__ == '__main__':
    main()
