import requests

api_url = f'http://127.0.0.1:8000/movie/api/list/'

response = requests.get(api_url)

if response.status_code == 200:
    movie_data = response.json()
    for movie in movie_data:
        print(movie.get("title") + ":")
        print(f'{movie.get("director")}, {movie.get("release_year")}, {movie.get("budget")}, {movie.get("runtime")}, {movie.get("rating")}, {movie.get("genre")}.')
        print(movie.get("description"))
        print("")
else:
    print(f"Error retrieving the movie list: status code {response.status_code}")