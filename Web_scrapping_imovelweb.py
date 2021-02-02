#%%
from os import replace
from bs4 import BeautifulSoup
import requests
import csv
import pandas
import timeit

url = "https://www.imovelweb.com.br/imoveis-aluguel-campinas-sp-pagina-"
page = 1


#%%
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}

for page in range(1,5):
    url_page = url + str(page) + ".html"
    # print(url_page)
    
    html_text = requests.get(url_page, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')

    with open("Data/site_text.html",'w',encoding="utf8") as file:
        file.write(str(soup.prettify()))

    # cards = soup.find_all('div', class_='postingCardTop')

    cards = soup.find('div', class_='postingCardTop')
    print(cards)

    # for card in cards:
    #     print(card.text)
    #     print("-------------------------//-------------------")

# %%