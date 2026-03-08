#!/usr/bin/env python3
"""
MAG7 Stock Data Module
Fetches stock prices for Magnificent Seven companies.
"""

import yfinance as yf
from datetime import datetime


# Stock Tickers (MAG7 + ACN)
MAG7_TICKERS = {
    'AAPL': 'Apple',
    'MSFT': 'Microsoft', 
    'AMZN': 'Amazon',
    'GOOGL': 'Alphabet (Google)',
    'NVDA': 'NVIDIA',
    'META': 'Meta',
    'TSLA': 'Tesla',
    'ACN': 'Accenture'
}


def get_mag7_stocks():
    """
    Fetch current stock data for MAG7 companies.
    
    Returns:
        list: List of dictionaries containing stock data
    """
    stocks = []
    
    for ticker_symbol, company_name in MAG7_TICKERS.items():
        try:
            # Get ticker data
            ticker = yf.Ticker(ticker_symbol)
            
            # Get today's data
            history = ticker.history(period="1d")
            
            if history.empty:
                print(f"Warning: No data available for {ticker_symbol}")
                continue
            
            # Get current price and previous close
            current_price = history['Close'].iloc[-1]
            previous_close = history['Open'].iloc[0] if len(history) > 0 else current_price
            
            # Calculate change
            change = current_price - previous_close
            change_percent = (change / previous_close) * 100 if previous_close > 0 else 0
            
            stock_info = {
                'symbol': ticker_symbol,
                'company': company_name,
                'current_price': round(current_price, 2),
                'previous_close': round(previous_close, 2),
                'change': round(change, 2),
                'change_percent': round(change_percent, 2)
            }
            
            stocks.append(stock_info)
            print(f"Got data for {ticker_symbol}: ${current_price:.2f} ({change_percent:+.2f}%)")
            
        except Exception as e:
            print(f"Error fetching data for {ticker_symbol}: {e}")
            continue
    
    return stocks


def get_stock_info(ticker_symbol):
    """Get detailed stock info for a specific ticker."""
    try:
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info
        return info
    except Exception as e:
        print(f"Error fetching info for {ticker_symbol}: {e}")
        return None


if __name__ == "__main__":
    # Test the module
    stocks = get_mag7_stocks()
    print("\n=== MAG7 Stock Data ===")
    for stock in stocks:
        print(f"{stock['symbol']}: ${stock['current_price']} ({stock['change_percent']:+.2f}%)")
