# House rent prices
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)

![Example data image](https://github.com/Pedronagy/House_rent_prices/blob/master/Figures/area_rent_03.jpeg)

## Table of contents
- [Introduction](#introduction)
- [Workflow](#workflow)
    - [Get the data](#get-the-data)
    - [Analyzing the results](#analyzing-the-results)
    - [Machine learning](#machine-learning)
- [Future implementations](#future-implementations)


## Introduction
This is a project of mine to analyse house rent prices on the city of Campinas, in São Paulo state, Brazil.  
My initial motivation was to learn a bit of data science and to find what are the rent prices in Campinas, since i'm thinking of moving to a new house in the next months.  
Since this was a very practical project with very useful results i choose it as a learning exercise.  
The big question here is: **How much will i have to pay to rent a house in Campinas?**  
The second big question is: **Will i be able to afford it or i'll be homeless forever ?**  
But the second one is not included on this project, only in my life projects :)

## Workflow  
### Get the data
I initially do a web scrapping([Web_scrapping_vivareal.py](https://github.com/Pedronagy/House_rent_prices/blob/master/Failed%20web%20scraping/Web_scrapping_vivareal.py)) on a site called vivareal.com.br with the BeautifulSoup python library. Its not the most efficient way to do web scrapping but its easy and fast, so better suited for a small project like this one.  
After I made the analysis of the results([Analisys_vivareal.py](https://github.com/Pedronagy/House_rent_prices/blob/master/Failed%20web%20scraping/Analisys_vivareal.py)), i found out that the claimed "40.000+" results were all the same 65 results repeated over and over again. So i basically wasted my time on that site (#disappointed).  
Then  i went to zapimoveis.com.br, made a new web scrapping([Web_scrapping_zap.py](Web_scrapping_zap.py)) which gave actual results (even though the number of results were also inflated) getting about 6000 house prices which i moved to a .csv file.  
On a side note, i've tried other sites too but some had a captcha barrier or were harder to deal with, since they had an infinite scroll and not single pages results.  

### Analyzing the results
I made the analysis of those results ([Analisys_zap.ipynb](Analisys_zap.ipynb)) initially reducing the data to a smaller scale, up to a max rent of 2500, an area of 250 and so on.  
I did that because the rent data also included commercial buildings with 1000m^2 or 30 car spaces which didn't make sense to me, since i was looking for a house to rent and i don't have R$20.000 to pay rent every month . . . yet.  
More details can be seen in the code but i tried to make some sense of the data comparing variables, ploting box plots to see the distribution and so on.  
For and easier visualization some of the graphs were exported as images, so i didn't had to make new compilations every time.  

### Machine learning
After that, i applied some machine learning ([Machine_learning.ipynb](https://github.com/Pedronagy/House_rent_prices/blob/master/Machine%20learning.ipynb)) to make a projection of the data and cluster similar points.
I tried some linear regression and different methods for the clustering.

## Future implementations
1. I think there is still space for a better analysis on the data. Some of the clustering didn't make a lot of sense or simply weren't very helpful.
2. Actually rent a house. Please give me money (;-;)
