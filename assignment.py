from bs4 import BeautifulSoup
import requests
import csv

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

source = requests.get('https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar', headers=headers).text
soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())

Names = []
Prices = []
Rating = []
# for loop

for i in soup.find_all('span', class_='a-size-base-plus a-color-base a-text-normal'):
    string = i.text
    Names.append(string.strip())

for i in soup.find_all('span', class_='a-price-whole'):
    Prices.append(i.text)

for i in soup.find_all('span', class_='a-icon-alt'):
    Rating.append(i.text)

file_name = 'Products.csv'

with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Sr.No', 'Name', 'Prices', 'Rating', 'Seller'])

    for i in range(len(Names)):
        writer.writerow([i+1, Names[i], Prices[i], Rating[i] , Names[i].split(' ', 1)[0]])
