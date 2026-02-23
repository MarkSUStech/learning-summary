# 学期与寒假学习总结

这是一个展示我在学期和寒假期间学习成果的项目展示网站。

## 项目列表

### 1. MyAgent
智能代理系统，展示了AI代理的开发与应用。

### 2. AI SVG 自训练
基于机器学习的SVG图像生成与训练项目。

### 3. LaTeX Editor
功能完整的LaTeX编辑器，支持实时预览和文档编辑。

### 4. Chinese Xiangqi 2.00
完整的中国象棋游戏系统，包含客户端和服务器端，支持在线对战。

## 部署方式

### GitHub Pages 部署

1. 将项目推送到GitHub仓库
2. 在仓库设置中启用GitHub Pages
3. 选择main分支作为源
4. 访问 `https://yourusername.github.io/repository-name`

### Vercel 部署

1. 安装Vercel CLI: `npm i -g vercel`
2. 在项目目录运行: `vercel`
3. 按照提示完成部署

### Netlify 部署

1. 将项目文件夹拖拽到 [Netlify Drop](https://app.netlify.com/drop)
2. 或使用Netlify CLI: `netlify deploy --prod`

## 本地运行

直接在浏览器中打开 `index.html` 文件即可查看。

或使用本地服务器：

```bash
# Python 3
python -m http.server 8000

# Node.js (需要安装 http-server)
npx http-server -p 8000
```

然后访问 `http://localhost:8000`

## 文件结构

```
web/
├── index.html          # 主页面
├── styles.css          # 样式文件
├── script.js           # JavaScript文件
├── README.md           # 说明文档
└── *.mp4              # 演示视频文件
```

## 更新项目内容

如需更新项目信息，请编辑 `index.html` 文件中对应的项目部分。

## 许可证

本项目仅用于学习展示目的。

