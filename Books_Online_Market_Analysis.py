from requests_html import HTMLSession
from ScrapedProductClass import ScrapedProduct
from writers import *
from functions import *
import time

def pageScraping(arrayToAppend, imgArray, targetList, category): 
    
    for element in targetList : 
        url = element.absolute_links.pop()
        response = session.get(url)
        
        scrapedProduct = ScrapedProduct()

        # URL
        try:
            scrapedProduct.productUrl = url
        except Exception as e:
            print(f"Error setting URL: {e} at " + scrapedProduct.title + " in " + category)
        
        # UPC
        try:
            scrapedProduct.productCode = response.html.find('table > tr > td', first=True).text
        except Exception as e:
            print(f"Error setting UPC: {e} at " + scrapedProduct.title + " in " + category)
        
        # Title
        try:
            scrapedProduct.title = response.html.find('div.col-sm-6.product_main > h1', first=True).text
        except Exception as e:
            print(f"Error setting title: {e} at " + scrapedProduct.title + " in " + category)
        
        # Price Including Tax
        try:
            scrapedProduct.productPriceTaxIncluded = response.html.find('table', first=True).find('tr > td')[3].text
        except Exception as e:
            print(f"Error setting price tax included: {e} at " + scrapedProduct.title + " in " + category)
        
        # Price Excluding Tax
        try:
            scrapedProduct.productPriceTaxExcluded = response.html.find('table', first=True).find('tr > td')[2].text
        except Exception as e:
            print(f"Error setting product price tax excluded: {e} at " + scrapedProduct.title + " in " + category)
        
        # Number Available
        try:
            scrapedProduct.productNbr = response.html.search('In stock ({} available)')[0]
        except Exception as e:
            print(f"Error setting product number: {e} at " + scrapedProduct.title + " in " + category)
        
        # Description
        try:
            scrapedProduct.productDescription = response.html.find('article.product_page > p', first=True).text
        except Exception as e:
            print(f"Error setting description: {e} at " + scrapedProduct.title + " in " + category)
        
        # Category
        scrapedProduct.category = category
        
        # Rating
        try:
            scrapedProduct.productRating = response.html.search('"star-rating {}"')[0]
        except Exception as e:
            print(f"Error setting rating: {e} at " + scrapedProduct.title + " in " + category)
        
        # Image URL
        try:
            scrapedProduct.productImgUrl = "https://books.toscrape.com/" + (response.html.find('[src]', first=True).attrs['src']).lstrip("../")
            imgArray.append(scrapedProduct.productImgUrl + "_*delimiter*_" + safeFilename(scrapedProduct.title))

        except Exception as e:
            print(f"Error setting image url: {e} at " + scrapedProduct.title + " in " + category)

        arrayToAppend.append(scrapedProduct)


def categoryScraping(r, category, categoryUrl): 
    categoryProductList = []
    imgList = []    
    listToScrap = r.html.find('ol.row', first = True).find('div.image_container > a')
    filename = category

    ### 12:58 ###

    #if(len(listToScrap)<20): 
    #    pageScraping(categoryProductList, imgList, listToScrap, category)

    #else:
    #    response = session.get(categoryUrl)
    #    paginationCheck = response.html.find('li.current', first=True)
    #    pageNumber = 1

    #    if paginationCheck: 
    #        for _ in range(int(paginationCheck.text.split()[-1])):
    #            response = session.get(urlCleaner(categoryUrl, "index.html", f"page-{pageNumber}.html"))
    #            pageScraping(categoryProductList, imgList, listToScrap, category)
    #            pageNumber += 1
        
    ### 13:39 ###

    #pageNumber = 1
    
    #while True:        
    #    response = session.get(urlCleaner(categoryUrl, "index.html", f"page-{pageNumber}.html"))
       
    #    if response.status_code == 200:
    #        pageScraping(categoryProductList, imgList, listToScrap, category)
    #        pageNumber += 1
    #    else:
    #        break

    ### 11:30 ###

    pageScraping(categoryProductList, imgList, listToScrap, category)    

    response = session.get(categoryUrl)
    paginationCheck = response.html.find('li.current', first=True)
    if paginationCheck: 
        for _ in range(int(paginationCheck.text.split()[-1])-1):
            r = session.get(response.html.find('li.next > a', first=True).absolute_links.pop())
            listToScrap = r.html.find('ol.row', first=True).find('div.image_container > a')
            pageScraping(categoryProductList, imgList, listToScrap, category)

    ###

    writeToCsv(filename, categoryProductList)
    writeImg(filename, imgList)

startTimer = time.time()
session = HTMLSession()
URL = 'http://books.toscrape.com/index.html'
response = session.get(URL)

### Starting the scraping process by looping through the categories
categoryList = response.html.find('ul.nav.nav-list > li > ul > li > a')
for category in categoryList : 
    categoryName = category.text
    categoryUrl = category.absolute_links.pop()
    response = session.get(categoryUrl)
    print(f'Now scraping the "{categoryName}" category')
    categoryScraping(response, categoryName, categoryUrl)

endTimer = time.time()
timerResult = endTimer - startTimer

print(f"Scraping successfully completed in {int(timerResult // 60)}:{int(timerResult %60)} minutes")
