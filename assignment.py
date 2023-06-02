from bs4 import BeautifulSoup
import requests
import csv
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

source = requests.get('https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar', headers=headers).text
soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

links = []
Names = []
Prices = []
Rating = []
Seller = []

# for loop to find all the Product Links for Seller name
for i in soup.find_all('a',attrs={'class' : 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}):
    # print(i["href"])
    links.append("https://www.amazon.in/" + i["href"])

# for loop to find all the Product Name form the page storing into Names list
for i in soup.find_all('span', class_='a-size-base-plus a-color-base a-text-normal'):
    string = i.text
    Names.append(string.strip())

# for loop to find all the Product Price form the page and storing into Prices list
for i in soup.find_all('span', class_='a-price-whole'):
    Prices.append(i.text)

# for loop to find all the Product Rating from the page and storing into Rating list
for i in soup.find_all('span', class_='a-icon-alt'):
    Rating.append(i.text)

# for loop to find all the Seller name for each product in the stored links
for j in range(len(links)):
    a = True
    # While loop to try unlit we get the Seller Name
    while a:
        try:
            time.sleep(10)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

            source = requests.get(links[j],headers=headers).text
            soup = BeautifulSoup(source, 'lxml')

            # finding seller name and storing into seller list
            i = soup.find("div", attrs={"id": 'merchant-info'})
            yString = i.text
            Seller.append(yString)
            # print(yString)
            a = False

        # exception when scraping is blocked via amazon for seller name
        except AttributeError:
            pass

# creating a csv
file_name = 'Products.csv'

# writing Column names in csv
with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Sr.No', 'Name', 'Prices', 'Rating', 'Seller'])

    # writing the content of all the stored list into csv
    for i in range(len(Names)):
        writer.writerow([i+1, Names[i], Prices[i], Rating[i], Seller[i]])
