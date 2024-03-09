import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_homework.settings')
django.setup()

from movie_app.models import Movie, User

#1. Delete existing entries from Movie and User
movie_list = Movie.objects.all()
user_list = User.objects.all()

for movie in movie_list:
    movie.delete()

for user in user_list:
    user.delete()

#2. Add 10 movie objects to the database

movie1 = Movie(title="Joker",
                description="During the 1980s, a failed stand-up comedian is driven insane and turns to a life of crime and chaos in Gotham City while becoming an infamous psychopathic crime figure.",
                director="Todd Phillips", release_year="2019", budget="$55-70 million", runtime="122 min", rating="R", genre="Thriller")
movie1.save()