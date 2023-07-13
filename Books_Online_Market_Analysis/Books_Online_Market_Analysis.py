
import csv
import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

data = []

paragraphs = soup.find_all('h1')
for paragraph in paragraphs:
    data.append(paragraph.get_text())

    column_titles = ['Title']
    filename = 'scrapeddata.csv'
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(column_titles)
    for item in data:
        writer.writerow([item])

