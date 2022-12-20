import uvicorn

from fastapi import FastAPI
from financial_statements.main import get_statement
app = FastAPI()


@app.get("/")
def root():
    message = {
        "Code": "200",
        "message": "You've succesfully reached Financial_API",
    }
    return message

@app.get("/stockinfo/")
def ticker(ticker: str = "BRK.A"):
    return {"Ticker": ticker}

@app.get("/financials/")
def get_arg_values():
    return {"details":"Keys are input and values are expected result",
            "is":"Income Statement",
            "cfs": "Cash-Flow Statement",
            "bs":"Balance Sheet"}

@app.get("/financials/{statement_type}/")
def financials(statement_type: str, ticker: str, years_of_data: int = 5):
    
    return get_statement(statement_type, ticker, years_of_data)

if __name__ == "__main__":
    uvicorn.run("server.api:app", host="0.0.0.0", port=8000, reload=True)
