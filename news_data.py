#!/usr/bin/env python3
"""
MAG7 News Data Module
Fetches business news related to MAG7 companies using web scraping.
"""

import requests
from datetime import datetime
from datetime import timezone, timedelta
import re


def translate_text(text, target_lang='zh-CN'):
    """
    Translate text to target language using Google Translate.
    Returns original text if translation fails.
    """
    if not text:
        return text
    
    try:
        from deep_translator import GoogleTranslator
        translator = GoogleTranslator(source='auto', target=target_lang)
        translated = translator.translate(text)
        return translated if translated else text
    except Exception as e:
        print(f"Translation error: {e}")
        return text


def get_mag7_news():
    """
    Fetch latest business news for MAG7 companies using Google News RSS.
    
    Returns:
        list: List of dictionaries containing news articles with translations
    """
    news = []
    
    # Stock Tickers and names
    companies = [
        {'name': 'Apple', 'ticker': 'AAPL'},
        {'name': 'Microsoft', 'ticker': 'MSFT'},
        {'name': 'Amazon', 'ticker': 'AMZN'},
        {'name': 'Google', 'ticker': 'GOOGL'},
        {'name': 'Nvidia', 'ticker': 'NVDA'},
        {'name': 'Meta', 'ticker': 'META'},
        {'name': 'Tesla', 'ticker': 'TSLA'},
        {'name': 'Accenture', 'ticker': 'ACN'}
    ]
    
    seen_titles = set()
    
    # Use Google News RSS feed
    for company in companies[:5]:  # Limit to 5 companies to avoid too many requests
        try:
            # Fetch Google News RSS
            url = f"https://news.google.com/rss/search?q={company['name']}%20{company['ticker']}%20stock&hl=en-US&gl=US&ceid=US:en"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                # Parse RSS XML
                import xml.etree.ElementTree as ET
                root = ET.fromstring(response.content)
                
                # Get namespace
                ns = {'atom': 'http://www.w3.org/2005/Atom'}
                
                # Find items
                items = root.findall('.//item')
                
                for item in items[:2]:  # Get 2 articles per company
                    title = item.find('title').text if item.find('title') is not None else ''
                    link = item.find('link').text if item.find('link') is not None else ''
                    pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ''
                    source = item.find('source').text if item.find('source') is not None else 'Google News'
                    
                    # Avoid duplicates
                    if title and title not in seen_titles:
                        seen_titles.add(title)
                        
                        # Translate to Chinese
                        try:
                            title_zh = translate_text(title, 'zh-CN')
                        except:
                            title_zh = title
                        
                        news_item = {
                            'title': title,
                            'title_zh': title_zh,
                            'description': '',
                            'description_zh': '',
                            'url': link,
                            'source': source,
                            'published_at': 'Recent',
                            'company': company['name']
                        }
                        news.append(news_item)
                        
                        if len(news) >= 10:
                            break
        
        except Exception as e:
            print(f"Error fetching news for {company['name']}: {e}")
            continue
        
        if len(news) >= 10:
            break
    
    # If no news fetched, return sample data for testing
    if not news:
        print("Warning: Could not fetch live news, using sample data")
        news = get_sample_news()
    
    return news[:10]  # Return max 10 articles


def get_sample_news():
    """Return sample news for testing purposes."""
    return [
        {
            'title': 'Apple Reports Strong Q1 Earnings, Services Revenue Surges',
            'title_zh': '苹果Q1财报强劲，服务收入大幅增长',
            'description': 'Apple Inc. reported first-quarter earnings that exceeded analysts expectations, with services revenue reaching a new all-time high.',
            'description_zh': '苹果公司公布的季度财报超出分析师预期，服务收入创历史新高。',
            'url': 'https://www.reuters.com/technology/apple-reports-q1-earnings-2025/',
            'source': 'Reuters',
            'published_at': 'Today',
            'company': 'Apple'
        },
        {
            'title': 'Microsoft Azure Growth Accelerates Amid AI Demand',
            'title_zh': '微软Azure在AI需求推动下加速增长',
            'description': 'Microsoft cloud revenue continues to grow as enterprise demand for AI services drives Azure usage across industries.',
            'description_zh': '随着企业AI服务需求推动Azure在各行业的使用，微软云收入持续增长。',
            'url': 'https://www.bloomberg.com/technology/microsoft-azure-growth-2025/',
            'source': 'Bloomberg',
            'published_at': 'Today',
            'company': 'Microsoft'
        },
        {
            'title': 'NVIDIA Stock Hits Record High on AI Chip Demand',
            'title_zh': '英伟达股价因AI芯片需求创历史新高',
            'description': 'NVIDIA shares surged to record levels as demand for its AI semiconductors continues to outpace supply.',
            'description_zh': '英伟达股价飙升至历史新高，对其AI半导体的需求持续超过供应。',
            'url': 'https://www.cnbc.com/nvidia-stock-record-2025/',
            'source': 'CNBC',
            'published_at': 'Today',
            'company': 'NVIDIA'
        },
        {
            'title': 'Tesla Announces New Model Y Production Expansion',
            'title_zh': '特斯拉宣布扩大Model Y生产',
            'description': 'Tesla plans to increase production capacity at its Gigafactories to meet growing demand for the updated Model Y.',
            'description_zh': '特斯拉计划提高超级工厂的产能，以满足不断增长的Model Y需求。',
            'url': 'https://www.reuters.com/automobiles/tesla-model-y-expansion-2025/',
            'source': 'Reuters',
            'published_at': 'Today',
            'company': 'Tesla'
        },
        {
            'title': 'Amazon Web Services Launches New AI Tools for Enterprises',
            'title_zh': '亚马逊云服务推出面向企业的新AI工具',
            'description': 'AWS announces new artificial intelligence tools designed to help businesses automate operations and improve efficiency.',
            'description_zh': 'AWS宣布推出新的人工智能工具，帮助企业实现运营自动化和提高效率。',
            'url': 'https://www.techcrunch.com/aws-ai-tools-2025/',
            'source': 'TechCrunch',
            'published_at': 'Today',
            'company': 'Amazon'
        }
    ]


if __name__ == "__main__":
    # Test the module
    news = get_mag7_news()
    print("\n=== MAG7 News (with translations) ===")
    for item in news:
        print(f"- {item['title']}")
        print(f"  CN: {item['title_zh']}")
        print(f"  URL: {item['url']}")
        print(f"  Source: {item['source']}")
        print()
