## House_rent_prices - About
This project was made in Python 3.8.5

## Introduction
This is a project of mine to analyse house rent prices on the city of Campinas, in São Paulo state, Brazil.  
My initial motivation was to learn a bit of data science and to find what are the rent prices in Campinas, since i'm thinking of moving to a new house in the next months.  
Since this was a very practical project with very useful results i choose it as a learning exercise.

## Workflow  
### Get the data
I initially do a [web scrapping](Web_scrapping_vivareal.py) on a site called vivareal.com.br with the BeautifulSoup python library. Its not the most efficient way to do web scrapping but its easy and fast, so better suited for a small project like this one.  
After I made the [analysis of the results](Analisys_vivareal.py), i found out that the claimed "40.000+" results were all the same 65 results repeated over and over again. So i basically wasted my time on that site.  
#disappointed  
Then  i went to zapimoveis.com.br, made a new [web scrapping](Web_scrapping_zap.py) which gave actual results (even though the number of results were also inflated) getting about 6000 house prices which i moved to a .csv file.  
On a side note, i've tried other sites too but some had a captcha barrier or were harder to deal with, since they had an infinite scroll and not single pages results.  

### Analyzing the results
[I made the analysis of those results](Analisys_zap.py) initially reducing the data to a smaller scale, up to a max rent of 2500, an area of 250 and so on.  
I did that because the rent data also included commercial buildings with 1000m^2 or 30 car spaces with didn't make sense to me, since i was looking for a house to rent and i don't have R$20.000 to pay rent every month . . . yet.  
More details can be seen in the file but i tried to make some sense of the data, either comparing variables or clustering similar points.  
For and easier visualization some of the graphs were exported as images.

### Machine learning
After that, [i applied some machine learning](Machine_learning.py) to make a projection of the data.  
So, a house with this many rooms, this area and this number of car spaces will cost how much?, sort of question

## Future implementations
1. I think there is still space for a better analysis on the data. Some of the clustering didn't make a lot of sense or simply weren't very helpful.
2. The machine learning need to be completed. Its on my todo list.
3. Actually rent a house. Please give me money (;-;)
