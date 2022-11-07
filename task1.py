from bs4 import BeautifulSoup
import requests 
import json


url="https://www.imdb.com/india/top-rated-indian-movies//"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
# print(soup)
tbody=soup.find("tbody",class_="lister-list")
# print(tbody)
b=tbody.find_all("tr")

# print(b)

movie=[]

for i in b:
    movie_details={}

    movie_name=i.find("td",class_="titleColumn").a.get_text()
    # print(movie_name)
    movie_details["movie_name"]=movie_name

    movie_rank=i.find("td",class_="titleColumn").get_text().strip().replace("\n"," ").replace(" ","")
    movie_rank=movie_rank[:1]
    movie_details["movie_rank"]=int(movie_rank)

    rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
    movie_details["movie_rating"]=float(rating)

    year_of_release=i.find('td',class_="titleColumn").span.get_text()
    year=year_of_release[1:-1]
    movie_details["year_of_release"]=int(year)

    movie_link=i.find('td',class_="titleColumn").a["href"]
    link='https://www.imdb.com'+movie_link
    # print(link)

    movie_details["link"]=link

    movie.append(movie_details)
    # print(movie)
    

    with open("first_task.json","w")as f:
        data=json.dump(movie,f,indent=4)
    
