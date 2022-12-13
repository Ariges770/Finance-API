# Finance API
> Name: Ari Gestetner  
App Type: API/Addon  
Catagory: Finance



<!-- 
## Table of Contents
1. [Description](#description)  
    1. [Motivation](#motivation)
        1. [What Did I Have to Solve](#what-did-i-have-to-solve)
        2. [What Did I Learn](#what-did-i-learn)
        3. [How Does My Project Stand Out](#how-does-my-project-stand-out)
        4. [Main Features](#main-features)
    2. [Technologies](#technologies)
        1. [Languages](#languages)
        2. [Framework](#framework)
        3. [Deployment](#deployment)
2. [How to Install and Run the Project](#how-to-install-and-run-the-project)
    1. [Tests](#tests)
    2. [How to Use the Project](#how-to-use-the-project)
    3. [Credits](#credits)
    4. [License](#license)
     -->
1. [Finance API](#finance-api)
   1. [Description](#description)
      1. [Motivation](#motivation)
         1. [Why Did I Create This Application?](#why-did-i-create-this-application)
         2. [What Did I Have to Solve?](#what-did-i-have-to-solve)
         3. [What Did I Learn?](#what-did-i-learn)
         4. [How Does My Project Stand Out?](#how-does-my-project-stand-out)
         5. [Main Features](#main-features)
      2. [Technologies  \*](#technologies)
         1. [Languages\*](#languages)
         2. [Framework\*](#framework)
         3. [Deployment\*](#deployment)
         4. [Why These Technologies?](#why-these-technologies)
   2. [How to Install and Run the Project\*](#how-to-install-and-run-the-project)
      1. [Tests\*](#tests)
      2. [How to Use the Project\*](#how-to-use-the-project)
      3. [Credits\*](#credits)
      4. [License \*](#license)

## Description
Finance-API was built to provide easy access to financial data directly to your investment spreadsheet. It can provide the client with past performance in the form of financial statements. Furthermore, it is also able to provide the user with currently listed options and market data about the stock, like market value or KPI's like the p/e ratio.

### Motivation
#### Why Did I Create This Application?
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

#### What Did I Learn?
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
Not only that but, it can also be customised to how I want it (i.e. adding sections to a statement on the backend, so I don't have to perform the calculations in a spreadsheet).
#### Main Features
- 

### Technologies  *
This API/Addon
#### Languages*
#### Framework*
#### Deployment*
#### Why These Technologies?

## How to Install and Run the Project*

### Tests*

### How to Use the Project*

### Credits*
The general format for this markdown README was inspired by [FreeCodeCamp](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/).

### License *
