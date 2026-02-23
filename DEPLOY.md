# 部署指南

本指南将帮助您将学习总结网站部署到互联网上。

## 方式一：GitHub Pages（推荐，免费）

### 步骤 1: 创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角的 "+" 按钮，选择 "New repository"
3. 输入仓库名称（例如：`learning-summary`）
4. 选择 Public（公开）或 Private（私有）
5. 不要勾选 "Initialize this repository with a README"
6. 点击 "Create repository"

### 步骤 2: 上传代码到 GitHub

在项目目录下打开终端，执行以下命令：

```bash
# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 提交更改
git commit -m "Initial commit: 学习总结网站"

# 添加远程仓库（将 YOUR_USERNAME 和 REPO_NAME 替换为实际值）
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 步骤 3: 启用 GitHub Pages

1. 在 GitHub 仓库页面，点击 "Settings"（设置）
2. 在左侧菜单中找到 "Pages"
3. 在 "Source" 部分，选择 "Deploy from a branch"
4. 选择分支为 "main"，文件夹为 "/ (root)"
5. 点击 "Save"
6. 等待几分钟，GitHub 会生成您的网站地址：`https://YOUR_USERNAME.github.io/REPO_NAME`

## 方式二：Vercel（推荐，免费且快速）

### 步骤 1: 安装 Vercel CLI

```bash
npm install -g vercel
```

### 步骤 2: 登录 Vercel

```bash
vercel login
```

### 步骤 3: 部署项目

在项目目录下执行：

```bash
vercel
```

按照提示完成部署。首次部署会询问一些问题：
- Set up and deploy? **Yes**
- Which scope? 选择您的账户
- Link to existing project? **No**
- What's your project's name? 输入项目名称
- In which directory is your code located? **./**

部署完成后，Vercel 会提供一个 URL，例如：`https://your-project.vercel.app`

### 步骤 4: 自动部署（可选）

如果您已经将代码推送到 GitHub，Vercel 会自动检测并部署。您也可以：
1. 访问 [vercel.com](https://vercel.com)
2. 点击 "Add New Project"
3. 导入您的 GitHub 仓库
4. 点击 "Deploy"

## 方式三：Netlify（免费且简单）

### 方法 A: 拖拽部署

1. 访问 [Netlify Drop](https://app.netlify.com/drop)
2. 将整个项目文件夹拖拽到页面中
3. 等待部署完成
4. 获得一个随机 URL，例如：`https://random-name-123.netlify.app`

### 方法 B: Git 集成

1. 访问 [Netlify](https://www.netlify.com)
2. 注册/登录账户
3. 点击 "Add new site" -> "Import an existing project"
4. 选择 GitHub，授权并选择仓库
5. 点击 "Deploy site"

## 方式四：本地预览

在部署之前，您可以在本地预览网站：

### 使用 Python

```bash
# Python 3
python -m http.server 8000

# 然后访问 http://localhost:8000
```

### 使用 Node.js

```bash
# 安装 http-server（如果还没有）
npm install -g http-server

# 启动服务器
http-server -p 8000

# 然后访问 http://localhost:8000
```

### 使用 VS Code

1. 安装 "Live Server" 扩展
2. 右键点击 `index.html`
3. 选择 "Open with Live Server"

## 注意事项

1. **视频文件大小**：如果视频文件很大，可能会影响加载速度。建议：
   - 压缩视频文件
   - 使用视频托管服务（如 YouTube、Bilibili）然后嵌入
   - 使用 CDN 加速

2. **自定义域名**（可选）：
   - GitHub Pages: 在仓库设置中添加自定义域名
   - Vercel/Netlify: 在项目设置中添加自定义域名

3. **更新网站**：
   - 修改代码后，提交并推送到 GitHub
   - GitHub Pages 会自动更新（可能需要几分钟）
   - Vercel/Netlify 会自动检测并重新部署

## 故障排除

### GitHub Pages 不显示
- 检查仓库是否为 Public（免费账户只能部署 Public 仓库）
- 确认已启用 Pages 功能
- 检查文件路径是否正确

### 视频无法播放
- 检查视频文件路径是否正确
- 确认视频格式为浏览器支持的格式（MP4 推荐）
- 检查文件大小，过大可能导致加载缓慢

### 样式不显示
- 检查 CSS 文件路径
- 确认浏览器控制台是否有错误
- 清除浏览器缓存

## 需要帮助？

如果遇到问题，可以：
1. 查看各平台的官方文档
2. 检查浏览器控制台的错误信息
3. 确认所有文件都已正确上传


