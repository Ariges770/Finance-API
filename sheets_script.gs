function retrieveInfo(ticker, years_of_data, statement_type) {
    var response = UrlFetchApp.fetch(`http://finance-api.gestetnerari.com/financials/${statement_type}/?years_of_data=${years_of_data}&ticker=${ticker}`);
    var object   = JSON.parse(response.getContentText());
    return object
  }
  
  function statement(ticker, years_of_data, statement_type) {
    statements = retrieveInfo(ticker, years_of_data, statement_type)
    const res_array = []; 
    for(let i in statements["Yearly_Data"][0]) { 
      res_array.push(i);
    }
  
    const verticalArray = [];
    const horizontalArray = [];
    verticalArray.push([]);
    for(let title in statements["Yearly_Data"][0]) {
      horizontalArray.push(title);
      for (let year in statements["Yearly_Data"]) {
        horizontalArray.push(statements["Yearly_Data"][year][title]);
        // console.log(`${title}: ${statements["Yearly_Data"][year][title]}`)
      }
      let temp = [...horizontalArray]
      verticalArray.push(temp);
      horizontalArray.length = 0;
    }
    // console.log(verticalArray);
    return verticalArray
  }
  
  function BS(ticker, years_of_data){
    return statement(ticker, years_of_data, "bs")
  }
  
  function IS(ticker, years_of_data){
    return statement(ticker, years_of_data, "is")
  }
  
  function CFS(ticker, years_of_data){
    return statement(ticker, years_of_data, "cfs")
  }