class ScrapedProduct:
    def __init__(self):
        self.__productUrl = "n/a"
        self.__productCode = "n/a"
        self.__title = "n/a"
        self.__productPriceTaxIncluded = "n/a"
        self.__productPriceTaxExcluded = "n/a"
        self.__productNbr = "n/a"
        self.__productDescription = "n/a"
        self.__category = "n/a"
        self.__productRating = "n/a"
        self.__productImgUrl = "n/a"

    @property
    def productUrl(self):
        return self.__productUrl

    @productUrl.setter
    def productUrl(self, value):
        self.__productUrl = value

    @property
    def productCode(self):
        return self.__productCode

    @productCode.setter
    def productCode(self, value):
        self.__productCode = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def productPriceTaxIncluded(self):
        return self.__productPriceTaxIncluded

    @productPriceTaxIncluded.setter
    def productPriceTaxIncluded(self, value):
        self.__productPriceTaxIncluded = value

    @property
    def productPriceTaxExcluded(self):
        return self.__productPriceTaxExcluded

    @productPriceTaxExcluded.setter
    def productPriceTaxExcluded(self, value):
        self.__productPriceTaxExcluded = value

    @property
    def productNbr(self):
        return self.__productNbr

    @productNbr.setter
    def productNbr(self, value):
        self.__productNbr = value

    @property
    def productDescription(self):
        return self.__productDescription

    @productDescription.setter
    def productDescription(self, value):
        self.__productDescription = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value

    @property
    def productRating(self):
        return self.__productRating

    @productRating.setter
    def productRating(self, value):
        self.__productRating = value + " stars" if value else "n/a"

    @property
    def productImgUrl(self):
        return self.__productImgUrl

    @productImgUrl.setter
    def productImgUrl(self, value):
        self.__productImgUrl = value