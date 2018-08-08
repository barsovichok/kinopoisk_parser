import requests
from bs4 import BeautifulSoup
from lxml import html

def input_user_data():
    user_input = input('Напишите ссылку на фильм на Кинопоиске\n')
    return user_input

def get_requests(user_input):
    page = requests.get(user_input)
    return page

def parse_soup(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def find_movie_name(soup):
    movie_name = soup.find(class_="moviename-big")
    movie_name = movie_name.get_text()
    return movie_name

def find_director(soup):
    director = soup.find(itemprop="director")
    director = director.a.get_text()
    return director

def find_box_office(soup):
    box_office = soup.find(id ="div_usa_box_td2")
    box_office = box_office.div.a
    box_office = box_office.get_text()
    box_office = box_office[1:]
    box_office = box_office.replace('\xa0', '')
    box_office = int(box_office)
    return box_office


def find_image(soup):
    image = soup.find(id="photoBlock")
    image = image.div.img.get('src')
    return image

def dict_film_data(movie_name, director, box_office, image):
    dict_film_data = {'film':movie_name, 'director':director, 'box_office':box_office, 'image':image}
    return dict_film_data

def print_film_data(dict_film_data):
    print(dict_film_data)

   
if __name__ == '__main__': 
    user_input = input_user_data()
    page = get_requests(user_input)
    soup = parse_soup(page)
    movie_name = find_movie_name(soup)
    director = find_director(soup)
    box_office = find_box_office(soup)
    image = find_image(soup)
    dict_film_data = dict_film_data(movie_name, director, box_office, image)
    print_film_data(dict_film_data)




