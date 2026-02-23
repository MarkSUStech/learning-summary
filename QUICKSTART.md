# 快速开始指南

## 📋 项目结构

```
web/
├── index.html              # 主页面
├── styles.css              # 样式文件
├── script.js               # JavaScript交互
├── README.md               # 项目说明
├── DEPLOY.md               # 部署指南
├── QUICKSTART.md           # 本文件
├── package.json            # Node.js配置
├── vercel.json             # Vercel部署配置
├── .gitignore              # Git忽略文件
├── .github/                # GitHub Actions配置
│   └── workflows/
│       └── deploy.yml
├── projects/               # 项目文件夹
│   ├── myagent/
│   ├── ai-svg/
│   ├── latex-editor/
│   └── chinese-xiangqi/
└── *.mp4                   # 演示视频文件
```

## 🚀 本地预览

### 方法 1: 直接打开（最简单）
双击 `index.html` 文件，在浏览器中打开。

### 方法 2: 使用本地服务器（推荐）

#### 使用 Python
```bash
# Python 3
python -m http.server 8000

# 然后访问 http://localhost:8000
```

#### 使用 Node.js
```bash
# 安装依赖（可选）
npm install

# 启动服务器
npm start

# 或直接使用
npx http-server -p 8000
```

#### 使用 VS Code Live Server
1. 安装 "Live Server" 扩展
2. 右键点击 `index.html`
3. 选择 "Open with Live Server"

## ✏️ 自定义内容

### 更新项目信息

编辑 `index.html` 文件，找到对应的项目部分（例如 `<!-- MyAgent 项目 -->`），修改：
- 项目描述
- 项目特点列表
- 添加项目截图或演示

### 添加项目截图

1. 将图片文件放在项目根目录或 `images/` 文件夹
2. 在 `index.html` 中找到对应的 `.placeholder-media` 部分
3. 替换为：
```html
<img src="images/myagent-screenshot.png" alt="MyAgent 截图">
```

### 添加更多视频

在 `index.html` 的 `video-container` 中添加新的视频项：
```html
<div class="video-item">
    <h4>视频标题</h4>
    <video controls>
        <source src="视频文件名.mp4" type="video/mp4">
        您的浏览器不支持视频播放。
    </video>
</div>
```

## 🎨 自定义样式

编辑 `styles.css` 文件，可以修改：
- 颜色主题（`:root` 变量）
- 字体大小和样式
- 布局和间距
- 动画效果

## 📦 部署到网上

详细部署步骤请查看 [DEPLOY.md](./DEPLOY.md)

### 快速部署（3种方式）

1. **GitHub Pages**（免费，适合代码托管）
   - 推送到 GitHub
   - 在仓库设置中启用 Pages

2. **Vercel**（免费，快速，推荐）
   ```bash
   npx vercel
   ```

3. **Netlify**（免费，简单）
   - 访问 [netlify.com/drop](https://app.netlify.com/drop)
   - 拖拽项目文件夹

## 📝 下一步

1. ✅ 预览网站，确认所有内容正确
2. ✅ 添加项目截图和详细描述
3. ✅ 根据实际情况更新项目信息
4. ✅ 选择部署方式并部署
5. ✅ 分享您的学习总结网站！

## ❓ 常见问题

### 视频无法播放？
- 检查视频文件路径是否正确
- 确认视频格式为 MP4
- 文件过大可能导致加载慢，建议压缩视频

### 样式不显示？
- 确认 `styles.css` 文件路径正确
- 清除浏览器缓存
- 检查浏览器控制台是否有错误

### 部署后页面空白？
- 检查文件路径（使用相对路径）
- 确认所有文件都已上传
- 检查 GitHub Pages 设置

## 💡 提示

- 视频文件较大，建议压缩后再上传
- 可以使用在线工具压缩视频：[CloudConvert](https://cloudconvert.com)
- 建议使用 GitHub Pages 或 Vercel，它们都支持自动部署
- 定期更新项目内容，保持网站活跃

祝您部署顺利！🎉

