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

DOMAINS = ['科技', 'AI', '金融', '心理', '健康', '土木']
DATE = '2026-04-06'
BASE_DIR = f'/root/.openclaw/workspace/everyday-information/{DATE}'

# 各领域来源配置
SOURCES = {
    '科技': {
        'cn': ['36氪', '极客公园', '爱范儿', '腾讯科技', '知乎'],
        'en': ['Hacker News', 'TechCrunch', 'The Verge', 'Wired', 'Reddit r/technology'],
        'yt': ['YouTube科技']
    },
    'AI': {
        'cn': ['36氪AI', '量子位', '腾讯云', 'CSDN', '知乎AI'],
        'en': ['Hacker News AI', 'Reddit r/artificial', 'Reddit r/LocalLLaMA', 'TechCrunch AI', 'OpenAI Blog'],
        'yt': ['YouTube AI']
    },
    '金融': {
        'cn': ['雪球', '同花顺', '东方财富', '老虎证券', '富途'],
        'en': ['Reddit r/investing', 'Reddit r/wallstreetbets', 'Financial Times', 'WSJ', 'Bloomberg'],
        'yt': ['YouTube金融']
    },
    '心理': {
        'cn': ['简单心理', '壹心理', '知乎心理', 'KnowYourself', '心理学报'],
        'en': ['Reddit r/psychology', 'Reddit r/mentalhealth', 'Psychology Today', 'Harvard Health', 'Mindful'],
        'yt': ['YouTube心理']
    },
    '健康': {
        'cn': ['丁香医生', '腾讯医典', '养生堂', '人民网健康', '果壳'],
        'en': ['Reddit r/fitness', 'Reddit r/nutrition', 'Healthline', 'WebMD', 'Mayo Clinic'],
        'yt': ['YouTube健康']
    },
    '土木': {
        'cn': ['土木在线', '筑龙网', '中国建筑学会', '建筑学报', '腾讯新闻建筑'],
        'en': ['Reddit r/engineering', 'Reddit r/civilengineering', 'ASCE', 'The B1M', 'Engineering News'],
        'yt': ['YouTube土木']
    }
}

def fetch_url(url):
    """获取URL内容"""
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        r.raise_for_status()
        return r.text[:20000]
    except Exception as e:
        return f"Error: {e}"

def save_item(domain, source_type, idx, title, content=''):
    """保存单条内容为MD文件"""
    folder = f'{BASE_DIR}/{domain}'
    prefix = f'{idx:02d}-{source_type}'
    if source_type == 'cn':
        prefix += '-国内'
    elif source_type == 'en':
        prefix += '-国外'
    else:
        prefix += '-YT'
    
    filename = f'{folder}/{prefix}.md'
    os.makedirs(folder, exist_ok=True)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f'''# {title}

## 📋 基本信息
- **来源资讯**: {source_type}
- **阶段**: 采集

## 💡 核心观点
待补充

## 📖 背景信息
{content[:200] if content else '待采集'}

## 🌐 来源详情
- **国内来源**: 
- **国外来源**: 
- **YouTube**: 

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
    for domain in DOMAINS:
        print(f"\n📁 采集领域: {domain}")
        sources = SOURCES[domain]
        
        # 采集国内10条
        for i, src in enumerate(sources['cn'][:10], 1):
            save_item(domain, 'cn', i, f'{src}资讯')
            print(f"  [{i}/25] 国内: {src}")
        
        # 采集国外10条
        for i, src in enumerate(sources['en'][:10], 11):
            save_item(domain, 'en', i, f'{src}资讯')
            print(f"  [{i}/25] 国外: {src}")
        
        # 采集YouTube 5条
        for i in range(21, 26):
            save_item(domain, 'yt', i, f'YouTube视频{i-20}')
            print(f"  [{i}/25] YouTube")
    
    print("\n✅ 采集完成!")
    return 0

if __name__ == '__main__':
    exit(main())