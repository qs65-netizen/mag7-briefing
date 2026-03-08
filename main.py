#!/usr/bin/env python3
"""
MAG7 Daily Briefing Script
Fetches MAG7 stock prices and related business news, saves as local HTML file.
"""

import os
import json
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import our modules
from stocks_data import get_mag7_stocks
from news_data import get_mag7_news


def save_html_report(stocks_data, news_data, output_path):
    """Save HTML report to local file with bilingual support."""
    
    # Build stocks table rows
    stocks_rows = ""
    for stock in stocks_data:
        change_color = "#16a34a" if stock['change_percent'] >= 0 else "#dc2626"
        change_symbol = "+" if stock['change_percent'] >= 0 else ""
        
        stocks_rows += f"""
        <tr>
            <td style="padding: 12px; border-bottom: 1px solid #e5e7eb; font-weight: 600;">{stock['symbol']}</td>
            <td style="padding: 12px; border-bottom: 1px solid #e5e7eb;">${stock['current_price']:.2f}</td>
            <td style="padding: 12px; border-bottom: 1px solid #e5e7eb; color: {change_color}; font-weight: 500;">
                {change_symbol}{stock['change_percent']:.2f}%
            </td>
        </tr>
        """
    
    # Build news items with translations
    news_items = ""
    for news in news_data:
        title_zh = news.get('title_zh', news.get('title', ''))
        desc_zh = news.get('description_zh', news.get('description', ''))
        
        news_items += f"""
        <div class="news-item" style="margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid #e5e7eb;">
            <h3 class="news-title" style="margin: 0 0 8px 0; font-size: 16px;">
                <a href="{news['url']}" style="color: #2563eb; text-decoration: none;" target="_blank">
                    <span class="en">{news['title']}</span>
                    <span class="zh" style="display:none;">{title_zh}</span>
                </a>
            </h3>
            <p class="news-desc" style="margin: 0 0 8px 0; color: #4b5563; font-size: 14px; line-height: 1.5;">
                <span class="en">{news.get('description', '')}</span>
                <span class="zh" style="display:none;">{desc_zh}</span>
            </p>
            <p style="margin: 0; color: #6b7280; font-size: 12px;">
                {news['source']} • {news['published_at']}
            </p>
        </div>
        """
    
    # Generate HTML with bilingual support
    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")
    
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ryan's Agent Debrief - {today}</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                background-color: #f4f4f5;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            }}
            .header {{
                padding: 24px;
                background: linear-gradient(135deg, #1e3a5f 0%, #2563eb 100%);
            }}
            .header h1 {{
                margin: 0;
                color: #ffffff;
                font-size: 24px;
                font-weight: 600;
            }}
            .header p {{
                margin: 8px 0 0 0;
                color: #bfdbfe;
                font-size: 14px;
            }}
            .lang-toggle {{
                text-align: right;
                padding: 12px 24px;
                background-color: #f9fafb;
                border-bottom: 1px solid #e5e7eb;
                font-size: 13px;
                color: #6b7280;
            }}
            .lang-label {{
                margin-right: 8px;
            }}
            .lang-btn {{
                background-color: #ffffff;
                border: 1px solid #e5e7eb;
                border-radius: 16px;
                padding: 4px 12px;
                font-size: 13px;
                color: #374151;
                cursor: pointer;
                transition: all 0.2s;
                margin: 0 2px;
            }}
            .lang-btn:hover {{
                border-color: #2563eb;
                color: #2563eb;
            }}
            .lang-btn.active {{
                background-color: #2563eb;
                color: #ffffff;
                border-color: #2563eb;
            }}
            .date-section {{
                padding: 16px 24px;
                background-color: #f9fafb;
                border-bottom: 1px solid #e5e7eb;
            }}
            .date-section p {{
                margin: 0;
                color: #6b7280;
                font-size: 14px;
            }}
            .content {{
                padding: 24px;
            }}
            .section-title {{
                margin: 0 0 16px 0;
                font-size: 18px;
                font-weight: 600;
                color: #111827;
            }}
            .stock-table {{
                width: 100%;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
                overflow: hidden;
            }}
            .stock-table th {{
                padding: 12px;
                text-align: left;
                font-size: 12px;
                font-weight: 600;
                color: #6b7280;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                background-color: #f9fafb;
            }}
            .stock-table td {{
                padding: 12px;
                border-bottom: 1px solid #e5e7eb;
            }}
            .news-section {{
                padding: 0 24px 24px 24px;
            }}
            .footer {{
                padding: 24px;
                background-color: #f9fafb;
                border-top: 1px solid #e5e7eb;
            }}
            .footer p {{
                margin: 0;
                color: #9ca3af;
                font-size: 12px;
                text-align: center;
            }}
            /* Chinese text hidden by default */
            .zh {{
                display: none;
            }}
            /* Show Chinese when lang is zh */
            html[lang="zh"] .en {{
                display: none;
            }}
            html[lang="zh"] .zh {{
                display: block !important;
            }}
            html[lang="zh"] .zh-inline {{
                display: inline;
            }}
            html[lang="zh"] .en-inline {{
                display: none;
            }}
            /* News translations */
            html[lang="zh"] .news-title .en {{
                display: none;
            }}
            html[lang="zh"] .news-title .zh {{
                display: inline;
            }}
            html[lang="zh"] .news-desc .en {{
                display: none;
            }}
            html[lang="zh"] .news-desc .zh {{
                display: inline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Header -->
            <div class="header">
                <h1 class="en">Daily Market Intelligence</h1>
                <h1 class="zh">每日市场情报</h1>
                <p class="en">MAG7 + ACN Stock Performance & News</p>
                <p class="zh">MAG7 + ACN 股票行情与新闻</p>
            </div>
            
            <!-- Language Toggle -->
            <div class="lang-toggle">
                <span class="lang-label en">Language:</span>
                <span class="lang-label zh" style="display:none;">语言：</span>
                <button class="lang-btn en" onclick="setLang('en')">English</button>
                <button class="lang-btn zh" onclick="setLang('zh')" style="display:none;">中文</button>
            </div>
            
            <!-- Date -->
            <div class="date-section">
                <p>
                    <span class="en">{today} • Generated at {current_time}</span>
                    <span class="zh">{today} • 生成时间 {current_time}</span>
                </p>
            </div>
            
            <!-- Stock Performance -->
            <div class="content">
                <h2 class="section-title en">The Scoreboard</h2>
                <h2 class="section-title zh">行情一览</h2>
                <table class="stock-table" cellpadding="0" cellspacing="0">
                    <thead>
                        <tr>
<th class="en">Symbol</th>
                            <th class="zh">股票代码</th>
                            <th class="en">Price</th>
                            <th class="zh">价格</th>
                            <th class="en">Change</th>
                            <th class="zh">涨跌幅</th>
                        </tr>
                    </thead>
                    <tbody>
                        {stocks_rows}
                    </tbody>
                </table>
            </div>
            
            <!-- News Section -->
            <div class="news-section">
                <h2 class="section-title en">Intelligence Brief</h2>
                <h2 class="section-title zh">新闻简报</h2>
                {news_items}
            </div>
            
            <!-- Footer -->
            <div class="footer">
                <p>
                    <span class="en">Generated by Ryan's Agent • {today}</span>
                    <span class="zh">由 Ryan's Agent 生成 • {today}</span>
                </p>
            </div>
        </div>
        
        <script>
            function setLang(lang) {{
                document.documentElement.setAttribute('lang', lang);
                localStorage.setItem('preferredLang', lang);
                
                // Update button visibility
                document.querySelectorAll('.lang-btn.en').forEach(el => {{
                    el.style.display = lang === 'en' ? 'inline-block' : 'none';
                }});
                document.querySelectorAll('.lang-btn.zh').forEach(el => {{
                    el.style.display = lang === 'zh' ? 'inline-block' : 'none';
                }});
            }}
            
            // Load preferred language
            const savedLang = localStorage.getItem('preferredLang') || 'en';
            document.documentElement.setAttribute('lang', savedLang);
            setLang(savedLang);
        </script>
    </body>
    </html>
    """
    
    # Save to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Report saved to: {output_path}")
    return output_path


def main():
    """Main function to run the briefing."""
    print(f"Starting MAG7 Daily Briefing at {datetime.now()}")
    
    # Output directory
    output_dir = Path(__file__).parent / "reports"
    output_dir.mkdir(exist_ok=True)
    
    today = datetime.now().strftime("%Y-%m-%d")
    # Use index.html for GitHub Pages compatibility
    output_file = output_dir / "index.html"
    
    try:
        # Get stock data
        print("Fetching MAG7 + ACN stock data...")
        stocks_data = get_mag7_stocks()
        print(f"Got data for {len(stocks_data)} stocks")
        
        # Get news data
        print("Fetching MAG7 + ACN news...")
        news_data = get_mag7_news()
        print(f"Got {len(news_data)} news articles")
        
        # Save HTML report
        print("Generating HTML report...")
        save_html_report(stocks_data, news_data, output_file)
        
        print("Daily briefing completed successfully!")
        print(f"\n✅ Report saved to: {output_file}")
        print("Open this file in your browser to view the briefing.")
        
    except Exception as e:
        print(f"Error in daily briefing: {e}")
        raise


if __name__ == "__main__":
    main()
