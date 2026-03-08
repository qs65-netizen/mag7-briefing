# MAG7 Daily Briefing

自动每日简报：MAG7 + ACN 股票行情与财经新闻

## 功能

- 📈 每日自动获取 MAG7 + ACN 股票价格
- 📰 自动获取相关财经新闻（带翻译）
- 🌍 中英文双语支持
- ☁️ 自动部署到 GitHub Pages

## 部署

### 1. 创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)
2. 创建新仓库，命名为 `mag7-briefing`
3. 设置为 **Public** 仓库

### 2. 推送代码

```bash
cd mag7_briefing
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/mag7-briefing.git
git push -u origin main
```

### 3. 启用 GitHub Pages

1. 进入仓库 → Settings → Pages
2. Source 选择 **Deploy from a branch**
3. Branch 选择 **gh-pages**，文件夹选择 **/(root)**
4. 点击 Save

### 4. 启用 GitHub Actions

1. 进入仓库 → Actions
2. 看到 "Daily MAG7 Briefing" 工作流
3. 点击 **Enable workflow**

### 5. 手动触发一次

1. 进入 Actions → Daily MAG7 Briefing
2. 点击 **Run workflow** → **Run workflow**

## 访问

部署完成后，访问: `https://YOUR_USERNAME.github.io/mag7-briefing/`

## 自动运行

每天 **7:00 AM UTC** (3:00 PM 北京时间) 自动运行

## 自定义

- 修改 `stocks_data.py` 添加更多股票
- 修改 `main.py` 自定义页面样式
