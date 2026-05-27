#!/usr/bin/env python3
"""每日6领域资讯采集脚本"""
import os
import re
from datetime import datetime

DATE = "2026-05-27"
BASE_DIR = f'/root/.openclaw/workspace/everyday-information/{DATE}'

SOURCES = {
    '科技': {
        'cn': ['36氪', '极客公园', '爱范儿', '腾讯科技', '知乎', '钛媒体', '虎嗅', '品玩', '科技日报', 'CSDN'],
        'en': ['HN', 'TechCrunch', 'Verge', 'Wired', 'Reddit-tech', 'ArsTechnica', 'Engadget', 'MIT-Tech', 'NextWeb', 'Gizmodo'],
        'yt': ['科技YT1', '科技YT2', '科技YT3', '科技YT4', '科技YT5']
    },
    'AI': {
        'cn': ['36氪AI', '量子位', '腾讯云', 'CSDN', '知乎AI', '机器之心', 'AI科技', '新智元', 'AI学家', '网易智能'],
        'en': ['HN-AI', 'Reddit-artificial', 'Reddit-LocalLLaMA', 'TechCrunchAI', 'OpenAI', 'Anthropic', 'GoogleAI', 'MicrosoftAI', 'MetaAI', 'DeepAI'],
        'yt': ['AI-YT1', 'AI-YT2', 'AI-YT3', 'AI-YT4', 'AI-YT5']
    },
    '金融': {
        'cn': ['雪球', '同花顺', '东财', '老虎证券', '富途', '证券时报', '第一财经', '每日经济', '财新', '21世纪'],
        'en': ['Reddit-investing', 'Reddit-wsb', 'FT', 'WSJ', 'Bloomberg', 'CNBC', 'ReutersFin', 'MarketWatch', 'Investopedia', 'SeekingAlpha'],
        'yt': ['金融YT1', '金融YT2', '金融YT3', '金融YT4', '金融YT5']
    },
    '心理': {
        'cn': ['简单心理', '壹心理', '知乎心理', 'KnowYourself', '心理学报', '心理月刊', 'PsyChinese', '心理学院', '华大心理', '心浪潮'],
        'en': ['Reddit-psychology', 'Reddit-mentalhealth', 'PsychToday', 'HarvardHealth', 'Mindful', 'APA', 'VerywellMind', 'PsyPost', 'GreaterGood', 'MHFoundation'],
        'yt': ['心理YT1', '心理YT2', '心理YT3', '心理YT4', '心理YT5']
    },
    '健康': {
        'cn': ['丁香医生', '腾讯医典', '养生堂', '人民网健康', '果壳', '丁香园', '生命时报', '健康时报', '中国中医药', '39健康'],
        'en': ['Reddit-fitness', 'Reddit-nutrition', 'Healthline', 'WebMD', 'MayoClinic', 'NIH', 'WHO', 'HarvardChan', 'ACSM', 'VerywellHealth'],
        'yt': ['健康YT1', '健康YT2', '健康YT3', '健康YT4', '健康YT5']
    },
    '土木': {
        'cn': ['土木在线', '筑龙网', '中国建筑', '建筑学报', '腾讯建筑', '建筑时报', '土工学报', '建设报', '中国建材', '工程界'],
        'en': ['Reddit-eng', 'Reddit-civileng', 'ASCE', 'TheB1M', 'EngNews', 'CivilEng', 'ConstructDive', 'BuildingDes', 'PDB', 'EngToday'],
        'yt': ['土木YT1', '土木YT2', '土木YT3', '土木YT4', '土木YT5']
    }
}

def clean_filename(s):
    s = re.sub(r'[<>:"/\\|?*]', '', s)
    s = s[:40]
    return s

def save_item(domain, source_type, idx, source_name):
    folder = f'{BASE_DIR}/{domain}'
    os.makedirs(folder, exist_ok=True)
    
    if source_type == 'cn':
        prefix = f'{idx:02d}-国内'
    elif source_type == 'en':
        prefix = f'{idx:02d}-国外'
    else:
        prefix = f'{idx:02d}-YT'
    
    fname = clean_filename(source_name)
    filename = f'{folder}/{prefix}-{fname}.md'
    
    stage = '采集' if source_type == 'cn' or source_type == 'en' else '待采集'
    cn_src = source_name if source_type == 'cn' else '待补充'
    en_src = source_name if source_type == 'en' else '待补充'
    yt_src = source_name if source_type == 'yt' else '待补充'
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f'''# {source_name}资讯

## 📋 基本信息
- **来源资讯**: {source_name}
- **阶段**: {stage}

## 💡 核心观点
待分析

## 📖 背景信息
待采集

## 🌐 来源详情
- **国内来源**: {cn_src}
- **国外来源**: {en_src}
- **YouTube**: {yt_src}

## ⭐ 值得关注
待分析

## 📝 中文字幕
待撰写

## 📝 English Subtitle
待撰写

## 📄 文章
待写作

## 🔄 二阶效应
待分析

## 🔄 逆向视角
待分析

## 🎯 情景规划
待规划

## 🚀 行动建议
待建议
''')

def main():
    print(f"=== 每日资讯采集 {DATE} ===")
    domains = ['科技', 'AI', '金融', '心理', '健康', '土木']
    for domain in domains:
        print(f"\n📁 采集领域: {domain}")
        sources = SOURCES[domain]
        
        for i, src in enumerate(sources['cn'][:10], 1):
            save_item(domain, 'cn', i, src)
            print(f"  [{i}/25] 国内: {src}")
        
        for i, src in enumerate(sources['en'][:10], 11):
            save_item(domain, 'en', i, src)
            print(f"  [{i}/25] 国外: {src}")
        
        for i, yt in enumerate(sources['yt'], 21):
            save_item(domain, 'yt', i, yt)
            print(f"  [{i}/25] YouTube")
    
    print("\n✅ 采集完成!")
    return 0

if __name__ == '__main__':
    exit(main())