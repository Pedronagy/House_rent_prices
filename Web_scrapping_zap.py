# Import libraries
from os import replace
from bs4 import BeautifulSoup
import requests
import csv
import pandas
import timeit

# Select the source url
url = "https://www.zapimoveis.com.br/aluguel/imoveis/sp+campinas/?pagina="
page = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}

# Create the csv output file with the relevant column names
site_data =  open('site_data_zap.csv', mode='w',newline='\n', encoding='utf-8')
writer = csv.writer(site_data,delimiter='\t')
site_data_names = [
        'rent', 
        'condominium',
        'iptu',
        'adress',
        'area',
        'room',
        'car_space',
        'bathroom',
        'description',
        'link'
    ]
writer.writerow(site_data_names)

# Calculate the total number of pages to be read. There are 24 cards per page
house_results = soup.find('h1', class_='js-summary-title heading-regular heading-regular__bold align-left results__title').text.replace('.','')[:6]
total_pages = int(house_results)//24

start = timeit.default_timer()

# Scrap the data
for page in range(1,total_pages):
    url_page = url + str(page) + "&onde=,S%C3%A3o%20Paulo,Campinas,,,,,,BR%3ESao%20Paulo%3ENULL%3ECampinas,-22.909938,-47.062633&transacao=Aluguel&tipo=Im%C3%B3vel%20usado"
    if page%10==0:
        print("Page:{}/{}".format(page,total_pages),end=' ')
        current = timeit.default_timer()
        print("Time: {:.2f}min Estimated time:{:.2f}min".format((current-start)/60,total_pages*(current-start)/(page*60))  
    
    html_text = requests.get(url_page, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')

    cards = soup.find_all('div', class_='simple-card__box')

    for card in cards:
        try:
            rent = card.find('p', class_='simple-card__price js-price heading-regular heading-regular__bolder align-left').text
        except:
            rent = ""
        try:
            condominium = card.find('li', class_='card-price__item condominium text-regular').text
        except:
            condominium = ""
        try:
            iptu = card.find('li', class_='card-price__item iptu text-regular').text
        except:
            iptu = ""
        try:
            adress = card.find('p', class_='simple-card__address').text
        except:
            adress = ""
        try:
            area = card.find('li', class_='feature__item text-small js-areas').text
        except:
            area = ""
        try:
            room = card.find('li', class_='feature__item text-small js-bedrooms').text
        except:
            room = ""
        try:
            car_space = card.find('li', class_='feature__item text-small js-parking-spaces').text
        except:
            car_space = ""
        try:
            bathroom = card.find('li', class_='feature__item text-small js-bathrooms').text
        except:
            bathroom = ""
        try:
            description = card.find('span', class_='text-regular simple-card__text').text
        except:
            description = ""
        try:
            link = card.find('a').text
        except:
            link = ""

        # Correct and clean the data
        writer.writerow([
                rent.replace(' ','').replace("\n", "").replace(".", "")[2:-4],
                condominium.replace(' ','').replace("\n", "").replace(".", "")[12:],
                iptu.replace(' ','').replace("\n", "").replace(".", "")[6:],
                adress,
                area.replace(' ','').replace("\n", "").replace(".", "")[:-2],
                room.replace(' ','').replace("\n", "").replace(".", ""),
                car_space.replace(' ','').replace("\n", "").replace(".", ""),
                bathroom.replace(' ','').replace("\n", "").replace(".", ""),
                description,
                link
            ])

site_data.close()
file_printed = pandas.read_csv('site_data_zap.csv',sep='\t',header=None)

