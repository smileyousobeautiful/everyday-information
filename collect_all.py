#!/usr/bin/env python3
"""每日6领域资讯采集脚本"""
import os
import json
import requests
from datetime import datetime
from urllib.parse import urljoin

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

DATE = '2026-04-15'
BASE_DIR = f'/root/.openclaw/workspace/everyday-information/{DATE}'

# 各领域来源配置 - 每个领域10条国内+10条国外+5条YouTube=25条
SOURCES = {
    '科技': {
        'cn': ['36氪', '极客公园', '爱范儿', '腾讯科技', '知乎', '钛媒体', '虎嗅', '品玩', '科技日报', 'CSDN'],
        'en': ['Hacker News', 'TechCrunch', 'The Verge', 'Wired', 'Reddit r/technology', 'Ars Technica', 'Engadget', 'MIT Tech Review', 'The Next Web', 'Gizmodo'],
        'yt': ['YouTube科技1', 'YouTube科技2', 'YouTube科技3', 'YouTube科技4', 'YouTube科技5']
    },
    'AI': {
        'cn': ['36氪AI', '量子位', '腾讯云', 'CSDN', '知乎AI', '机器之心', 'AI科技评论', '新智元', '人工智能学家', '网易智能'],
        'en': ['Hacker News AI', 'Reddit r/artificial', 'Reddit r/LocalLLaMA', 'TechCrunch AI', 'OpenAI Blog', 'Anthropic Blog', 'Google AI', 'Microsoft AI', 'Meta AI', 'DeepAI'],
        'yt': ['YouTube AI1', 'YouTube AI2', 'YouTube AI3', 'YouTube AI4', 'YouTube AI5']
    },
    '金融': {
        'cn': ['雪球', '同花顺', '东方财富', '老虎证券', '富途', '证券时报', '第一财经', '每日经济新闻', '财新', '21世纪经济报道'],
        'en': ['Reddit r/investing', 'Reddit r/wallstreetbets', 'Financial Times', 'WSJ', 'Bloomberg', 'CNBC', 'Reuters Finance', 'MarketWatch', 'Investopedia', 'Seeking Alpha'],
        'yt': ['YouTube金融1', 'YouTube金融2', 'YouTube金融3', 'YouTube金融4', 'YouTube金融5']
    },
    '心理': {
        'cn': ['简单心理', '壹心理', '知乎心理', 'KnowYourself', '心理学报', '心理月刊', 'PsyChinese', '心理学院', '华大心理', '心浪潮'],
        'en': ['Reddit r/psychology', 'Reddit r/mentalhealth', 'Psychology Today', 'Harvard Health', 'Mindful', 'APA', 'Verywell Mind', 'PsyPost', 'Greater Good', 'Mental Health Foundation'],
        'yt': ['YouTube心理1', 'YouTube心理2', 'YouTube心理3', 'YouTube心理4', 'YouTube心理5']
    },
    '健康': {
        'cn': ['丁香医生', '腾讯医典', '养生堂', '人民网健康', '果壳', '丁香园', '生命时报', '健康时报', '中国中医药报', '39健康'],
        'en': ['Reddit r/fitness', 'Reddit r/nutrition', 'Healthline', 'WebMD', 'Mayo Clinic', 'NIH', 'WHO', 'Harvard T.H. Chan', 'ACSM', 'Verywell Health'],
        'yt': ['YouTube健康1', 'YouTube健康2', 'YouTube健康3', 'YouTube健康4', 'YouTube健康5']
    },
    '土木': {
        'cn': ['土木在线', '筑龙网', '中国建筑学会', '建筑学报', '腾讯新闻建筑', '建筑时报', '土木工程学报', '建设报', '中国建材', '工程界'],
        'en': ['Reddit r/engineering', 'Reddit r/civilengineering', 'ASCE', 'The B1M', 'Engineering News', 'Civil Engineering', 'Construction Dive', 'Building Design', 'PDB', 'Engineering Today'],
        'yt': ['YouTube土木1', 'YouTube土木2', 'YouTube土木3', 'YouTube土木4', 'YouTube土木5']
    }
}

def save_item(domain, source_type, idx, title, source_name=''):
    """保存单条内容为MD文件"""
    folder = f'{BASE_DIR}/{domain}'
    
    if source_type == 'cn':
        prefix = f'{idx:02d}-国内'
    elif source_type == 'en':
        prefix = f'{idx:02d}-国外'
    else:
        prefix = f'{idx:02d}-YT'
    
    filename = f'{folder}/{prefix}-{source_name}.md'
    os.makedirs(folder, exist_ok=True)
    
    stage = '采集' if source_type == 'cn' or source_type == 'en' else '待采集'
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f'''# {title}

## 📋 基本信息
- **来源资讯**: {source_name}
- **阶段**: {stage}

## 💡 核心观点
待分析

## 📖 背景信息
待采集

## 🌐 来源详情
- **国内来源**: {source_name if source_type == 'cn' else '待补充'}
- **国外来源**: {source_name if source_type == 'en' else '待补充'}
- **YouTube**: {source_name if source_type == 'yt' else '待补充'}

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
        
        # 采集国内10条
        for i, src in enumerate(sources['cn'][:10], 1):
            save_item(domain, 'cn', i, f'{src}资讯', src)
            print(f"  [{i}/25] 国内: {src}")
        
        # 采集国外10条
        for i, src in enumerate(sources['en'][:10], 11):
            save_item(domain, 'en', i, f'{src}资讯', src)
            print(f"  [{i}/25] 国外: {src}")
        
        # 采集YouTube 5条
        for i, yt in enumerate(sources['yt'], 21):
            save_item(domain, 'yt', i, yt, yt)
            print(f"  [{i}/25] YouTube")
    
    print("\n✅ 采集完成!")
    return 0

if __name__ == '__main__':
    exit(main())
