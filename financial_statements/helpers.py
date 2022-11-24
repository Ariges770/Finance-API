import threading
import requests
import csv

from time import sleep
from random import randint, random
from bs4 import BeautifulSoup

def getStatement(ticker: str, statement_type: str, page: int, index: int, results: list):
    
    with open("User Agents.csv", "r") as agents:
        agents_list = [agent for agent in csv.DictReader(agents)]
    rand = randint(0, (len(agents_list) - 1))
    headers = agents_list[rand]
    # headers = {
    #     'authority': 'www.barchart.com',
    #     'referer': f'https://www.barchart.com/stocks/quotes/{ticker}/{statement_type}/annual',
    #     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104", "Opera GX";v="90"',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117',
    # }
    params = {
        'reportPage': page,
    }
    response = requests.get(f'https://www.barchart.com/stocks/quotes/{ticker}/{statement_type}/annual', params=params, headers=headers)
    results[index] = response
def load_pages(ticker: str, statement_type, max_pages: int, thread_list: list, results: list):

    # Add threads to list the size of the number of pages searched
    for page, index in enumerate(range(max_pages), 1):
        t = threading.Thread(target=getStatement, args=(ticker,statement_type,page,index,results))
        thread_list.append(t)

    # Start threads and ensure they are all completed before continuing
    for thread in thread_list:
        thread.start()
        sleep(random())

    for thread in thread_list:
        thread.join()
    return results

def prepare_template(results: list, statement: dict, statement_type: str):
    # Create dict with all statement keys set to None
    for page, table in enumerate(results):
        soup = BeautifulSoup(table.text, "lxml")
        if soup.findAll("barchart-table-scroll"):
            # Find all table rows
            table = soup.find("table").find_all("tr")

            # Add years as keys to statement dict
            for td in table[0].find_all("td"):
                if td.contents[0] == "\xa0":
                    pass
                else:
                    year = td.contents[0].strip()
                    statement["Yearly Data"].append({"Financial Year": year})
                    
            for tr in table[1:]:
                # Skip the row separators
                if tr["class"]:
                    if tr["class"][0] == "bc-financial-report__row-separator":
                        continue
                # Set the statment key as the value header (E.G. COGS)
                key = tr.find_all("td")[0].string.strip()
                    
                # Add keys to dictionary including addition keys not included
                for list_index, year in enumerate(statement["Yearly Data"]):
                    years_data = statement["Yearly Data"][list_index]
                    if statement_type == "income-statement":
                        
                        if key == "Ebitda":
                            # Add Weighted Basic/Diluted Average Shares Outstanding Keys
                            years_data["Weighted Average Basic Shares Outstanding"] = None
                            years_data["Weighted Average Diluted Shares Outstanding"] = None
                            
                    elif statement_type == "cash-flow":
                        pass
                    
                    elif statement_type == "balance-sheet":
                        # Add Totals keys
                        if key == "TOTAL":
                            years_data["Total Current Assets"] = None
                        if key == "Total Assets":
                            years_data["Total Non-Current Assets"] = None
                        if key == "Non-Current Liabilities":
                            years_data["Total Current Liabilities"] = None
                        if key == "Total Liabilities":
                            years_data["Total Non-Current Liabilities"] = None
                        if key == "Total Liabilities And Equity":
                            years_data["Total Shareholders' Equity"] = None
                    else:
                        raise("Incorrect statement_type")
                            
                    years_data[key] = None

    return statement

def fill_dict(results: list, statement: dict):
    # Loop through each page to extract the contents of 5Y at a time and load page to BeautifulSoup
    for page, table in enumerate(results):
        soup = BeautifulSoup(table.text, "lxml")
        # Ensure the correct table exists (Financial statements)
        if soup.findAll("barchart-table-scroll"):
            # Find all table rows
            table = soup.find("table").find_all("tr")
            statement["Years Of Data"] += 5

            # Loop through each row of the table to add to dict
            for tr in table[1:]:
                # Skip the row separators
                if tr["class"]:
                    if tr["class"][0] == "bc-financial-report__row-separator":
                        continue
                # Set key to be first column of the table for each row and clean up
                key = tr.find_all("td")[0].string.strip()

                # Go through each data box in the row selected, clean up and add to dict
                for list_index, td in enumerate(tr.find_all("td")[1:]):
                    if td.string:
                        value = td.string.strip()
                    else:
                        value = td.string
                    # Set "N/A" to be None
                    if value != None:
                        if value.removeprefix("$") == "N/A":
                            value = None
                    
                    # Set year_index as column number plus the pages done times 5, years_statement is the dict entry for that years data
                    year_index = (list_index) + (page * 5)
                    years_statement = statement["Yearly Data"][year_index]
                    
                    # Add the value to that years fin statement
                    years_statement[key] = value
    
    return statement

def get_max_pages(years_of_data):
    # max_pages = input("How many years of data? ")
    # if years_of_data.isnumeric():
    max_pages = (years_of_data)

    if max_pages % 5 != 0:
        max_pages //= 5
        max_pages += 1
    else:
        max_pages //= 5

    return max_pages
    # else:
    #     print("Invalid Input")
    #     return 0
    
def adjustment_statement(statement: dict, statement_type: str):
    yearly_data = statement["Yearly Data"]
    
    for year, years_statement in enumerate(yearly_data):
        # Income Statement
        if statement_type == "income-statement":
            
            # Add Weighted Basic/Diluted Average Shares Outstanding
            try:
                # Save values to variables and ensure the keys exist with erroor handling
                basic_shares = years_statement["EPS Basic Total Ops"]
                diluted_shares = years_statement["EPS Diluted Total Ops"]
                net_income = years_statement["Net Income"]
            except KeyError:
                pass
            else:
                # Calculate shares outstanding, refer to README for more info
                if basic_shares != None and net_income != None:
                    try: 
                        net_income = convert("to_float", net_income)
                        basic_shares = net_income / convert("to_float", basic_shares)
                        # Add values to dict with rounding, converting to int, formatting with commas and converting to strings
                        years_statement["Weighted Average Basic Shares Outstanding"] = convert("to_str", basic_shares)
                    except (ZeroDivisionError, AttributeError, ValueError) as error:
                        years_statement["Weighted Average Basic Shares Outstanding"] = None
                if diluted_shares != None and net_income != None:
                    try:
                        diluted_shares = net_income / convert("to_float", diluted_shares)
                        years_statement["Weighted Average Diluted Shares Outstanding"] = convert("to_str", diluted_shares)
                        pass
                    except (ZeroDivisionError, AttributeError, ValueError) as error:
                        years_statement["Weighted Average Diluted Shares Outstanding"] = None
        
        # Cash Flow Statement
        if statement_type == "cash-flow":
            pass
        
        # Balance Sheet
        if statement_type == "balance-sheet":
            # Change key name of TOTAL to Total Current Assets
            years_statement["Total Current Assets"] = years_statement.pop("TOTAL")
            # Calculate NCA
            years_statement["Total Non-Current Assets"] = calculate_keys(years_statement, first_key="Non-Current Assets", total_key="Total Non-Current Assets")
            # Calculate CL
            years_statement["Total Current Liabilities"] = calculate_keys(years_statement, first_key="Current Liabilities", total_key="Total Current Liabilities")
            # Calculate NCL
            years_statement["Total Non-Current Liabilities"] = calculate_keys(years_statement, first_key="Non-Current Liabilities", total_key="Total Non-Current Liabilities")
            # Calculate Equity
            years_statement["Total Shareholders' Equity"] = calculate_keys(years_statement, first_key="Shareholders' Equity", total_key="Total Shareholders' Equity")
        
        statement["Yearly Data"][year] = years_statement
    
    return statement

# Convert statement values to a float to perform calculations on and back to string for visual purposes
def convert(direction: str, num, calculate: bool = False):
    if num == None:
        if calculate == False:
            return None
        else:
            return 0
    elif direction == "to_float":
        num = num.replace("$", "").replace(",", "")
        return float(num)
    elif direction == "to_str":
        num = (int(round(num, -3)))
        return str(format(num, ",d"))
    else:
        return num
    
def calculate_keys(years_statement: dict, first_key: str, total_key: str):
    total = 0
    can_count = False
    for num, key in enumerate(years_statement):
        # print(key, years_statement[key], sep=": ")
        if key == total_key:
            can_count = False
            return convert("to_str", total)
        if can_count:
            add_to_total = convert("to_float", years_statement[key], calculate=True)
            if add_to_total == None:
                total = None
            else:
                total += add_to_total
        if key == first_key:
            can_count = True