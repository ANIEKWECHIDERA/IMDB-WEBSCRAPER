#first, i imported the necessary libraries for the project 

from bs4 import BeautifulSoup
import requests
import openpyxl

#creating an excel workbook to save the info into
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'IMDB top rated movies data'
sheet.append(['Movie rank', 'Movie name', 'Movie year', 'Movie rating'])

#extracting the data from the site by parsing the HTML content of the site using beatifulsoup
and the whole code is basically done in a 'try' block incase of errors
url = "https://www.imdb.com/chart/top/"
try:
    source = requests.get(url)
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')
    #print(soup)
    #searching the parsed HTML content for the location of the info i want to scrape
    
    movies = soup.find('tbody', class_= "lister-list").find_all('tr')
    #print(len(movies))
    
    #creating a loop to search the in for from the apropriate tag
    
    for movie in movies:
        
        name = movie.find('td', class_="titleColumn").a.text
        
        rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
        
        year = movie.find('td', class_="titleColumn").span.text.strip('()')
        
        rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
        
        print(rank, name, year, rating)
       #now i have to append the result of the search to the excel file
        
        sheet.append([int(rank), name, int(year), int(float(rating))])
    
except Exception as e:
   print(e)

#this is saving the excel file to my desktop withthe name 'imdb movie rating.xlsx'
excel.save(r'C:\Users\chide\Desktop\imdb movie rating.xlsx')





