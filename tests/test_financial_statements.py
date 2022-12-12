from financial_statements.helpers import *
from app import app
import pytest
from typing import Union
from fastapi.testclient import TestClient


client = TestClient(app)


class Parameters():
    
    def __init__(self) -> None:
        self.tickers_params =  [
        {"ticker":"jpm", "years_of_data":50}, 
        {"ticker":"aapl", "years_of_data":5}, 
        {"ticker":"sofi", "years_of_data": 10}, 
        {"ticker":"flt.ax", "years_of_data":25}, 
        {"ticker":"cba.ax", "years_of_data":5}, 
        {"ticker":"asc.ln", "years_of_data":5},
        ]
        
        self.statement_types = (
        "cfs", 
        "is", 
        "bs",
        )
        
        self.results = []
        self.ticker_results()
    
    def ticker_results(self):
        for test_ticker in self.tickers_params:
            for test_statement_type in self.statement_types:
                max_pages = get_max_pages(test_ticker["years_of_data"])
                self.results.append(Results(max_pages, test_ticker["ticker"], test_statement_type))
                

                
test_params = Parameters()
                

def test_max_pages():
    assert get_max_pages(years_of_data=50) == 10
    assert get_max_pages(years_of_data=2) == 1

@pytest.mark.parametrize("test_stock_results", test_params.results)
def test_load_pages_function(test_stock_results: Results):
    results = test_stock_results
    results.results = load_pages(results.ticker, results.statement_type, results.max_pages, results.thread_list, results.results)
    test_results = results.results[0]
    assert test_results.status_code == 200

@pytest.mark.parametrize("test_stock_results", test_params.results)
def test_fill_results_function(test_stock_results: Results):
    results = test_stock_results
    results.statement = prepare_template(results.results, results.statement, results.statement_type)
    assert len(results.statement["Yearly Data"]) >= 1

@pytest.mark.parametrize("test_stock_results", test_params.results)
def test_fill_dict_function(test_stock_results: Results):
    results = test_stock_results
    results.statement = fill_dict(results.results, results.statement)
    assert results.statement

@pytest.mark.parametrize("test_stock_results", test_params.results)
def test_adjustment_function(test_stock_results: Results):
    results = test_stock_results
    results.statement = adjustment_statement(results.statement, results.statement_type)
    assert results.statement
            
