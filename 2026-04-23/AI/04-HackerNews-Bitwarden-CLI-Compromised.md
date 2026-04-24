# 标题：Bitwarden CLI被植入恶意代码 - 供应链攻击再添新受害者

## 📋 基本信息
- **来源资讯**: Socket安全研究团队
- **阶段**: 采集

## 💡 核心观点
Bitwarden CLI 2026.4.0在Checkmarx供应链攻击活动中被 compromise，恶意代码瞄准开发者凭证。

## 📖 背景信息
2026年4月23日，Socket安全研究团队发现开源密码管理器Bitwarden的CLI工具在最新的供应链攻击活动中被 compromise。Bitwarden为超过1000万用户和5万多家企业提供密码管理服务，是企业采用最多的三大密码管理器之一。受影响的版本是@bitwarden/cli 2026.4.0，恶意代码被嵌入在bw1.js文件中。攻击似乎利用了Bitwarden CI/CD管道中受损的GitHub Action。

## 🌐 来源详情
- **国内来源**: -
- **国外来源**: Hacker News、Socket.dev
- **YouTube**: -

## ⭐ 值得关注
这是Checkmarx供应链攻击活动的最新受害者。恶意代码针对GitHub Actions Runner、AWS、Azure、GCP凭证以及Claude/MCP配置。俄罗斯语系的系统会静默退出，这可能是攻击者的"自毁开关"。

## 📝 中文字幕
密码管理器Bitwarden CLI被植入后门，超过1000万用户受影响

## 📝 English Subtitle
Bitwarden CLI Compromised in Supply Chain Attack, 10M+ Users Affected

## 📄 文章
2026年4月23日，Socket安全研究团队发现Bitwarden CLI在Checkmarx供应链攻击活动中被 compromise。Bitwarden是全球最受欢迎的开源密码管理器之一，为超过1000万个人用户和5万多家企业提供密码管理服务。

受影响的版本是@bitwarden/cli 2026.4.0，恶意代码被嵌入在bw1.js文件中。攻击者利用了Bitwarden CI/CD管道中受损的GitHub Action，这与该活动中其他受影响仓库的模式一致。

恶意payload包含以下功能：
- 使用与Checkmarx相同的C2端点（audit.checkmarx[.]cx/v1/telemetry）
- 针对GitHub Actions Runner的Python内存抓取脚本
- 从~/.aws/文件和环境变量中获取AWS凭证
- 通过azd获取Azure令牌
- 通过gcloud config config-helper获取GCP凭证
- 窃取npm配置文件(.npmrc)、SSH密钥和环境变量
- 窃取Claude/MCP配置文件

攻击者还创建了以Dune为主题的公开仓库（使用{word}-{word-{3digits}命名模式），使用加密结果进行提交，并在提交消息中嵌入令牌，标记为"LongLiveTheResistanceAgainstMachines"。

俄罗斯语系统的系统会静默退出，这似乎是攻击者的自毁开关。恶意代码还会在~/.bashrc和~/.zshrc中注入payload以实现持久化。

## 🔄 二阶效应
供应链攻击持续困扰开源生态系统，开发者需要更加警惕其使用的工具。GitHub Actions的安全性成为关注焦点。企业可能加速采用软件供应链安全工具。

## 🔄 逆向视角
虽然这次攻击利用了CI/CD管道的弱点，但也暴露了密码管理器作为高价值目标的风险。攻击者越来越多地将目标对准开发者工具，以获取有价值的凭证。

## 🎯 情景规划
- **3个月**: 更多供应链攻击事件可能被曝光
- **6个月**: GitHub和npm加强安全措施
- **1年后**: 软件供应链安全成为行业标准

## 🚀 行动建议
1. 立即检查是否使用了Bitwarden CLI 2026.4.0版本
2. 轮换在受影响环境中可能暴露的任何凭证
3. 检查GitHub是否有未经授权的仓库创建
4. 审核npm是否有未经授权的发布
5. 考虑使用Socket等供应链安全工具