import requests
import json

id = 135
api_url = f'http://127.0.0.1:8000/movie/api/list/{id}/'

movie_data = {
    "title":"Oppenheimer",
    "description":"The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb.",
    "director":"Christopher Nolan",
    "release_year":"2023",
    "budget":"100 million",
    "runtime":"180 min",
    "rating":"7.3",
    "genre":"History",
}

response = requests.put(url = api_url,
                         data = json.dumps(movie_data),
                         headers={"Content-Type": 'application/json'})

if response.status_code == 200:
    print("Movie updated successfully.")
else:
    print(f"Error updating movie: status code {response.status_code}")