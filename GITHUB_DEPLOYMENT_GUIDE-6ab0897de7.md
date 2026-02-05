# 🚀 GitHub部署快速操作指南

> **5分钟将高等数学教学系统部署到GitHub，零门槛，全免费！**

---

## ✨ 你将获得什么

部署完成后，你将拥有：
- 🎨 **在线课堂白板** - 12章完整教案，随时访问
- 🔬 **跨界探索系统** - AI驱动的科学探索之旅
- 📝 **考试与反馈系统** - 自动化教学工具
- 🤖 **AI内容生成** - 每周自动更新，无需人工

**所有功能完全免费，支持自定义修改！**

---

## 📋 部署前准备

### 需要的工具（全部免费）

| 工具 | 用途 | 获取方式 |
|------|------|---------|
| GitHub账号 | 托管代码和网页 | https://github.com/signup |
| OpenAI账号 | AI功能（可选） | https://platform.openai.com/ |
| 现代浏览器 | 访问系统 | Chrome/Firefox/Safari |

### 预计时间

- **首次部署**：5-10分钟
- **日常使用**：打开即用

---

## 🎯 一键部署方案（推荐）

### 方案1：使用GitHub Pages（最简单，5分钟）

#### 步骤1：创建仓库（2分钟）

1. 登录 GitHub
2. 点击右上角 **+** → **New repository**
3. 填写仓库信息：
   - **Repository name**: `math-teaching-system`（或自定义）
   - **Description**: AI驱动的高等数学教学系统
   - 选择 **Public**（公开）或 **Private**（私有）
   - **不要**勾选 "Add a README file"
4. 点击 **Create repository**

#### 步骤2：上传文件（3分钟）

**方式A：拖拽上传（推荐新手）**

1. 在新仓库页面，点击 **uploading an existing file**
2. 将本项目的所有文件拖拽到上传区域
3. 滚动到底部，在 **Commit changes** 框中输入：`初始部署`
4. 点击 **Commit changes**（绿色按钮）

**方式B：命令行上传（推荐熟练用户）**

```bash
# 初始化仓库
git init
git add .
git commit -m "初始部署"

# 关联GitHub仓库（替换你的用户名和仓库名）
git remote add origin https://github.com/你的用户名/math-teaching-system.git
git branch -M main
git push -u origin main
```

#### 步骤3：启用GitHub Pages（1分钟）

1. 进入仓库，点击 **Settings**（顶部导航栏）
2. 左侧菜单找到 **Pages**
3. 在 **Source** 下选择：
   - **Branch**: `main`
   - **Folder**: `/root`
4. 点击 **Save**
5. 等待1-2分钟，刷新页面，会看到：
   > 🎉 **Your site is live at https://你的用户名.github.io/math-teaching-system/**

#### 步骤4：访问系统

点击显示的链接，系统就部署完成了！

**主要页面地址**：
- 📊 课堂白板：`/dashboard.html`
- 🔬 探索系统：`/exploration.html`
- 📝 考试系统：`/exam.html`
- 💬 反馈系统：`/feedback.html`

---

## 🔧 配置AI功能（可选）

如果需要使用AI自动生成内容，需要配置OpenAI API密钥。

### 获取OpenAI API密钥

1. 访问 https://platform.openai.com/
2. 注册/登录账号
3. 点击右上角头像 → **API keys**
4. 点击 **Create new secret key**
5. 复制生成的密钥（格式：`sk-...`）
6. **保存密钥，只显示一次**

### 配置GitHub Secrets

1. 进入你的GitHub仓库
2. 点击 **Settings** → **Secrets and variables** → **Actions**
3. 点击 **New repository secret**
4. 填写：
   - **Name**: `OPENAI_API_KEY`
   - **Secret**: 粘贴你的OpenAI API密钥
5. 点击 **Add secret**

### 启用GitHub Actions

1. 进入 **Settings** → **Actions** → **General**
2. 找到 **Actions permissions**
3. 选择 **Allow all actions and reusable workflows**
4. 点击 **Save**

---

## 📦 方案2：使用Vercel（功能更强，可选）

### 优点

- 更快的访问速度
- 自动HTTPS
- 支持自定义域名
- 实时预览部署

### 部署步骤

1. **准备仓库**（同方案1步骤1-2）
2. **连接Vercel**：
   - 访问 https://vercel.com/
   - 点击 **Sign Up** → 使用GitHub登录
3. **导入项目**：
   - 点击 **Add New** → **Project**
   - 选择你的GitHub仓库
   - 点击 **Import**
4. **配置部署**：
   - **Framework Preset**: Other
   - **Root Directory**: `./`
   - 点击 **Deploy**
5. **访问系统**：
   - 等待1-2分钟，Vercel会提供访问链接
   - 格式：`https://你的项目名.vercel.app`

---

## 🎯 常用操作指南

### 如何修改内容

#### 方法1：直接在GitHub编辑

1. 进入仓库
2. 找到要修改的文件
3. 点击文件名进入详情
4. 点击右上角 **✏️** 图标
5. 在线编辑内容
6. 滚动到底部，填写：
   - **Commit message**: 描述修改内容
7. 点击 **Commit changes**

#### 方法2：本地编辑后推送

```bash
# 1. 拉取最新代码
git pull origin main

# 2. 编辑文件（用任意编辑器）

# 3. 提交修改
git add .
git commit -m "修改内容描述"

# 4. 推送到GitHub
git push origin main
```

### 如何更新系统内容

#### 更新教案或探索内容

直接编辑对应的文件：
- 课堂白板：`frontend/dashboard.html`
- 探索系统：`frontend/exploration.html`
- 考试系统：`frontend/exam.html`

修改后GitHub Pages会自动更新（1-2分钟）。

#### 使用AI自动生成内容

1. 确保已配置OpenAI API密钥
2. 进入仓库的 **Actions** 标签
3. 选择工作流：
   - **生成章节跨界探索内容（AI驱动）** - 生成跨界探索内容
   - **导出学生反馈数据到Excel（手动触发）** - 导出反馈数据
4. 点击 **Run workflow**
5. 配置参数后点击运行
6. 等待完成，查看生成的内容

### 如何查看GitHub Actions日志

1. 进入仓库的 **Actions** 标签
2. 点击左侧的某个工作流
3. 点击具体运行记录
4. 滚动到底部查看日志

---

## 📊 数据管理

### 反馈数据导出

**方法1：手动触发**

1. 进入 **Actions** → **导出学生反馈数据到Excel（手动触发）**
2. 点击 **Run workflow**
3. 等待完成后，查看 **Artifacts**（构件）
4. 下载生成的Excel文件

**方法2：自动导出（每周一0点）**

系统会自动运行 **自动导出学生反馈数据到Excel** 工作流，无需手动操作。

### 备份数据

**方法1：定期下载**

1. 进入仓库
2. 点击 **Code**（绿色按钮）
3. 选择 **Download ZIP**
4. 下载整个仓库的压缩包

**方法2：Git克隆备份**

```bash
git clone https://github.com/你的用户名/math-teaching-system.git
```

---

## 🌐 自定义域名（可选）

### 在GitHub Pages使用自定义域名

1. 购买域名（如阿里云、腾讯云）
2. 在DNS提供商添加CNAME记录：
   - 主机记录：`www`
   - 记录值：`你的用户名.github.io`
3. 在GitHub仓库的 **Settings** → **Pages**
4. 在 **Custom domain** 填入你的域名
5. 等待DNS生效（通常1-24小时）

---

## 📱 移动端访问

部署完成后，可以直接在手机浏览器访问：

1. 打开手机浏览器（Safari、Chrome等）
2. 输入你的GitHub Pages链接
3. 系统会自动适配移动端屏幕

**提示**：
- 建议将网址添加到手机主屏幕
- 体验和桌面端一致

---

## 🔐 隐私与安全

### 私有仓库

如果你希望只有自己可以访问：

1. 创建仓库时选择 **Private**
2. 或在现有仓库中：
   - **Settings** → 底部 **Danger Zone**
   - 点击 **Change repository visibility**
   - 选择 **Private**

### 保护API密钥

**重要**：API密钥已通过GitHub Secrets加密存储，安全可靠。

**不要**：
- ❌ 将API密钥写在代码文件中
- ❌ 将密钥提交到公开仓库
- ❌ 分享你的密钥给他人

---

## 💡 最佳实践

### 1. 版本管理

```bash
# 创建功能分支
git checkout -b feature/新功能

# 完成后合并到主分支
git checkout main
git merge feature/新功能
```

### 2. 定期备份

- 每周下载一次仓库备份
- 或使用GitHub的自动备份功能

### 3. 内容更新

- 建议：每周更新一次教案
- 探索内容：每月更新一次
- 考试题目：每学期更新一次

---

## ❓ 常见问题

### Q1: 部署后页面显示404错误

**原因**：文件路径不正确

**解决**：
- 确保文件在仓库根目录
- 访问路径应为：`仓库名/文件名.html`
- 例如：`math-teaching-system/dashboard.html`

### Q2: GitHub Pages更新后看不到新内容

**原因**：缓存问题

**解决**：
1. 清除浏览器缓存（Ctrl+Shift+R）
2. 或等待1-2分钟让GitHub缓存刷新

### Q3: AI功能不工作

**原因**：API密钥未配置或已过期

**解决**：
1. 检查GitHub Secrets中是否有`OPENAI_API_KEY`
2. 确认API密钥是否有效（OpenAI账号余额>0）
3. 查看GitHub Actions日志获取错误信息

### Q4: 如何限制访问权限

**方法1：私有仓库**
- 创建时选择Private
- 或将现有仓库改为Private

**方法2：访问控制**
- 需要额外的认证系统
- 可考虑使用Firebase Auth等服务

### Q5: 可以多人协作吗？

**可以！**

1. 进入 **Settings** → **Collaborators**
2. 点击 **Add people**
3. 输入协作者的GitHub用户名
4. 选择权限级别：Maintainer（管理员）/Writer（编辑）/Reader（只读）

---

## 📞 获取帮助

### 文档资源

- 📖 **快速开始**：`docs/QUICK_START.md`
- 📖 **完整指南**：`docs/COMPLETE_DELIVERY_GUIDE.md`
- 📖 **探索功能**：`docs/EXPLORATION_GUIDE.md`
- 📖 **教学手册**：`docs/EXPLORATION_TEACHING_MANUAL.md`

### 社区支持

- GitHub Issues：提交问题或建议
- GitHub Discussions：参与讨论

### 常用链接

- GitHub主页：https://github.com/
- GitHub Pages文档：https://docs.github.com/pages
- Vercel文档：https://vercel.com/docs
- OpenAI文档：https://platform.openai.com/docs

---

## 🎉 部署完成后

### 你可以做这些事

✅ **开始教学**
- 使用课堂白板进行教学
- 让学生访问探索系统自学
- 使用考试系统布置作业

✅ **收集反馈**
- 使用反馈系统收集学生意见
- 定期导出反馈数据分析

✅ **更新内容**
- 根据教学需要修改教案
- 使用AI生成新的探索内容
- 更新考试题目

✅ **分享成果**
- 分享GitHub链接给学生
- 分享优秀探索成果
- 推荐给同事使用

---

## 🚀 下一步建议

1. **测试系统**：先自己体验所有功能
2. **准备内容**：根据实际教学修改教案
3. **培训学生**：教学生如何使用系统
4. **收集反馈**：定期收集学生使用反馈
5. **持续优化**：根据反馈改进系统

---

## 💰 成本说明

### 完全免费方案

- GitHub托管：**免费**（公开仓库）
- GitHub Pages：**免费**
- GitHub Actions：**免费**（每月2000分钟）
- 访问流量：**免费**（100GB/月）

### AI功能成本

- OpenAI API：按使用量计费
- 教学使用：**$5-20/月**（足够使用）
- 可以设置每月预算上限

**总计**：最低成本为 **$0/月**（不使用AI功能）

---

## 📚 扩展资源

### 高级功能

- 自定义域名配置
- SSL证书设置
- CDN加速配置
- 数据库集成

### 集成方案

- 与学校管理系统对接
- 与LMS（学习管理系统）集成
- 开发移动端App
- 添加实时互动功能

---

**恭喜！你已掌握在GitHub上部署教学系统的全部技能！** 🎊

---

**文档版本**：v1.0  
**更新时间**：2026年2月5日  
**维护者**：AI助手

**现在就开始部署吧！5分钟后，你就能拥有属于自己的在线教学系统！** 🚀
