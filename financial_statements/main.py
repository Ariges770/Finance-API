from financial_statements.helpers import get_max_pages, load_pages, prepare_template, fill_dict, adjustment_statement


def get_statement(statement_type: str, ticker: str, years_of_data: int):
    if statement_type == "is":
        statement_type = "income-statement"
    elif statement_type == "cfs":
        statement_type = "cash-flow"
    elif statement_type == "bs":
        statement_type = "balance-sheet"
    else:
        return {"Code": 400, "Statement Type": "Incorrect"}
          
        
    max_pages = get_max_pages(years_of_data)
    results = [None] * max_pages
    thread_list = []
    statement = {}
    statement["Ticker"] = ticker.upper()
    statement["Statement Type"] = statement_type    
    statement["Years Of Data"] = 0
    statement["Yearly Data"] = []
    
    results = load_pages(ticker, statement_type, max_pages, thread_list, results)

    statement = prepare_template(results, statement, statement_type)
    
    statement = fill_dict(results, statement)
    
    statement = adjustment_statement(statement, statement_type)
    
    return statement