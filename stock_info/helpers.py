import requests
import csv
import json
import logging

from typing import Any, Union
from random import randint

def get_headers() -> tuple[dict[str, Any], dict[str, Any]]:
    """
    Returns required headers and cookies to make api request with required token
    Keyword arguments:
    Return: tuple(headers, cookies)
    """
    
    homeurl = "https://www.barchart.com/"
    
    with open("User Agents.csv", "r") as agents:
        agents_list = [agent for agent in csv.DictReader(agents) if agent["referer"] == homeurl]
    # Choose random int to index between 0 and the length of the list of dicts
    rand = randint(0, (len(agents_list) - 1))
    headers = agents_list[rand]
    homepage = requests.get(url=homeurl, headers=headers)
    cookies: int = dict(homepage.cookies)
    headers["x-xsrf-token"] = cookies.get("XSRF-TOKEN").removesuffix("%3D") + "="
    request_cookies = {
        'XSRF-TOKEN': cookies['XSRF-TOKEN'],
        'laravel_token=': cookies['laravel_token'],
    }
    return headers, request_cookies

def get_stock_response(ticker: str, headers: dict, request_cookies: dict) -> requests.Response:
    
    url = "https://www.barchart.com/proxies/core-api/v1/quotes/get"
    
    with open("stock_info/fields.txt", "r") as txt:
        fields = txt.read()

    querystring = {
        "fields":fields,
        "raw": 1,
        "symbols":ticker,
        }
    
    response = requests.get(url=url, headers=headers, params=querystring, cookies=request_cookies)
    
    content = json.loads(response.content)
    
    rate_limit_remaining = f"{response.headers.get('x-ratelimit-remaining')}/{response.headers.get('x-ratelimit-limit')}"
    
    # Add the rate limit to stock_info content
    content["rate-limit"] = rate_limit_remaining
    
    return content