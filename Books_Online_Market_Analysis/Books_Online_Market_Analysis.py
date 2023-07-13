
import csv
from requests_html import HTMLSession

session = HTMLSession()
url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = session.get(url)

filename = 'scrappedData.csv'
scrappedProduct = {
    'product_page_url': 'null',
    'universal_ product_code (upc)': 'null',
    'title': 'null',
    'price_including_tax': 'null',
    'price_excluding_tax': 'null',
    'number_available': 'null',
    'product_description': 'null',
    'category': 'null',
    'review_rating': 'null',
    'image_url': 'null',
}

scrappedProduct['product_page_url'] = url
scrappedProduct['title'] = response.html.find('title', first = True)
   
with open(filename, 'w', newline='') as csvfile:
    #print(scrappedProduct.values())
    writer = csv.DictWriter(csvfile, scrappedProduct.keys())
    writer.writeheader()
    writer.writerow(scrappedProduct)
