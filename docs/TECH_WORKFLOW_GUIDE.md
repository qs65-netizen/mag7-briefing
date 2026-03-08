# Tech Development Workflow Guide
## From Concept to Production - A Manager's Handbook

---

# 技术开发工作流程指南
## 从概念到生产 - 管理者手册

---

## Table of Contents / 目录

1. [Overview / 概述](#1-overview--概述)
2. [Project Planning / 项目规划](#2-project-planning--项目规划)
3. [Technical Architecture / 技术架构](#3-technical-architecture--技术架构)
4. [Development Environment / 开发环境](#4-development-environment--开发环境)
5. [Code Development / 代码开发](#5-code-development--代码开发)
6. [Version Control with Git / Git版本控制](#6-version-control-with-git--git版本控制)
7. [Code Review / 代码审查](#7-code-review--代码审查)
8. [CI/CD Pipeline / 持续集成/持续部署](#8-cicd-pipeline--持续集成持续部署)
9. [Deployment / 部署上线](#9-deployment--部署上线)
10. [Monitoring & Maintenance / 监控与维护](#10-monitoring--maintenance--监控与维护)
11. [Common Terminology / 常用术语](#11-common-terminology--常用术语)
12. [Quick Reference / 快速参考](#12-quick-reference--快速参考)

---

## 1. Overview / 概述

### What is a Development Workflow? / 什么是开发工作流程？

A development workflow is the end-to-end process of building and delivering software. It typically includes: / 开发工作流程是构建和交付软件的端到端流程，通常包括：

- **Planning** - Defining what to build / 规划 - 确定要构建什么
- **Development** - Writing the code / 开发 - 编写代码
- **Testing** - Verifying the code works / 测试 - 验证代码是否正常工作
- **Review** - Getting feedback from peers / 审查 - 获得同行的反馈
- **Integration** - Combining changes / 集成 - 合并更改
- **Deployment** - Releasing to production / 部署 - 发布到生产环境
- **Monitoring** - Tracking performance / 监控 - 跟踪性能

### The Players / 角色

| Role | Responsibility | 角色 | 职责 |
|------|---------------|------|------|
| **Product Manager** | Defines what to build | 产品经理 | 定义要构建什么 |
| **Engineering Manager** | Leads the team, manages timeline | 工程经理 | 领导团队，管理时间表 |
| **Software Engineer** | Writes code | 软件工程师 | 编写代码 |
| **DevOps Engineer** | Manages infrastructure & deployment | 运维工程师 | 管理基础设施和部署 |
| **QA Engineer** | Tests the software | QA工程师 | 测试软件 |
| **Designer** | Creates the visual design | 设计师 | 创建视觉设计 |

---

## 2. Project Planning / 项目规划

### 2.1 Requirements Gathering / 需求收集

**What happens:** / 发生了什么：
The team meets with stakeholders (you!) to understand what they need. / 团队与利益相关者（也就是您！）会面，了解他们的需求。

**Manager's role:** / 管理者角色：
- Ask clear questions / 提出明确的问题
- Prioritize features (MoSCoW method: Must have, Should have, Could have, Won't have) / 优先排序功能（MoSCoW方法：必须有、应该有、可以有、不会有）
- Define success metrics / 定义成功指标
- Set realistic timelines / 设定现实的时间表

**Key questions to ask:** / 需要问的关键问题：
1. What problem are we solving? / 我们要解决什么问题？
2. Who are the users? / 用户是谁？
3. What is the timeline? / 时间表是什么？
4. What is the budget? / 预算是多少？
5. What are the technical constraints? / 有什么技术限制？

### 2.2 Technical Specification / 技术规格

**What happens:** / 发生了什么：
Engineers create a technical design document (TDD - Technical Design Document) that outlines: / 工程师创建技术设计文档，详细说明：

- **Architecture** - How the system is structured / 架构 - 系统如何构建
- **Data models** - How data is stored / 数据模型 - 如何存储数据
- **APIs** - How different parts communicate / API - 不同部分如何通信
- **Security** - How to protect the system / 安全 - 如何保护系统
- **Scalability** - How to handle growth / 可扩展性 - 如何处理增长

**Manager's role:** / 管理者角色：
- Review the design for feasibility / 审查设计的可行性
- Identify risks / 识别风险
- Allocate resources / 分配资源
- Set milestones / 设定里程碑

---

## 3. Technical Architecture / 技术架构

### 3.1 Frontend vs Backend / 前端 vs 后端

```
┌─────────────────────────────────────────────────────────────┐
│                        USER'S BROWSER                        │
│                    (User Interface / UI)                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                         FRONTEND                             │
│  • HTML/CSS/JavaScript                                    │
│  • React, Vue, Angular                                    │
│  • Handles user interaction                               │
└─────────────────────────────────────────────────────────────┘
                              │
                    (API Calls / REST)
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                          BACKEND                            │
│  • Python, Node.js, Java, Go                             │
│  • Business logic                                         │
│  • Database operations                                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                         DATABASE                            │
│  • MySQL, PostgreSQL, MongoDB                            │
│  • Stores data                                            │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Cloud Services / 云服务

| Service Type | Examples | 服务类型 | 示例 |
|-------------|----------|----------|------|
| **Compute** | AWS EC2, Google Cloud VM | 计算 | AWS EC2, Google Cloud VM |
| **Storage** | AWS S3, Google Cloud Storage | 存储 | AWS S3, Google Cloud Storage |
| **Database** | AWS RDS, Google Cloud SQL | 数据库 | AWS RDS, Google Cloud SQL |
| **CDN** | Cloudflare, AWS CloudFront | CDN | Cloudflare, AWS CloudFront |
| **Hosting** | Vercel, Netlify, GitHub Pages | 托管 | Vercel, Netlify, GitHub Pages |

---

## 4. Development Environment / 开发环境

### 4.1 Local Setup / 本地环境设置

**What happens:** / 发生了什么：
Each developer sets up their local machine with the necessary tools. / 每个开发者在他们的本地机器上设置必要的工具。

**Common tools:** / 常用工具：

| Tool | Purpose | 工具 | 用途 |
|------|---------|------|------|
| **VS Code** | Code editor | 代码编辑器 |
| **Git** | Version control | 版本控制 |
| **Docker** | Containerization | 容器化 |
| **Node.js** | JavaScript runtime | JavaScript运行时 |
| **Python** | Python runtime | Python运行时 |
| **Homebrew** | Package manager (Mac) | 包管理器(Mac) |

### 4.2 Terminal Commands Basics / 终端命令基础

```bash
# Navigation / 导航
ls                          # List files / 列出文件
cd folder_name              # Change directory / 切换目录
pwd                         # Print working directory / 打印当前目录
mkdir folder_name           # Create directory / 创建目录

# File operations / 文件操作
cp source dest              # Copy / 复制
mv source dest              # Move / 移动
rm file_name                # Delete / 删除
cat file_name               # View file content / 查看文件内容

# Git commands / Git命令
git status                  # Check status / 检查状态
git add .                   # Stage all changes / 暂存所有更改
git commit -m "message"     # Commit with message / 提交并添加消息
git push                    # Push to remote / 推送到远程
git pull                    # Pull from remote / 从远程拉取
git branch                  # List branches / 列出分支
```

---

## 5. Code Development / 代码开发

### 5.1 Coding Standards / 编码规范

**Best practices:** / 最佳实践：

1. **Write clean, readable code** - Code is read more often than it's written / 编写清晰、可读的代码 - 代码被阅读的次数比编写多
2. **Use meaningful names** - Variable names should describe what they contain / 使用有意义的名称 - 变量名应描述其内容
3. **Comment complex logic** - Explain why, not what / 注释复杂的逻辑 - 解释为什么，而不是做什么
4. **Follow style guides** - Consistent formatting across the team / 遵循风格指南 - 全队一致的格式

### 5.2 Project Structure / 项目结构

```
my-project/
├── .github/
│   └── workflows/          # CI/CD configurations / CI/CD配置
├── src/                     # Source code / 源代码
│   ├── components/         # UI components / UI组件
│   ├──pages/              # Page components / 页面组件
│   ├── styles/             # CSS/Styles / 样式
│   └── utils/              # Utility functions / 工具函数
├── tests/                   # Test files / 测试文件
├── docs/                    # Documentation / 文档
├── .gitignore              # Git ignore rules / Git忽略规则
├── README.md                # Project readme / 项目说明
├── package.json             # Dependencies (Node.js) / 依赖
└── requirements.txt        # Dependencies (Python) / 依赖
```

### 5.3 Dependencies / 依赖管理

**What are dependencies?** / 什么是依赖？
Libraries or packages that your code needs to function. / 代码运行所需的库或包。

**How to manage:** / 如何管理：
- **Python:** `requirements.txt` lists all Python packages / 列出所有Python包
- **Node.js:** `package.json` lists all JavaScript packages / 列出所有JavaScript包

**Installation:** / 安装：
```bash
# Python
pip install -r requirements.txt

# Node.js
npm install
```

---

## 6. Version Control with Git / Git版本控制

### 6.1 What is Git? / 什么是Git？

Git is a **version control system** that tracks changes to your code. It allows multiple people to work on the same project simultaneously. / Git是一个跟踪代码更改的版本控制系统。它允许多人同时处理同一个项目。

### 6.2 Key Concepts / 关键概念

| Concept | Explanation | 概念 | 解释 |
|---------|-------------|------|------|
| **Repository (Repo)** | The project folder | 仓库 | 项目文件夹 |
| **Branch** | A separate line of development | 分支 | 独立的开发线 |
| **Commit** | A saved snapshot of changes | 提交 | 更改的已保存快照 |
| **Merge** | Combining branches | 合并 | 组合分支 |
| **Pull Request (PR)** | Request to merge changes | 拉取请求 | 请求合并更改 |
| **Remote** | The cloud version of the repo | 远程 | 仓库的云版本 |

### 6.3 Git Workflow / Git工作流程

```
┌─────────────────────────────────────────────────────────────┐
│                    TYPICAL GIT WORKFLOW                     │
└─────────────────────────────────────────────────────────────┘

1. Create a branch / 创建分支
   git checkout -b feature/new-feature

2. Make changes / 更改代码
   (edit files in your code editor)

3. Stage changes / 暂存更改
   git add .
   or
   git add specific-file.py

4. Commit changes / 提交更改
   git commit -m "Add new feature"

5. Push to remote / 推送到远程
   git push origin feature/new-feature

6. Create Pull Request / 创建拉取请求
   (via GitHub website)

7. Code Review / 代码审查
   (team members review and comment)

8. Merge / 合并
   (after approval, merge to main branch)
```

### 6.4 GitHub / GitHub

**What is GitHub?** / 什么是GitHub？
A cloud platform for hosting Git repositories and collaborating on code. / 用于托管Git仓库和协作开发代码的云平台。

**Key features:** / 关键功能：
- **Repositories** - Host your code / 托管代码
- **Pull Requests** - Code review process / 代码审查流程
- **Issues** - Track bugs and tasks / 跟踪bug和任务
- **Actions** - CI/CD automation / CI/CD自动化
- **Pages** - Free website hosting / 免费网站托管

---

## 7. Code Review / 代码审查

### 7.1 Why Review Code? / 为什么要审查代码？

- **Catch bugs early** - Find errors before they reach production / 及早发现错误 - 在生产前发现错误
- **Share knowledge** - Team members learn from each other / 分享知识 - 团队成员相互学习
- **Maintain quality** - Ensure consistent standards / 保持质量 - 确保一致的标准
- **Mentorship** - Senior engineers guide juniors / 指导 - 高级工程师指导初级工程师

### 7.2 Code Review Checklist / 代码审查清单

**Reviewers should check:** / 审查者应该检查：

- [ ] Does the code work as intended? / 代码是否按预期工作？
- [ ] Is the code readable and maintainable? / 代码是否可读和可维护？
- [ ] Are there any security vulnerabilities? / 是否有安全漏洞？
- [ ] Are there adequate tests? / 是否有足够的测试？
- [ ] Does it follow coding standards? / 是否遵循编码标准？
- [ ] Is the documentation updated? / 文档是否已更新？

### 7.3 Giving Good Feedback / 提供良好的反馈

**Good feedback:** / 良好的反馈：
- "Consider using a hash map here for O(1) lookup instead of O(n) linear search." / "考虑在这里使用哈希表实现O(1)查找，而不是O(n)线性搜索。"

**Avoid:** / 避免：
- "This is wrong." / "这是错的。" (Too vague / 太模糊)
- "You should have done it my way." / "你应该用我的方法做。" (Not constructive / 没有建设性)

---

## 8. CI/CD Pipeline / 持续集成/持续部署

### 8.1 What is CI/CD? / 什么是CI/CD？

| Term | Full Name | Meaning | 含义 |
|------|-----------|---------|------|
| **CI** | Continuous Integration | Automatically test code when pushed | 推送时自动测试代码 |
| **CD** | Continuous Deployment | Automatically deploy code after tests pass | 测试通过后自动部署代码 |

### 8.2 GitHub Actions / GitHub Actions

**What is GitHub Actions?** / 什么是GitHub Actions？
A CI/CD platform built into GitHub that automates your workflow. / 内置在GitHub中的CI/CD平台，可自动化您的工作流程。

**Key components:** / 关键组件：

```
┌─────────────────────────────────────────────────────────────┐
│                    GITHUB ACTIONS                           │
└─────────────────────────────────────────────────────────────┘

Workflow (工作流)
    │
    ├── Trigger (触发器)
    │   ├── on: push          # When code is pushed / 推送代码时
    │   ├── on: pull_request  # When PR is created / 创建PR时
    │   ├── on: schedule      # On a schedule / 按计划
    │   └── workflow_dispatch # Manual trigger / 手动触发
    │
    ├── Jobs (作业)
    │   └── build-and-deploy
    │       │
    │       └── Steps (步骤)
    │           ├── Checkout code
    │           ├── Setup environment
    │           ├── Install dependencies
    │           ├── Run tests
    │           └── Deploy
```

### 8.3 Example: Our MAG7 Briefing Workflow / 示例：我们的简报工作流

```yaml
name: Daily MAG7 Briefing

on:
  schedule:
    - cron: '0 7 * * *'      # Run daily at 7 AM UTC
  workflow_dispatch:          # Allow manual run
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Generate briefing
        run: python main.py

      - name: Deploy to GitHub Pages
        uses: actions/deploy-pages@v4
```

---

## 9. Deployment / 部署上线

### 9.1 What is Deployment? / 什么是部署？

Deployment is the process of making your application available to users. / 部署是让您的应用程序对用户可用的过程。

### 9.2 Deployment Methods / 部署方式

| Method | Description | 描述 |
|--------|-------------|------|
| **Manual** | Developer uploads files via FTP/SFTP | 开发者通过FTP/SFTP上传文件 |
| **Automated** | CI/CD pipeline deploys automatically | CI/CD流水线自动部署 |
| **Blue-Green** | Two identical environments, switch between them | 两个相同环境，切换 |
| **Canary** | Deploy to small % first, then expand | 先部署到小部分，然后扩展 |

### 9.3 GitHub Pages / GitHub Pages

**What is GitHub Pages?** / 什么是GitHub Pages？
A free static website hosting service from GitHub. / GitHub提供的免费静态网站托管服务。

**How it works:** / 工作原理：
1. Push code to GitHub repository / 将代码推送到GitHub仓库
2. GitHub Actions builds the site / GitHub Actions构建网站
3. Site is published at `username.github.io/repo-name` / 网站发布在 `username.github.io/repo-name`

**For our project:** / 对于我们的项目：
- URL: `https://qs65-netizen.github.io/mag7-briefing/`
- Auto-deploys on every push to main branch / 每次推送到main分支时自动部署

---

## 10. Monitoring & Maintenance / 监控与维护

### 10.1 Why Monitor? / 为什么要监控？

- **Detect issues early** - Before users notice / 及早发现问题 - 在用户注意到之前
- **Understand usage** - Know how people use your product / 了解使用情况 - 知道人们如何使用您的产品
- **Plan capacity** - Know when to scale / 规划容量 - 知道何时扩展
- **Improve performance** - Identify bottlenecks / 改进性能 - 识别瓶颈

### 10.2 Key Metrics / 关键指标

| Metric | Description | 描述 |
|--------|-------------|------|
| **Uptime** | % of time the service is available | 服务可用的时间百分比 |
| **Response Time** | How fast the page loads | 页面加载速度 |
| **Error Rate** | % of requests that fail | 失败的请求百分比 |
| **Traffic** | Number of visitors | 访问者数量 |

### 10.3 Types of Testing / 测试类型

| Test Type | Purpose | 目的 |
|-----------|---------|------|
| **Unit Tests** | Test individual functions | 测试单个函数 |
| **Integration Tests** | Test how parts work together | 测试各部分如何协同工作 |
| **End-to-End Tests** | Test complete user flows | 测试完整的用户流程 |
| **Performance Tests** | Test under load | 在负载下测试 |
| **Security Tests** | Find vulnerabilities | 查找漏洞 |

---

## 11. Common Terminology / 常用术语

### A-E

| Term | Definition | 定义 |
|------|------------|------|
| **API** | Application Programming Interface - How software talks to each other | 软件相互通信的方式 |
| **Bug** | An error in code that causes unexpected behavior | 导致意外行为的代码错误 |
| **CI/CD** | Continuous Integration/Continuous Deployment | 持续集成/持续部署 |
| **Cloud** | Remote servers accessed via internet | 通过互联网访问的远程服务器 |
| **Container** | Lightweight virtual environment | 轻量级虚拟环境 |
| **Database** | System for storing and retrieving data | 存储和检索数据的系统 |
| **Deploy** | Release to production | 发布到生产环境 |
| **Docker** | Containerization platform | 容器化平台 |

### F-O

| Term | Definition | 定义 |
|------|------------|------|
| **Framework** | Pre-built structure for developing applications | 开发应用程序的预建结构 |
| **Frontend** | The user-facing part of an application | 应用程序的用户面向部分 |
| **Backend** | Server-side logic and data processing | 服务器端逻辑和数据处理 |
| **Git** | Version control system | 版本控制系统 |
| **GitHub** | Cloud platform for Git repositories | Git仓库的云平台 |
| **IDE** | Integrated Development Environment | 集成开发环境 |
| **JSON** | JavaScript Object Notation - Data format | 数据格式 |
| **MVP** | Minimum Viable Product - The simplest version that works | 最小可行产品 - 最简单的可工作版本 |

### P-Z

| Term | Definition | 定义 |
|------|------------|------|
| **PR** | Pull Request - Request to merge code changes | 请求合并代码更改 |
| **Production** | The live environment where real users access the app | 真实用户访问应用的实时环境 |
| **Repo** | Repository - Project folder | 仓库 - 项目文件夹 |
| **Sandbox** | Test environment | 测试环境 |
| **Scrum** | Agile project management method | 敏捷项目管理方法 |
| **Sprint** | Short development cycle | 短开发周期 |
| **Staging** | Pre-production testing environment | 预生产测试环境 |
| **Tech Debt** | Future cost of shortcuts taken now | 现在走捷径的未来成本 |

---

## 12. Quick Reference / 快速参考

### 12.1 Typical Project Timeline / 典型项目时间表

```
Week 1: Planning & Design
  ├── Requirements gathering
  ├── Technical specification
  └── Architecture design

Week 2-4: Development
  ├── Sprint 1: Core features
  ├── Sprint 2: Additional features
  └── Sprint 3: Refinement

Week 5: Testing & Review
  ├── QA testing
  ├── Code review
  └── Bug fixes

Week 6: Deployment
  ├── Staging deployment
  ├── User acceptance testing
  └── Production deployment
```

### 12.2 Communication Templates / 沟通模板

**Asking for a status update:** / 请求状态更新：
```
Hi team,

Could you please provide a quick status update on the [project name]?
- What's complete?
- Any blockers?
- What's next?

Thanks!
```

**Assigning a task:** / 分配任务：
```
[Name],

Could you take a look at [task]? 
It's related to [feature/bug].

Let me know if you need any clarification.

Thanks!
```

**Reporting an issue:** / 报告问题：
```
I'm seeing an issue with [feature]:

Steps to reproduce:
1. 
2. 

Expected behavior: 
Actual behavior:

Any ideas?
```

### 12.3 Useful Links / 有用链接

| Resource | URL | 资源 |
|----------|-----|------|
| GitHub | github.com | 代码托管 |
| Stack Overflow | stackoverflow.com | 技术问答 |
| MDN Web Docs | developer.mozilla.org | Web开发文档 |
| GitHub Docs | docs.github.com | GitHub文档 |

---

## Summary / 总结

### Key Takeaways / 关键要点

1. **Planning is crucial** - Spend time understanding requirements before coding / 规划至关重要 - 在编码前花时间了解需求

2. **Version control is essential** - Git tracks every change / 版本控制是必不可少的 - Git跟踪每一次更改

3. **Automation saves time** - CI/CD reduces manual work / 自动化节省时间 - CI/CD减少手动工作

4. **Testing is not optional** - Always test before deploying / 测试不是可选的 - 部署前一定要测试

5. **Communication is key** - Keep stakeholders informed / 沟通是关键 - 让利益相关者了解情况

---

*Document created as a learning resource for understanding software development workflows.*  
*本文档作为学习资源创建，用于理解软件开发工作流程。*

---

**Next Steps / 下一步：**

1. Try making a small change to the project yourself! / 尝试自己做一个小的更改！
2. Explore GitHub to see how other projects are structured / 探索GitHub，了解其他项目的结构
3. Read more about specific technologies you're interested in / 了解更多关于您感兴趣的具体技术

Remember: Even the most senior engineers started where you are now. Everyone learns by doing! / 记住：即使是最资深工程师也始于您现在的起点。每个人都是通过实践学习的！
