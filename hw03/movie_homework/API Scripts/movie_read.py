import requests

id = 133
api_url = f'http://127.0.0.1:8000/movie/api/list/{id}/'

response = requests.get(api_url)

if response.status_code == 200:
    movie_data = response.json()
    print(movie_data.get("title") + ":")
    print(f'{movie_data.get("director")}, {movie_data.get("release_year")}, {movie_data.get("budget")}, {movie_data.get("runtime")}, {movie_data.get("rating")}, {movie_data.get("genre")}.')
    print(movie_data.get("description"))
else:
    print(f"Error retrieving the movie: status code {response.status_code}")