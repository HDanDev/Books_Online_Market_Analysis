class ScrapedProduct:
    def __init__(self):  
        pass

@property
def product_page_url(self):
    return self.__productUrl

@product_page_url.setter
def product_page_url(self, value):
    self.__productUrl = value

@property
def universal_product_code(self):
    return self.__productCode

@universal_product_code.setter
def universal_product_code(self, value):
    self.__productCode = value

@property
def title(self):
    return self.__title

@title.setter
def title(self, value):
    self.__title = value

@property
def price_including_tax(self):
    return self.__productPriceTaxIncluded

@price_including_tax.setter
def price_including_tax(self, value):
    self.__productPriceTaxIncluded = value

@property
def price_excluding_tax(self):
    return self.__productPriceTaxExcluded

@price_excluding_tax.setter
def price_excluding_tax(self, value):
    self.__productPriceTaxExcluded = value

@property
def number_available(self):
    return self.__productNbr

@number_available.setter
def number_available(self, value):
    self.__productNbr = value

@property
def product_description(self):
    return self.__productDescription

@product_description.setter
def product_description(self, value):
    self.__productDescription = value

@property
def category(self):
    return self.__category

@category.setter
def category(self, value):
    self.__category = value

@property
def review_rating(self):
    return self.__productRating

@review_rating.setter
def review_rating(self, value):
    self.__productRating = value + " stars" if value else "null"

@property
def image_url(self):
    return self.__productImgUrl

@image_url.setter
def image_url(self, value):
    self.__productImgUrl = value

