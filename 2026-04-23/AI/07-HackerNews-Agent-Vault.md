# 标题：Infisical发布Agent Vault：AI代理的凭证保险库

## 📋 基本信息
- **来源资讯**: GitHub/Infisical
- **阶段**: 采集

## 💡 核心观点
Infisical发布开源Agent Vault，为AI代理提供凭证代理和保险库服务，消除凭证泄露风险。

## 📖 背景信息
2026年4月23日，Infisical在GitHub上发布了Agent Vault，这是一个开源的HTTP凭证代理和保险库，专门为AI代理设计。传统密钥管理依赖直接将凭证返回给调用者，但这在AI代理场景下存在问题——AI代理是非确定性系统，容易受到提示注入攻击，可能被欺骗泄露密钥。Agent Vault采用不同方式：永远不向代理透露存储在保险库中的凭证，而是在网络层注入正确的凭证。

## 🌐 来源详情
- **国内来源**: -
- **国外来源**: Hacker News、GitHub
- **YouTube**: -

## ⭐ 值得关注
Agent Vault支持任何代理（自定义Python/TypeScript代理、Claude Code、Cursor、Codex），使用AES-256-GCM加密，支持macOS和Linux系统，可以通过curl或Docker快速部署。

## 📝 中文字幕
开源新工具Agent Vault：AI代理的凭证安全守护者

## 📝 English Subtitle
Agent Vault: Open-Source Credential Vault for AI Agents

## 📄 文章
2026年4月23日，Infisical发布了Agent Vault，这是一个开源的HTTP凭证代理和保险库，旨在解决AI代理时代的凭证安全问题。

传统密钥管理依赖直接将凭证返回给调用者，但在AI代理场景下这种方法存在严重问题。AI代理是非确定性系统，容易受到提示注入攻击，可能被欺骗泄露其密钥。攻击者可以通过精心设计的提示诱导代理暴露其存储的凭证。

Agent Vault采用了一种完全不同的安全方法：Agent Vault永远不向代理透露存储在保险库中的凭证。相反，代理通过本地代理路由HTTP请求，Agent Vault在网络层注入正确的凭证。凭证从未返回给代理，因此即使用户受到提示注入攻击，攻击者也无法获取实际的凭证。

Agent Vault的核心功能包括：

1. 代理访问而非检索 - 代理获得一个受限会话和一个本地HTTPS_PROXY。它正常调用目标API，Agent Vault在网络层注入正确的凭证。

2. 与任何代理配合工作 - 支持自定义Python/TypeScript代理、sandboxed进程，以及Claude Code、Cursor和Codex等编码代理。

3. 静态加密 - 使用AES-256-GCM和随机数据加密密钥（DEK）对凭证进行加密。可选的master password通过Argon2id包装DEK。

4. 请求日志 - 每个保险库的每个代理请求都会被持久化，记录方法、主机、路径、状态、延迟和涉及的凭证密钥名称。

安装Agent Vault非常简单，可以通过curl、Docker或从源代码构建。

## 🔄 二阶效应
随着AI代理的普及，Agent Vault等安全工具将变得越来越重要。企业将更加重视AI系统的凭证管理，凭证泄露防护将成为AI安全的标准配置。

## 🔄 逆向视角
Agent Vault虽然增强了安全性，但也增加了系统复杂性。代理需要额外的配置才能通过代理路由流量，这可能增加部署和调试的难度。

## 🎯 情景规划
- **3个月**: Agent Vault获得广泛采用
- **6个月**: 类似的开源安全工具涌现
- **1年后**: AI代理安全成为行业标准

## 🚀 行动建议
1. 在部署AI代理时考虑使用Agent Vault
2. 评估现有AI系统的凭证安全风险
3. 关注开源AI安全工具的发展
4. 为团队提供AI安全培训