import requests
import json

api_url = 'http://127.0.0.1:8000/movie/api/list/'

movie_data = {
    "title":"Oppenheimer",
    "description":"The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb.",
    "director":"Christopher Nolan",
    "release_year":"2023",
    "budget":"100 million",
    "runtime":"180 min",
    "rating":"8.3",
    "genre":"History",
}

response = requests.post(url = api_url,
                         data = json.dumps(movie_data),
                         headers={"Content-Type": 'application/json'})

if response.status_code == 201:
    print("Movie created successfully.")
else:
    print(f"Error creating movie: status code {response.status_code}")