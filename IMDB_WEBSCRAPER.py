from bs4 import BeautifulSoup
import requests
import openpyxl

#creating an excel workbook and sheet
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'IMDB top rated movies data'
sheet.append(['Movie rank', 'Movie name', 'Movie year', 'Movie rating'])

#extracting data
url = "https://www.imdb.com/chart/top/"
try:
    source = requests.get(url)
    source.raise_for_status()
    
    soup = BeautifulSoup(source.text, 'html.parser')
    #print(soup)
    
    movies = soup.find('tbody', class_= "lister-list").find_all('tr')
    #print(len(movies))
    
    for movie in movies:
        
        name = movie.find('td', class_="titleColumn").a.text
        
        rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
        
        year = movie.find('td', class_="titleColumn").span.text.strip('()')
        
        rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
        
        print(rank, name, year, rating)
        #break
        sheet.append([rank, name, year, rating])
    
except Exception as e:
   print(e)

#saving the excel file
excel.save(r'C:\Users\chide\Desktop\imdb movie rating2.xlsx')





