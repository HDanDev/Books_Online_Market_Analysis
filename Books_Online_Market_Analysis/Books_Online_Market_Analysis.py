
import csv
from http.client import responses
from requests_html import HTMLSession

class ScrappedProduct:
    def __init__(self, 
                 url=None, 
                 upc=None, 
                 title=None, 
                 price_incl_tax=None, 
                 price_excl_tax=None, 
                 number_available=None, 
                 description=None, 
                 category=None, 
                 rating=None, 
                 image_url=None): 

        self.__product_page_url = url
        self.__universal_product_code = upc
        self.__title = title
        self.__price_including_tax = price_incl_tax
        self.__price_excluding_tax = price_excl_tax
        self.__number_available = number_available
        self.__product_description = description
        self.__category = category
        self.__review_rating = rating
        self.__image_url = image_url

    @property
    def product_page_url(self):
        return self.__product_page_url

    @property
    def universal_product_code(self):
        return self.__universal_product_code

    @property
    def title(self):
        return self.__title

    @property
    def price_including_tax(self):
        return self.__price_including_tax

    @property
    def price_excluding_tax(self):
        return self.__price_excluding_tax

    @property
    def number_available(self):
        return self.__number_available

    @property
    def product_description(self):
        return self.__product_description

    @property
    def category(self):
        return self.__category

    @property
    def review_rating(self):
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value):
        self.__review_rating = f"{value} stars"

    @property
    def image_url(self):
        return self.__image_url

session = HTMLSession()
url = 'http://books.toscrape.com/index.html'
response = session.get(url)

url = "http://books.toscrape.com/" + response.html.find('ul.nav.nav-list > li > ul > li > a', first = True).attrs['href']
response = session.get(url)

listToScrap = response.html.find('ol.row', first = True).find('div.image_container > a')

categoryProductList = []

for element in listToScrap : 
    href = element.attrs['href'].replace("../", "")
    url = "http://books.toscrape.com/catalogue/" + href
    response = session.get(url)
    listCategory = response.html.find('ul.breadcrumb', first=True).find('li > a')[2].text or "null"
    filename = listCategory + ".csv"

    scrappedProduct = ScrappedProduct(
        url, # url
        response.html.find('table > tr > td', first=True).text or "null", # upc
        response.html.find('div.col-sm-6.product_main > h1', first=True).text or "null", # title
        response.html.find('table', first=True).find('tr > td')[3].text or "null", # price TVAI
        response.html.find('table', first=True).find('tr > td')[2].text or "null", # price TVAE
        response.html.search('In stock ({} available)')[0] or "null", # number_available
        response.html.find('article.product_page > p', first=True).text or "null", # description
        listCategory, # category
        response.html.search('"star-rating {}"')[0] or "null", # rating
        response.html.find('[src]', first=True).attrs['src'] or "null", # image_url
    )
    categoryProductList.append(scrappedProduct)
   
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for product in categoryProductList:
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
