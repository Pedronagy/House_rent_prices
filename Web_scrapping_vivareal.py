#%%
from os import replace
from bs4 import BeautifulSoup
import requests
import csv
import pandas
import timeit

def get_soup(url,page):
    html_text = requests.get(url + "page")
    soup = BeautifulSoup(html_text.text, 'lxml')
    return soup

url = "https://www.vivareal.com.br/aluguel/sp/campinas/?pagina="
page = 1
html_text = requests.get(url + "page").text
soup = BeautifulSoup(html_text, 'lxml')
house_results = soup.find('strong', class_="results-summary__count js-total-records").get_text().replace(' ','').replace('.','')
total_pages = int(house_results) // 36 # São 36 resultados por página

site_data =  open('site_data.csv', mode='w',newline='\n', encoding='utf-8')
writer = csv.writer(site_data,delimiter='\t')
site_data_names = [
        'rent', 
        'condominium',
        'description',
        'area',
        'room',
        'bathroom',
        'car_space',
        'amenities',
        'location',
        'link'
    ]
writer.writerow(site_data_names)
#%%
start = timeit.default_timer()
for page in range(20):
    url_page = url + str(page)
    print(page)

    html_text = requests.get(url_page).text
    soup = BeautifulSoup(html_text, 'lxml')

    cards = soup.find_all('article', class_='property-card__container js-property-card')
    
    for card in cards:
        link = card.find('a', class_="property-card__content-link js-card-title").get('href')
        description = card.find('span', class_='property-card__title').text
        location = card.find('span', class_='property-card__address').text
        area = card.find('li', class_="property-card__detail-item property-card__detail-area").text
        room = card.find('li', class_="property-card__detail-item property-card__detail-room js-property-detail-rooms").text
        bathroom = card.find('li', class_="property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom").text
        car_space = card.find('li', class_="property-card__detail-item property-card__detail-garage js-property-detail-garages").text

        # condominio = card.find('footer', class_='property-card__price-details')
        # condominio2 = card.find('div', class_='property-card__price-details--condo')
        # condominio3 = card.find('strong', class_='js-condo-price')
        # rent1 = card.find('section', class_='property-card__price js-property-card-prices js-property-card__price-small')#.text
        rent2 = card.find('p').text
        # rent3 = card.find('section', class_="property-card__values").text
        # rent4 = card.find('section', class_="property-card__values").p.text

        # for condominio_tag in card.find_all('p'):
        #     print(condominio_tag.text)
        #     print(condominio_tag.next_sibling) #preço da casa

        amenities = ''
        first_count = 1
        for amenities_tag in card.find_all('li', class_="amenities__item"):
            if first_count:
                amenities = amenities_tag.text
                first_count-=1
                continue
            amenities = amenities + ',' + amenities_tag.text
            
        condominium_price = ''
        for item in card.select('strong', class_="js-condo-price"):
            condominium_price = item.get_text()

        # print("-------------------------//-------------------")
        # print("https://www.vivareal.com.br" + link)
        # print(description[2:].split(' ')[0])
        # print(location.replace(' - ',','))

        # print(rent2.replace(' ','').replace('.','')[2:-4])
        # print(condominium_price.replace(' ','').replace('.','')[2:])

        # print(amenities)    
        # print(area.replace(' ','')[:-2])
        # print(room.split('  ')[1].replace('--','0'))
        # print(bathroom.split('  ')[1].replace('--','0'))
        # print(car_space.split('  ')[1].replace('--','0'))
        
        writer.writerow([
            rent2.replace(' ','').replace('.','')[2:-4], 
            condominium_price.replace(' ','').replace('.','')[2:],
            description[2:].split(' ')[0],
            area.replace(' ','')[:-2],
            room.split('  ')[1].replace('--','0'),
            bathroom.split('  ')[1].replace('--','0'),
            car_space.split('  ')[1].replace('--','0'),
            amenities,
            location.replace(' - ',','),        
            "https://www.vivareal.com.br" + link
        ])

stop = timeit.default_timer()
print('Time: ', stop - start, "s")  
    
site_data.close()
file_printed = pandas.read_csv('site_data.csv',sep='\t',header=None)


# %%