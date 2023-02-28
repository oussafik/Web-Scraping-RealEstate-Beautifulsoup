# Real Estate Web Scraper

This project is a Python web scraper that extracts real estate data from the Realtor.com website for the city of Stockton, California. The data is then saved to either a MySQL database or a CSV file, depending on the file that is run. The project consists of two source code files, ScrapingToDB_TextFile.py and ScrapingToCsvFile.py, which accomplish the same task of scraping and storing the data, but use different methods to store the data.

## Getting Started

To run the web scraper, you will need to have Python 3 installed on your machine. You will also need to install the following Python libraries:

- BeautifulSoup
- requests
- mysql-connector-python (if using the realestate_db.py file)


You can install these libraries by running the following command in your terminal:
 'pip install beautifulsoup4 requests mysql-connector-python'
 
 
 ## How to Use

To use the web scraper, you can simply run one of the two source code files, depending on how you want to store the data.

### ScrapingToDB_TextFile.py

This file will save the scraped data to a MySQL database. Before running the file, you will need to set up a MySQL database and update the Connexion.py file with your database credentials. Once you have done this, you can run the file by navigating to the directory where the file is located and running the following command:
'python ScrapingToDB_TextFile.py'


The program will then scrape the data from the Realtor.com website and save it to the MySQL database and a local text file named 'data.txt'.


### ScrapingToCsvFile.py

This file will save the scraped data to a CSV file. To run the file, navigate to the directory where the file is located and run the following command:
'python ScrapingToCsvFile.py'

The program will then scrape the data from the Realtor.com website and save it to a CSV file named 'housing.csv' in the same directory.


## Data Collected

The web scraper collects the following data for each real estate listing:

- Location
- Status
- Price
- Owner
- Number of Bedrooms
- Number of Bathrooms
- Total Square Footage
- Square Footage of Lot


## Contributing

If you would like to contribute to this project, feel free to submit a pull request with your changes.

## Credits

This project was created by Oussama Fikri. The code is based on examples from the Beautiful Soup documentation and the requests library documentation.
