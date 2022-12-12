from financial_statements.helpers import Results, load_pages, prepare_template, fill_dict, adjustment_statement


def get_statement(statement_type: str, ticker: str, years_of_data: int):
    # if statement_type == "is":
    #     statement_type = "income-statement"
    # elif statement_type == "cfs":
    #     statement_type = "cash-flow"
    # elif statement_type == "bs":
    #     statement_type = "balance-sheet"
    # else:
    #     return {"Code": 400, "Statement Type": "Incorrect"}
          
        
    # max_pages = get_max_pages(years_of_data)
    # results = [None] * max_pages
    # thread_list = []
    # statement = {}
    # statement["Ticker"] = ticker.upper()
    # statement["Statement Type"] = statement_type    
    # statement["Years Of Data"] = 0
    # statement["Yearly Data"] = []
    
    results = Results(years_of_data, ticker, statement_type)
    
    results.results = load_pages(results.ticker, results.statement_type, results.max_pages, results.thread_list, results.results)

    results.statement = prepare_template(results.results, results.statement, results.statement_type)
    
    results.statement = fill_dict(results.results, results.statement)
    
    results.statement = adjustment_statement(results.statement, results.statement_type)
    
    return results.statement