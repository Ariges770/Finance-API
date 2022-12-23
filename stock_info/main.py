from stock_info.helpers import get_headers, get_stock_response

"""
Pseudo code:

generate xsrf token 

retrieve stock info
"""

def get_stock_info(ticker: str) -> dict:
    
    ticker = ticker.strip().upper()
    
    headers, cookies = get_headers()
    
    stock_info = get_stock_response(ticker, headers, cookies)
    
    return stock_info