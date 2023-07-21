from requests_html import HTMLSession
import requests
import csv
import os

class ScrapedProduct:
    def __init__(self):  
        pass

@property
def product_page_url(self):
    return self.__product_page_url

@product_page_url.setter
def product_page_url(self, value):
    self.__product_page_url = value

@property
def universal_product_code(self):
    return self.__universal_product_code

@universal_product_code.setter
def universal_product_code(self, value):
    self.__universal_product_code = value

@property
def title(self):
    return self.__title

@title.setter
def title(self, value):
    self.__title = value

@property
def price_including_tax(self):
    return self.__price_including_tax

@price_including_tax.setter
def price_including_tax(self, value):
    self.__price_including_tax = value

@property
def price_excluding_tax(self):
    return self.__price_excluding_tax

@price_excluding_tax.setter
def price_excluding_tax(self, value):
    self.__price_excluding_tax = value

@property
def number_available(self):
    return self.__number_available

@number_available.setter
def number_available(self, value):
    self.__number_available = value

@property
def product_description(self):
    return self.__product_description

@product_description.setter
def product_description(self, value):
    self.__product_description = value

@property
def category(self):
    return self.__category

@category.setter
def category(self, value):
    self.__category = value

@property
def review_rating(self):
    return self.__review_rating

@review_rating.setter
def review_rating(self, value):
    self.__review_rating = value + " stars" if value else "null"

@property
def image_url(self):
    return self.__image_url

@image_url.setter
def image_url(self, value):
    self.__image_url = value


def writeToCsv(fileName, listToWrite): 
    folder = "scraped_files/" + fileName + "/CSV file"
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, fileName + ".csv")

    with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax', 
                      'price_excluding_tax', 'number_available', 'product_description', 'category', 
                      'review_rating', 'image_url']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    
        for product in listToWrite:
            writer.writerow({
                'product_page_url': product.product_page_url or "null",
                'universal_product_code (upc)': product.universal_product_code or "null",
                'title': product.title or "null",
                'price_including_tax': product.price_including_tax or "null",
                'price_excluding_tax': product.price_excluding_tax or "null",
                'number_available': product.number_available or "null",
                'product_description': product.product_description or "null",
                'category': product.category or "null",
                'review_rating': product.review_rating or "null",
                'image_url': product.image_url or "null"
            })

def writeImg(category, image_urls):
    folder = "scraped_files/" + category + "/img"
    if not os.path.exists(folder):
        os.makedirs(folder)

    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url)
            response.raise_for_status()
            image_filename = os.path.join(folder, f"image_{i}.jpg")
            with open(image_filename, "wb") as f:
                f.write(response.content)
            print(f"Image {i + 1} downloaded and saved as {image_filename}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading image {i + 1}: {e}")

def pageScraping(arrayToAppend, imgArray, targetList, category): 
    for element in targetList : 
        url = element.absolute_links.pop()
        response = session.get(url)
        
        scrapedProduct = ScrapedProduct()

        # URL
        try:
            scrapedProduct.product_page_url = url
        except Exception as e:
            scrapedProduct.product_page_url = "null"
            print(f"Error setting URL: {e} at " + scrapedProduct.title + " in " + category)
        
        # UPC
        try:
            scrapedProduct.universal_product_code = response.html.find('table > tr > td', first=True).text
        except Exception as e:
            scrapedProduct.universal_product_code = "null"
            print(f"Error setting UPC: {e} at " + scrapedProduct.title + " in " + category)
        
        # Title
        try:
            scrapedProduct.title = response.html.find('div.col-sm-6.product_main > h1', first=True).text
        except Exception as e:
            scrapedProduct.title = "null"
            print(f"Error setting title: {e} at " + scrapedProduct.title + " in " + category)
        
        # Price Including Tax
        try:
            scrapedProduct.price_including_tax = response.html.find('table', first=True).find('tr > td')[3].text
        except Exception as e:
            scrapedProduct.price_including_tax = "null"
            print(f"Error setting price_including_tax: {e} at " + scrapedProduct.title + " in " + category)
        
        # Price Excluding Tax
        try:
            scrapedProduct.price_excluding_tax = response.html.find('table', first=True).find('tr > td')[2].text
        except Exception as e:
            scrapedProduct.price_excluding_tax = "null"
            print(f"Error setting price_excluding_tax: {e} at " + scrapedProduct.title + " in " + category)
        
        # Number Available
        try:
            scrapedProduct.number_available = response.html.search('In stock ({} available)')[0]
        except Exception as e:
            scrapedProduct.number_available = "null"
            print(f"Error setting number_available: {e} at " + scrapedProduct.title + " in " + category)
        
        # Description
        try:
            scrapedProduct.product_description = response.html.find('article.product_page > p', first=True).text
        except Exception as e:
            scrapedProduct.product_description = "null"
            print(f"Error setting description: {e} at " + scrapedProduct.title + " in " + category)
        
        # Category
        scrapedProduct.category = category
        
        # Rating
        try:
            scrapedProduct.review_rating = response.html.search('"star-rating {}"')[0]
        except Exception as e:
            scrapedProduct.review_rating = "null"
            print(f"Error setting rating: {e} at " + scrapedProduct.title + " in " + category)
        
        # Image URL
        try:
            scrapedProduct.image_url = "https://books.toscrape.com/" + (response.html.find('[src]', first=True).attrs['src']).lstrip("../")
            imgArray.append(scrapedProduct.image_url)

        except Exception as e:
            scrapedProduct.image_url = "null"
            print(f"Error setting image_url: {e} at " + scrapedProduct.title + " in " + category)

        arrayToAppend.append(scrapedProduct)


def categoryScraping(r, category, categoryUrl): 
    categoryProductList = []
    imgList = []    
    listToScrap = r.html.find('ol.row', first = True).find('div.image_container > a')
    filename = category

    pageScraping(categoryProductList, imgList, listToScrap, category)    

    response = session.get(categoryUrl)
    paginationCheck = response.html.find('li.current', first=True)
    if paginationCheck: 
        for _ in range(int(paginationCheck.text.split()[-1])-1):
            r = session.get(response.html.find('li.next > a', first=True).absolute_links.pop())
            listToScrap = r.html.find('ol.row', first=True).find('div.image_container > a')
            pageScraping(categoryProductList, imgList, listToScrap, category)

    writeToCsv(filename, categoryProductList)
    writeImg(filename, imgList)

session = HTMLSession()
url = 'http://books.toscrape.com/index.html'
response = session.get(url)

categoryList = response.html.find('ul.nav.nav-list > li > ul > li > a')
for category in categoryList : 
    categoryName = category.text
    categoryUrl = category.absolute_links.pop()
    response = session.get(categoryUrl)
    categoryScraping(response, categoryName, categoryUrl)
