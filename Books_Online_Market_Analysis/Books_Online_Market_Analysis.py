from requests_html import HTMLSession
from ScrapedProductClass import ScrapedProduct
from writers import *
from functions import *
import time

def pageScraping(arrayToAppend, imgArray, targetList, category, isPrintable): 
    if isPrintable :
        print(f'Now scraping the "{category}" category')

    for element in targetList : 
        url = element.absolute_links.pop()
        response = session.get(url)
        
        scrapedProduct = ScrapedProduct()

        # URL
        try:
            scrapedProduct.productUrl = url
        except Exception as e:
            scrapedProduct.productUrl = "null"
            print(f"Error setting URL: {e} at " + scrapedProduct.title + " in " + category)
        
        # UPC
        try:
            scrapedProduct.productCode = response.html.find('table > tr > td', first=True).text
        except Exception as e:
            scrapedProduct.productCode = "null"
            print(f"Error setting UPC: {e} at " + scrapedProduct.title + " in " + category)
        
        # Title
        try:
            scrapedProduct.title = response.html.find('div.col-sm-6.product_main > h1', first=True).text
        except Exception as e:
            scrapedProduct.title = "null"
            print(f"Error setting title: {e} at " + scrapedProduct.title + " in " + category)
        
        # Price Including Tax
        try:
            scrapedProduct.productPriceTaxIncluded = response.html.find('table', first=True).find('tr > td')[3].text
        except Exception as e:
            scrapedProduct.productPriceTaxIncluded = "null"
            print(f"Error setting price tax included: {e} at " + scrapedProduct.title + " in " + category)
        
        # Price Excluding Tax
        try:
            scrapedProduct.productPriceTaxExcluded = response.html.find('table', first=True).find('tr > td')[2].text
        except Exception as e:
            scrapedProduct.productPriceTaxExcluded = "null"
            print(f"Error setting product price tax excluded: {e} at " + scrapedProduct.title + " in " + category)
        
        # Number Available
        try:
            scrapedProduct.productNbr = response.html.search('In stock ({} available)')[0]
        except Exception as e:
            scrapedProduct.productNbr = "null"
            print(f"Error setting product number: {e} at " + scrapedProduct.title + " in " + category)
        
        # Description
        try:
            scrapedProduct.productDescription = response.html.find('article.product_page > p', first=True).text
        except Exception as e:
            scrapedProduct.productDescription = "null"
            print(f"Error setting description: {e} at " + scrapedProduct.title + " in " + category)
        
        # Category
        scrapedProduct.category = category
        
        # Rating
        try:
            scrapedProduct.productRating = response.html.search('"star-rating {}"')[0]
        except Exception as e:
            scrapedProduct.productRating = "null"
            print(f"Error setting rating: {e} at " + scrapedProduct.title + " in " + category)
        
        # Image URL
        try:
            scrapedProduct.productImgUrl = "https://books.toscrape.com/" + (response.html.find('[src]', first=True).attrs['src']).lstrip("../")
            imgArray.append(scrapedProduct.productImgUrl + "_*delimiter*_" + safeFilename(scrapedProduct.title))

        except Exception as e:
            scrapedProduct.productImgUrl = "null"
            print(f"Error setting image url: {e} at " + scrapedProduct.title + " in " + category)

        arrayToAppend.append(scrapedProduct)


def categoryScraping(r, category, categoryUrl): 
    categoryProductList = []
    imgList = []    
    listToScrap = r.html.find('ol.row', first = True).find('div.image_container > a')
    filename = category

    pageScraping(categoryProductList, imgList, listToScrap, category, True)    

    response = session.get(categoryUrl)
    paginationCheck = response.html.find('li.current', first=True)
    if paginationCheck: 
        for _ in range(int(paginationCheck.text.split()[-1])-1):
            r = session.get(response.html.find('li.next > a', first=True).absolute_links.pop())
            listToScrap = r.html.find('ol.row', first=True).find('div.image_container > a')
            pageScraping(categoryProductList, imgList, listToScrap, category, False)

    writeToCsv(filename, categoryProductList)
    writeImg(filename, imgList)

session = HTMLSession()
url = 'http://books.toscrape.com/index.html'
response = session.get(url)

startTimer = time.time()

categoryList = response.html.find('ul.nav.nav-list > li > ul > li > a')
for category in categoryList : 
    categoryName = category.text
    categoryUrl = category.absolute_links.pop()
    response = session.get(categoryUrl)
    categoryScraping(response, categoryName, categoryUrl)

endTimer = time.time()
timerResult = endTimer - startTimer

print(f"Scraping successfully completed in {int(timerResult // 60)}:{int(timerResult %60)} minutes")
