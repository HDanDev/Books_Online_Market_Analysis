
import csv
from http.client import responses
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
scrappedProduct['universal_ product_code (upc)'] = response.html.find('table > tr > td' , first = True).text
scrappedProduct['title'] = response.html.find('div.col-sm-6.product_main > h1', first = True).text
scrappedProduct['price_including_tax'] = response.html.find('table' , first = True).find('tr > td')[3].text
scrappedProduct['price_excluding_tax'] = response.html.find('table' , first = True).find('tr > td')[2].text
scrappedProduct['number_available'] = response.html.search('In stock ({} available)')[0]
scrappedProduct['product_description'] = response.html.find('article.product_page > p', first = True).text
scrappedProduct['category'] = response.html.find('ul.breadcrumb' , first = True).find('li > a')[2].text
scrappedProduct['review_rating'] = response.html.search('"star-rating {}"')[0]
scrappedProduct['image_url'] = response.html.find('[src]', first = True).attrs['src']
#print(response.text)
   
with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, scrappedProduct.keys())
    writer.writeheader()
    writer.writerow(scrappedProduct)
