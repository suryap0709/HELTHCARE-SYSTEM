import requests
from bs4 import BeautifulSoup

def scrape_movie_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movie_data = []
    for movie in soup.find_all('div', class_='movie'):
        title = movie.find('h2').text
        release_year = int(movie.find('span', class_='year').text)
        genre = movie.find('span', class_='genre').text
        rating = float(movie.find('span', class_='rating').text)
        movie_data.append({'title': title, 'release_year': release_year, 'genre': genre, 'rating': rating})
    
    return movie_data

def average_rating_by_year(movie_data, year):
    movies_in_year = [movie['rating'] for movie in movie_data if movie['release_year'] == year]
    return sum(movies_in_year) / len(movies_in_year) if movies_in_year else 0

# Example usage:
url = 'https://example.com/movies'
movie_data = scrape_movie_data(url)
print("Scraped Movie Data:", movie_data)

average_rating_2023 = average_rating_by_year(movie_data, 2023)
print("Average Rating for Movies Released in 2023:", average_rating_2023)
