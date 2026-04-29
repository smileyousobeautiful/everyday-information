# 标题：Claude Code现致命bug：HERMES.md字符串导致隐形扣费

## 📋 基本信息
- **来源资讯**: Hacker News
- **阶段**: 采集

## 💡 核心观点
Claude Code用户发现一个严重bug：git commit信息中包含"HERMES.md"字符串会导致API请求被错误路由到额外付费计费，而非套餐配额，导致用户$200隐形消费。

## 📖 背景信息
这是Anthropic Claude Code的一个计费路由bug。当git仓库的recent commit history中包含大小写敏感的字符串"HERMES.md"时，Claude Code的API请求会被静默路由到"extra usage"额外付费计费，而非用户订阅的Max计划配额。

用户报告称，其Max 20x计划（$200/月）每周可用额度仅消耗13%，却在包含该字符串的仓库中收到"You're out of extra usage"错误。经排查后发现是HERMES.md这个特定字符串触发计费路由异常。

## 🌐 来源详情
- **国内来源**: -
- **国外来源**: Hacker News
- **YouTube**: -

## ⭐ 值得关注
这是Anthropic产品中极其严重的事故。bug极其隐蔽——触发条件仅仅是commit信息文本，不涉及文件存在性，小写的"hermes.md"不触发，其他类似名称也不触发。这种静默扣费对用户信任是致命打击。

## 📝 中文字幕
Claude Code惊现隐形扣费bug！一个字符串让你多付$200

## 📝 English Subtitle
Claude Code Silent Billing Bug: One String Costs $200

## 📄 文章
一位Claude Code用户在排查计费异常时发现：无论他切换到孤立分支还是重新创建仓库，只要commit消息中包含"HERMES.md"字符串，系统就会将API调用路由到额外付费计费。

更离谱的是触发条件的精确性：
- "HERMES.md" 完全大写 → 触发
- "test HERMES.md test" → 触发
- "hermes.md" (小写) → 不触发
- "HERMES" (无扩展名) → 不触发
- "HERMES.txt" → 不触发
- 磁盘上存在HERMES.md但commit无此字符串 → 不触发

这表明Claude Code在构建系统prompt时包含了recent commit messages，而服务端某处将这个特定字符串作为计费路由的触发条件——很可能是内部测试标记被错误地应用到了生产环境。

影响：
- 用户在不知情的情况下被扣除了$200.98额外使用费
- 多个项目在额外额度耗尽后完全不可用，而套餐配额显示剩余86%+
- 错误信息完全没有提示是内容路由问题

## 🔄 二阶效应
Anthropic将紧急修复计费路由逻辑；用户会更谨慎地检查AI工具的账单；其他AI工具的类似内部标记可能被审视。

## 🔄 逆向视角
这可能是内部测试标记泄露到生产环境的结果；说明Anthropic有区分测试/生产的计费机制；问题发现后修复相对直接。

## 🎯 情景规划
如果趋势持续发展：3天内Anthropic发布修复补丁；1周内公布根本原因和补偿方案；1月内用户信任逐步恢复。

## 🚀 行动建议
Claude Code用户：立即检查你的git仓库是否有包含HERMES.md的commit历史；检查你的账单是否有未知额外扣费；可以重写包含该字符串的commit历史以暂时规避。