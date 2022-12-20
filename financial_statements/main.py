from financial_statements.helpers import Results, load_pages, prepare_template, fill_dict, adjustment_statement


def get_statement(statement_type: str, ticker: str, years_of_data: int):
    
    results = Results(years_of_data, ticker, statement_type)
    
    results.results = load_pages(results.ticker, results.statement_type, results.max_pages, results.thread_list, results.results)

    results.statement = prepare_template(results.results, results.statement, results.statement_type)
    
    results.statement = fill_dict(results.results, results.statement)
    
    results.statement = adjustment_statement(results.statement, results.statement_type)
    
    return results.statement