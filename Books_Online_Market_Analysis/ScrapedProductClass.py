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

