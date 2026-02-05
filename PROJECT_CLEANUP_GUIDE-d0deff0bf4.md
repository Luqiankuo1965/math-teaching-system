# 🧹 项目目录重构与整理指南

**生成时间**：2026年2月5日  
**目标**：清理混乱目录，建立清晰的项目结构

---

## 📊 当前问题分析

### 问题1：技能目录误混入
```
❌ 当前状态
项目根目录/
├── drawio-generator/          ← 技能目录（不应该在这里）
│   ├── SKILL.md
│   ├── references/
│   └── script/
├── generate_kaoyan_review.yml  ← 正确
├── feedback.html               ← 正确
├── SYSTEM_OVERVIEW.md          ← 正确
└── ...其他文件
```

### 问题2：核心资产识别困难
- **核心文件**（应保留）：8个.yml、6个.html、7个.md、1个.drawio
- **误入文件**（应清理）：整个drawio-generator/目录

---

## ✅ 正确的项目结构

### 推荐目录结构
```
教学互动系统/
├── .github/
│   └── workflows/              ← GitHub Actions工作流
│       ├── analyze_feedback.yml
│       ├── analyze_feedback_enhanced.yml
│       ├── generate_math_exam.yml
│       ├── generate_math_exam_enhanced.yml
│       ├── generate_whiteboard.yml
│       ├── generate_whiteboard_enhanced.yml
│       ├── generate_whiteboard_complete.yml
│       └── generate_kaoyan_review.yml
│
├── frontend/                   ← 前端页面
│   ├── index.html
│   ├── feedback.html
│   ├── feedback_complete.html
│   ├── dashboard.html
│   ├── dashboard_complete.html
│   └── exam.html
│
├── docs/                       ← 文档
│   ├── SYSTEM_OVERVIEW.md
│   ├── QUICK_START.md
│   ├── COMPLETE_DELIVERY_GUIDE.md
│   ├── COMPLETE_VERSION_DEPLOYMENT_SUMMARY.md
│   ├── ADVANCED_MATH_CHAPTERS.md
│   ├── KAOYAN_MATH_AUTO_GENERATION.md
│   └── SESSION_DESIGN_ARCHIVE_20260205.md
│
├── assets/                     ← 资产文件
│   └── diagrams/
│       ├── 教学互动系统_架构图.drawio
│       └── 500学生免费方案_架构图.drawio
│
├── README.md                   ← 项目说明
└── .gitignore                  ← Git忽略配置
```

---

## 🔧 重构步骤

### 第一步：创建标准目录结构

```bash
# 创建标准目录
mkdir -p .github/workflows
mkdir -p frontend
mkdir -p docs
mkdir -p assets/diagrams
```

### 第二步：移动工作流文件

```bash
# 移动所有.yml文件到.github/workflows/
mv analyze_feedback.yml .github/workflows/
mv analyze_feedback_enhanced.yml .github/workflows/
mv generate_math_exam.yml .github/workflows/
mv generate_math_exam_enhanced.yml .github/workflows/
mv generate_whiteboard.yml .github/workflows/
mv generate_whiteboard_enhanced.yml .github/workflows/
mv generate_whiteboard_complete.yml .github/workflows/
mv generate_kaoyan_review.yml .github/workflows/
```

### 第三步：移动前端文件

```bash
# 移动所有.html文件到frontend/
mv index.html frontend/
mv feedback.html frontend/
mv feedback_complete.html frontend/
mv dashboard.html frontend/
mv dashboard_complete.html frontend/
mv exam.html frontend/
```

### 第四步：移动文档文件

```bash
# 移动所有.md文件到docs/
mv SYSTEM_OVERVIEW.md docs/
mv QUICK_START.md docs/
mv COMPLETE_DELIVERY_GUIDE.md docs/
mv COMPLETE_VERSION_DEPLOYMENT_SUMMARY.md docs/
mv ADVANCED_MATH_CHAPTERS.md docs/
mv KAOYAN_MATH_AUTO_GENERATION.md docs/
mv SESSION_DESIGN_ARCHIVE_20260205.md docs/

# README.md保留在根目录
```

### 第五步：移动资产文件

```bash
# 移动drawio文件到assets/diagrams/
mv 教学互动系统_架构图.drawio assets/diagrams/
mv 500学生免费方案_架构图.drawio assets/diagrams/
```

### 第六步：清理误入的技能目录

```bash
# 删除整个drawio-generator目录
rm -rf drawio-generator/
```

---

## 📝 批量执行脚本

### Windows PowerShell版本
```powershell
# 创建目录
New-Item -ItemType Directory -Force -Path ".github\workflows"
New-Item -ItemType Directory -Force -Path "frontend"
New-Item -ItemType Directory -Force -Path "docs"
New-Item -ItemType Directory -Force -Path "assets\diagrams"

# 移动工作流文件
Move-Item "analyze_feedback.yml" ".github\workflows\"
Move-Item "analyze_feedback_enhanced.yml" ".github\workflows\"
Move-Item "generate_math_exam.yml" ".github\workflows\"
Move-Item "generate_math_exam_enhanced.yml" ".github\workflows\"
Move-Item "generate_whiteboard.yml" ".github\workflows\"
Move-Item "generate_whiteboard_enhanced.yml" ".github\workflows\"
Move-Item "generate_whiteboard_complete.yml" ".github\workflows\"
Move-Item "generate_kaoyan_review.yml" ".github\workflows\"

# 移动前端文件
Move-Item "index.html" "frontend\"
Move-Item "feedback.html" "frontend\"
Move-Item "feedback_complete.html" "frontend\"
Move-Item "dashboard.html" "frontend\"
Move-Item "dashboard_complete.html" "frontend\"
Move-Item "exam.html" "frontend\"

# 移动文档文件
Move-Item "SYSTEM_OVERVIEW.md" "docs\"
Move-Item "QUICK_START.md" "docs\"
Move-Item "COMPLETE_DELIVERY_GUIDE.md" "docs\"
Move-Item "COMPLETE_VERSION_DEPLOYMENT_SUMMARY.md" "docs\"
Move-Item "ADVANCED_MATH_CHAPTERS.md" "docs\"
Move-Item "KAOYAN_MATH_AUTO_GENERATION.md" "docs\"
Move-Item "SESSION_DESIGN_ARCHIVE_20260205.md" "docs\"

# 移动资产文件
Move-Item "教学互动系统_架构图.drawio" "assets\diagrams\"
Move-Item "500学生免费方案_架构图.drawio" "assets\diagrams\"

# 清理误入的技能目录
Remove-Item -Recurse -Force "drawio-generator"
```

### Linux/Mac Bash版本
```bash
#!/bin/bash

# 创建目录
mkdir -p .github/workflows
mkdir -p frontend
mkdir -p docs
mkdir -p assets/diagrams

# 移动工作流文件
mv analyze_feedback.yml .github/workflows/
mv analyze_feedback_enhanced.yml .github/workflows/
mv generate_math_exam.yml .github/workflows/
mv generate_math_exam_enhanced.yml .github/workflows/
mv generate_whiteboard.yml .github/workflows/
mv generate_whiteboard_enhanced.yml .github/workflows/
mv generate_whiteboard_complete.yml .github/workflows/
mv generate_kaoyan_review.yml .github/workflows/

# 移动前端文件
mv index.html frontend/
mv feedback.html frontend/
mv feedback_complete.html frontend/
mv dashboard.html frontend/
mv dashboard_complete.html frontend/
mv exam.html/

# 移动文档文件
mv SYSTEM_OVERVIEW.md docs/
mv QUICK_START.md docs/
mv COMPLETE_DELIVERY_GUIDE.md docs/
mv COMPLETE_VERSION_DEPLOYMENT_SUMMARY.md docs/
mv ADVANCED_MATH_CHAPTERS.md docs/
mv KAOYAN_MATH_AUTO_GENERATION.md docs/
mv SESSION_DESIGN_ARCHIVE_20260205.md docs/

# 移动资产文件
mv 教学互动系统_架构图.drawio assets/diagrams/
mv 500学生免费方案_架构图.drawio assets/diagrams/

# 清理误入的技能目录
rm -rf drawio-generator/

echo "✅ 项目重构完成！"
```

---

## 📋 文件清单核对

### 重构后应包含的文件

#### .github/workflows/ (8个)
- ✅ analyze_feedback.yml
- ✅ analyze_feedback_enhanced.yml
- ✅ generate_math_exam.yml
- ✅ generate_math_exam_enhanced.yml
- ✅ generate_whiteboard.yml
- ✅ generate_whiteboard_enhanced.yml
- ✅ generate_whiteboard_complete.yml
- ✅ generate_kaoyan_review.yml

#### frontend/ (6个)
- ✅ index.html
- ✅ feedback.html
- ✅ feedback_complete.html
- ✅ dashboard.html
- ✅ dashboard_complete.html
- ✅ exam.html

#### docs/ (7个)
- ✅ SYSTEM_OVERVIEW.md
- ✅ QUICK_START.md
- ✅ COMPLETE_DELIVERY_GUIDE.md
- ✅ COMPLETE_VERSION_DEPLOYMENT_SUMMARY.md
- ✅ ADVANCED_MATH_CHAPTERS.md
- ✅ KAOYAN_MATH_AUTO_GENERATION.md
- ✅ SESSION_DESIGN_ARCHIVE_20260205.md

#### assets/diagrams/ (2个)
- ✅ 教学互动系统_架构图.drawio
- ✅ 500学生免费方案_架构图.drawio

#### 根目录 (1个)
- ✅ README.md

### 应该删除的文件/目录
- ❌ drawio-generator/ (整个目录)

---

## 🔄 更新README链接

重构目录后，需要更新README.md中的文档链接：

```markdown
# 更新前
[QUICK_START.md](QUICK_START.md)

# 更新后
[QUICK_START.md](docs/QUICK_START.md)
```

### 自动更新脚本（Python）
```python
import os
import re

# 读取README
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 更新文档链接
docs_to_update = [
    'QUICK_START.md',
    'SYSTEM_OVERVIEW.md',
    'COMPLETE_DELIVERY_GUIDE.md',
    'COMPLETE_VERSION_DEPLOYMENT_SUMMARY.md',
    'ADVANCED_MATH_CHAPTERS.md',
    'KAOYAN_MATH_AUTO_GENERATION.md',
    'SESSION_DESIGN_ARCHIVE_20260205.md'
]

for doc in docs_to_update:
    content = content.replace(f']({doc})', f'](docs/{doc})')

# 保存更新后的README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ README.md链接已更新")
```

---

## ⚠️ 注意事项

### 1. Git版本控制
```bash
# 执行重构前先提交当前状态
git add .
git commit -m "保存重构前的状态"

# 执行重构

# 提交重构后的状态
git add .
git commit -m "重构项目目录结构"
```

### 2. 工作流路径更新
重构后，GitHub会自动识别`.github/workflows/`目录下的工作流文件，无需额外配置。

### 3. 前端路径更新
如果前端文件之间有相互引用，需要更新相对路径。

---

## ✅ 验证清单

重构完成后，请核对：

- [ ] 所有.yml文件已移动到`.github/workflows/`
- [ ] 所有.html文件已移动到`frontend/`
- [ ] 所有.md文档已移动到`docs/`
- [ ] 所有.drawio文件已移动到`assets/diagrams/`
- [ ] `drawio-generator/`目录已删除
- [ ] README.md中的文档链接已更新
- [ ] 前端页面之间的相互引用路径已更新
- [ ] GitHub Actions工作流可以正常触发
- [ ] 前端页面可以正常访问

---

## 🎯 重构后的优势

### 1. 清晰的项目结构
- 每个目录职责明确
- 文件分类有序

### 2. 便于团队协作
- 新成员快速上手
- 减少文件冲突

### 3. 易于维护扩展
- 新增功能有明确位置
- 遵循标准目录规范

### 4. 符合行业标准
- GitHub Actions标准路径
- 前后端分离架构

---

**执行建议**：先备份当前项目，然后按照步骤执行重构。
