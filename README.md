# E-Commerce-Project :exclamation:

# What is Web-Scraping :grey_question:

[Web scraping](https://en.wikipedia.org/wiki/Web_scraping), web harvesting, or web data extraction is data scraping used for extracting data from websites. It is a form of copying in which specific data is gathered and copied from the web, typically into a central local database or spreadsheet, for later retrieval or analysis.

For the current project we were contacted by an International company willing to open a new E-commerce business in European Union and with no background with this type of business.
The customer focus was on Electronic products, mainly Laptops, Headphones, Processors, Mouses, Cameras, Monitors and many more.
No data was provided by the client.
Our team had to first focus on knowing the domain in details, understand the business model and then look for appropriate data sources to come up with conlusions and strategies to determine strenghts and weaknesses of this form of business.

<p align="center">
  <img width="400" height="300" src="https://camo.githubusercontent.com/0c179ade1bb1b3ef10763c72b21a25c9100a6e943e5cacf15bdd9df3c6b1789d/68747470733a2f2f692e696d6775722e636f6d2f694753624d6c392e706e67">
</p>

# Understanding Data :exploding_head:

## Web Scraping

One of best way to know your competitor is to look at what they show publicly on their websites. There are so much informations like product details, prices, customer reviews, product seller information etc. which can help understand the competitor's business in a great extent.
To gather data from websites, we used a technique called Web scraping which is basically a technique of extracting relevant information from websites.

<p align="center">
  <img width="700" height="200" src="https://static.javatpoint.com/python/images/web-scraping-using-python.png">
</p>

## Scraping Flow

The following process has been repeated 8 times for 8 different Product types: Processors, Laptops, Cameras, Mouses, Monitors, Headphones, Smartphones, Keyboards.

The first step is to create a txt file (Create search_urls.txt) which will contain all the Urls of the products. Through a for loop I will be able to scrape the website and get all the first 400 Urls (limit declared in the range). The output of this action is to be find in the search_urls.txt
Once all the Urls have been scraped it is time to extract the information about the articles.

Next a yml file is created (search.yml).
This type of language is used for configuration files and in applications where data is being stored or transmitted. In my case it will contain all the element paths from where the informations would be extracted and my goal is to get the components of the articles I am interested in.
I will be looking for multiple information like title, the Url, the rating given from the consumers, the review count and the price of each article.

The search_urls.txt and the search.yml will be then used by the search.py as inputs and will produce as output the search_output.jsonl, a long list of articles with all the components information nested in a json file, and the product_urls.txt containing all urls of the single products for further scraping.

The search.py uses different packages, libraries and file format like:
Selectorlib (a Python package for extracting data from a HTML Page) which will read the yml file and extract the data I marked up on the page.

Requests a Python library used to easily make HTTP requests and getting raw HTML content from websites.

Json (JavaScript Object Notation) is an open standard data format, used for storing and exchanging data.

fake_useragent a library from which we will import UserAgent.

- As the article components where not enough for my scope, more information about every article needed to be extracted therefore a products.yml was created to select informations from teh product pages. By looking in the CSS elements of several products I was able to understand where all information where hidden in the text and extract them. For this purpose I installed a chrome extension to use the [selector gadget](https://selectorgadget.com/). 

- Next I created the product.py which used the product_urls.txt and products.yml as inputs and gave me as output the product_output.jsonl

- Finally the json files where validated with [jsonlint](https://jsonlint.com/) and after exporting them to my Visual studio code notebook were ready for the long cleaning process until creatin of 2 csv files ready for further analysis through Mysql.

# Data Cleaning

The [search files](https://github.com/Jyotika-Kalra/E-Commerce-Project/blob/master/Smartphones/DataCleaning.ipynb) were quite easy to clean, they required mainly extracting data from strings, deleting some additional text and changing Data type to the appropriate one.
Extracting the Asin from the Urls required some additional work "cutting" the Urls into pieces and keeping just the value of interest.

The [product files](https://github.com/Jyotika-Kalra/E-Commerce-Project/blob/master/Smartphones/DataCleaning.ipynb) instead required a way longer and more complicated journey: when scraping I retrieved all possible data that on the Amazon website appeared to be stored in different tables.

To open search and product .ipynb please consider using [nbviewer](https://nbviewer.jupyter.org/) and paste the github url in the bar.

When importing this data in my Visual Studio Code notebook I realized how nested it was (Dictionary in dictionary) with several values of interest being stored in the same cells of the df.

Please follow step by step the notebook to see all required steps until data was finally cleaned for my purpose.

This process has been repeated 8 times for 8 different Product types: Processors, Laptops, Cameras, Mouses, Monitors, Headphones, Smartphones, Keyboards. I will here link just the final csv of cleaned data.

# Mysql
The cleaned data has been subsequently pushed to Mysql for further analysis.

To achieve this result I used PyMySQL (here all instructions to install it), an interface for connecting to a MySQL database server from Python. It implements the Python Database API v2. 0 and contains a pure-Python MySQL client library. Other availabale options are MySQL/connector for Python or MySQLdb.

More details about how to create the data source, creating the engine and the connection to Mysql are povided in the Python notebook.

# Please note:

I have only shown 'SmartPhones' scraping in my Git hub and other products can be scarped and then cleaned in similar way like smartphones.

# Legal Terms
All data has been used only for educational purpose.

<p align="center">
  <img width="600" height="150" src="https://t4.ftcdn.net/jpg/03/49/52/85/360_F_349528536_95ktby9in4wxODsUJjsQGtk4t324h3Qh.jpg">
</p>
