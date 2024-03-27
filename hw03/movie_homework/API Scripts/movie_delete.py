import requests

id = 135
api_url = f'http://127.0.0.1:8000/movie/api/list/{id}/'

response = requests.delete(api_url)

if response.status_code == 204:
    print("Movie deleted successfully")
else:
    print(f"Error deleting the movie: status code {response.status_code}")