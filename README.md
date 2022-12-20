# Finance API
> Name: Ari Gestetner  
App Type: API/Add-on  
Category: Finance



<!-- 
## Table of Contents
- [Finance API](#finance-api)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
    - [Motivation](#motivation)
      - [Why Did I Create This Application?](#why-did-i-create-this-application)
      - [What Did I Have to Solve?](#what-did-i-have-to-solve)
      - [What Did I Learn?](#what-did-i-learn)
      - [How Does My Project Stand Out?](#how-does-my-project-stand-out)
      - [Main Features\*](#main-features)
    - [Technologies](#technologies)
      - [Languages](#languages)
      - [Framework](#framework)
      - [Deployment](#deployment)
  - [How to Install and Run the Project (Using make)](#how-to-install-and-run-the-project-using-make)
    - [How to Setup the App](#how-to-setup-the-app)
    - [How to Run the App](#how-to-run-the-app)
    - [How to Use the App](#how-to-use-the-app)
    - [Tests](#tests)
    - [Credits](#credits)
    - [License](#license)

## Description
Finance-API was built to provide easy access to financial data directly to your investment spreadsheet. It can provide the client with past performance in the form of financial statements. Furthermore, it is also able to provide the user with currently listed options and market data about the stock, like market value or KPI's like the p/e ratio.

### Motivation
#### Why Did I Create Did I Create This Application?
I initially prototyped this app as I was fed up with having to copy and paste financial statements into a spreadsheet for further automated valuation and analysis. I later consulted a friend asking what they thought of the concept, and they encouraged me to further build it up for easier use.  

#### What is This Application?
I initially prototyped this app as I was fed up with having to copy and paste financial statements into a spreadsheet for further automated valuation and analysis. I later consulted a friend asking what they thought of the concept, and they encouraged me to further build it up for easier use.  

#### What Did I Have to Solve?
Programming this API involved many challenges and problems which required a variety of solutions.  

One such issue arose at the beginning when I had to find a website to scrape that contained the data I wanted. 
At first, I had a look at Quickfs.com. The issue I quickly came across was that to view historical statements on their website, the user is required to use a sign-in. Due to considering scalability, I didn't want to have to use cookies linked to my name. Therefore, I determined I didn't want to use their website.

Next, I looked at using Yahoo Finance, where I built my first prototype. However, their statements are limited to 5 years of data whereas, just by signing in to Quickfs you can copy and paste 20 years of data for free. I was looking for at least 10 years of data.

Then I came across Barchart.com. They had allowed users to access financial statements for more than just US-listed businesses, with data ranging as far back as when the company first published a public filing. The main issue I found was that the data was only listed 5 years at a time, which would require multiple pages to be called, which is called synchronously, and would take at least 2 seconds per page, possibly taking over 30 seconds for 10 pages.

Thus, I was led to explore _multithreading_. Using threads I was able to place HTTP requests on a new thread to allow for non-blocking code, reducing the request times to approx. 2 seconds - the time taken for a one-page request.

To access the options API used on the Barchart website, I found that to make the call, cookies were required. However, these cookies expired meaning I couldn't keep them.

However, I quickly realised that if I made a page request to a Barchart page, the return headers would contain all the necessary content. After tinkering with the cookies by matching them up with cookies that worked and seeing which digits and letters should be added or removed, I found a way to access their API.
?
Programming this API involved many challenges and problems which required a variety of solutions.  

One such issue arose at the beginning when I had to find a website to scrape that contained the data I wanted. 
At first, I had a look at Quickfs.com. The issue I quickly came across was that to view historical statements on their website, the user is required to use a sign-in. Due to considering scalability, I didn't want to have to use cookies linked to my name. Therefore, I determined I didn't want to use their website.

Next, I looked at using Yahoo Finance, where I built my first prototype. However, their statements are limited to 5 years of data whereas, just by signing in to Quickfs you can copy and paste 20 years of data for free. I was looking for at least 10 years of data.

Then I came across Barchart.com. They had allowed users to access financial statements for more than just US-listed businesses, with data ranging as far back as when the company first published a public filing. The main issue I found was that the data was only listed 5 years at a time, which would require multiple pages to be called, which is called synchronously, and would take at least 2 seconds per page, possibly taking over 30 seconds for 10 pages.

Thus, I was led to explore _multithreading_. Using threads I was able to place HTTP requests on a new thread to allow for non-blocking code, reducing the request times to approx. 2 seconds - the time taken for a one-page request.

To access the options API used on the Barchart website, I found that to make the call, cookies were required. However, these cookies expired meaning I couldn't keep them.

However, I quickly realised that if I made a page request to a Barchart page, the return headers would contain all the necessary content. After tinkering with the cookies by matching them up with cookies that worked and seeing which digits and letters should be added or removed, I found a way to access their API.

#### What Did I Learn?
Throughout building this app, I learned many new programming concepts.
- OOP
- BeautifulSoup
- multi-threading
- Pytest/unit testing
- Fast-API
- REST API's
- modules and file management?
Throughout building this app, I learned many new programming concepts.
- OOP
- BeautifulSoup
- multi-threading
- Pytest/unit testing
- Fast-API
- REST API's
- modules and file management
#### How Does My Project Stand Out?
Whilst I had found some similar concepts available online, they all were too expensive for sustainable use. So my second option was to build my own.
Not only that but, it can also be customised to how I want it (i.e. adding sections to a statement on the backend, so I don't have to perform the calculations in a spreadsheet).?
Whilst I had found some similar concepts available online, they all were too expensive for sustainable use. So my second option was to build my own.
Not only that but, it can also be customised to how I want it (i.e. adding sections to a statement on the backend, so I don't have to perform the calculations in a spreadsheet).
#### Main Features*
This API is divided into three main features.
These are 
- 

### Technologies  
This API/Add-on
#### Languages
#### Framework
#### Deployment

## How to Install and Run the Project (Using make)
This application utilises a Makefile in order to easily set up and run.

### How to Setup the App
Being that this program uses a Makefile all it takes to run is...
```Bash
make
```
This command will create a virtual environment then install all packages from the requirements.txt

To activate the virtual environment, enter...
```Bash
source Finance_API3.9/bin/activate
```
To deactivate...
```Bash
deactivate
```
After running the app, python will create binaries to cache for quicker runtime. If you want to delete the virtual environment and remove those binaries, you can enter in the CLI...
```Bash
make clean
```
### How to Run the App
To run the app, all you have to do is enter...
```Bash
make run
```
If you would like to host using Vercel, you can use...
```Bash
make upload
```
And to upload to production...
```Bash
make prod
```

### How to Use the App
Fast API generates automated docs, these can be found at `\docs`. Alternatively, you can use `\redoc` for a different style 

### Tests
Being that building robust applications is my highest priority, I have implemented unit testing using Pytest. 
To run these tests use...
```Bash
make test
```

### Credits*
The general format for this markdown README was inspired by [FreeCodeCamp](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/).

### License 
© 2020 Ari Gestetner <ariges770@gmail.com>
