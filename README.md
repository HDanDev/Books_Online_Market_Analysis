--------------------
Web Scraping Project
--------------------

This is a web scraping project that extracts data from a small website, "Books to Scrape." The project utilizes Python and the requests and beautifulsoup4 libraries for web scraping. The scraped data includes information about various books, such as product details, prices, availability, and images.

----------------
Project Overview
----------------

The goal of this project is to demonstrate web scraping techniques using Python. The requests library is used to fetch the HTML content of web pages, and beautifulsoup4 is employed to parse and extract data from the HTML.

The script scrapes data from the "Books to Scrape" website for various book categories and saves the scraped information to CSV files. Additionally, it downloads and saves book cover images to the local filesystem.

---------------
Getting Started
---------------

-- Prerequisites --

Python (version 3.6 or higher)  

Python libraries:  

requests  
beautifulsoup4  

-- Installation --

1. Clone the repository:

```
https://github.com/HDanDev/Books_Online_Market_Analysis.git
```
```
cd Books_Online_Market_Analysis
```

2. Create a Python virtual environement:

```
py -m venv venv
```

3. Activate the virtual environment:

• Windows:
```
venv\Scripts\activate
```

• MacOS and Linux:
```
source venv/bin/activate
```

3. Install the required Python libraries using pip:

```
pip install -r requirements.txt
```

-----
Usage
-----

To run the web scraping script, execute the following command:

    Books_Online_Market_Analysis.py

The script will scrape data for various book categories from the "Books to Scrape" website. The extracted information will be saved as CSV files for each category in the scraped_files directory. Additionally, book cover images will be downloaded and saved in the scraped_files/[category]/img directory.
Project Structure

The project directory structure is as follows:

    web-scraping-project/
      ├── Books_Online_Market_Analysis.py
      ├── functions.py
      ├── README.md
      ├── ScrapedProductClass.py
      ├── writers.py
      └── scraped_files/
          ├── [category name]/
          │   ├── CSV file/
          │   │   └── [category name].csv
          │   └── img/
          │       └── [book name]
          ├── [category name]/
          │   ├── CSV file/
          │   │   └── [category name].csv
          │   └── img/
          │       └── [book name]
          └── [other_categories...]

Books_Online_Market_Analysis.py: The main Python script that initiates the web scraping process.  
functions.py: Contains utility functions.  
ScrapedProductClass.py: Defines the ScrapedProduct class to store scraped data in an organized manner.  
writers.py: Contains the functions for scraping and saving data into CSV and img files.  
README.md: This readme file.  
scraped_files/: Directory to store the scraped data.  
scraped_files/[category]/CSV file/: Directory to store CSV files for each book category.  
scraped_files/[category]/img/: Directory to store downloaded book cover images for each category.  

------------
Contributing
------------

Contributions to this project are welcome. If you find any bugs, have suggestions, or want to add new features, feel free to open an issue or submit a pull request.
