# STYLAN's Notes

> 我的学习笔记，记录技术成长与思考

[![GitHub Stars](https://img.shields.io/github/stars/duan-deqing/notes.svg?style=flat-square&label=Stars)](https://github.com/duan-deqing/notes)
[![GitHub Forks](https://img.shields.io/github/forks/duan-deqing/notes.svg?style=flat-square&label=Forks)](https://github.com/duan-deqing/notes/fork)
[![GitHub Issues](https://img.shields.io/github/issues/duan-deqing/notes.svg?style=flat-square&label=Issues)](https://github.com/duan-deqing/notes/issues)
[![GitHub License](https://img.shields.io/github/license/duan-deqing/notes.svg?style=flat-square&label=License)](https://github.com/duan-deqing/notes/blob/main/LICENSE)

## 📚 项目介绍

这是一个基于 MkDocs + Material 主题构建的个人技术笔记仓库，用于记录学习过程中的技术总结、实践经验和思考感悟。

## ✨ 特性

- 🎨 **现代化界面**: 使用 Material Design 风格，支持深色/浅色模式自动切换
- 🔍 **全文搜索**: 内置强大的搜索功能，快速定位所需内容
- 📱 **响应式设计**: 完美适配桌面端和移动端
- 🚀 **快速部署**: 集成 GitHub Actions 自动部署到 GitHub Pages
- 📝 **Markdown 编写**: 使用简洁的 Markdown 语法，专注内容创作

## 🚀 快速开始

### 环境要求

- Python 3.8+
- MkDocs 1.4+
- MkDocs Material 9.0+

### 本地运行

```bash
# 克隆仓库
git clone https://github.com/duan-deqing/notes.git

# 进入项目目录
cd notes

# 安装依赖
pip install -r requirements.txt

# 启动开发服务器
mkdocs serve

# 访问 http://localhost:8000
```

### 构建静态文件

```bash
mkdocs build
```

## 📁 项目结构

```
notes/
├── docs/                 # 文档目录
│   ├── index.md         # 首页
│   ├── about.md         # 关于
│   └── ...              # 其他文档
├── .github/
│   └── workflows/
│       └── docs.yml     # GitHub Actions 配置
├── mkdocs.yml           # MkDocs 配置文件
├── requirements.txt     # 依赖列表
└── README.md            # 项目说明
```

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🙏 致谢

- [MkDocs](https://www.mkdocs.org/) - 静态站点生成器
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) - 现代化主题
- [GitHub Pages](https://pages.github.com/) - 免费的静态站点托管服务

## 📞 联系方式

- GitHub: [@duan-deqing](https://github.com/duan-deqing)
- 邮箱: duan_deqing@163.com

---

⭐️ 如果这个项目对你有帮助，请给它一个 Star！
