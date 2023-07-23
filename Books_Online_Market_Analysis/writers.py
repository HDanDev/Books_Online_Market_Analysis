import requests
import csv
import os

def writeToCsv(fileName, listToWrite): 
    folder = "scraped_files/" + fileName + "/CSV file"
    if not os.path.exists(folder):
        os.makedirs(folder)

    filePath = os.path.join(folder, fileName + ".csv")

    with open(filePath, 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['product_page_url', 'universal_product_code (upc)', 'title', 'price_including_tax', 
                      'price_excluding_tax', 'number_available', 'product_description', 'category', 
                      'review_rating', 'image_url']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    
        for product in listToWrite:
            writer.writerow({
                'product_page_url': product.productUrl or "null",
                'universal_product_code (upc)': product.productCode or "null",
                'title': product.title or "null",
                'price_including_tax': product.productPriceTaxIncluded or "null",
                'price_excluding_tax': product.productPriceTaxExcluded or "null",
                'number_available': product.productNbr or "null",
                'product_description': product.productDescription or "null",
                'category': product.category or "null",
                'review_rating': product.productRating or "null",
                'image_url': product.productImgUrl or "null"
            })
            
def writeImg(category, imgList):
    folder = "scraped_files/" + category + "/img"
    if not os.path.exists(folder):
        os.makedirs(folder)

    for i, img in enumerate(imgList):
        splitedString = img.split("_*delimiter*_", 1)
        url = splitedString[0]
        imgName = splitedString[1]
        try:
            response = requests.get(url)
            response.raise_for_status()
            imageFilename = os.path.join(folder, f"{imgName}.jpg")
            with open(imageFilename, "wb") as f:
                f.write(response.content)
            print(f"Image {i + 1} downloaded and saved as {imageFilename}")
        except requests.exceptions.RequestException as e:
            print(f'Error downloading image {i + 1} "{imgName}": {e}')