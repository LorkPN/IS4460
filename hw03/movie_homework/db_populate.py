#import Django files
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

movie2 = Movie(title="The Lord of the Rings: The Fellowship of the Ring",
                description="A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.",
                director="Peter Jackson", release_year="2001", budget="$93 million", runtime="178 min", rating="PG-13", genre="Fantasy")
movie2.save()

movie3 = Movie(title="The Lord of the Rings: The Two Towers",
                description="While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Sauron's new ally, Saruman, and his hordes of Isengard.",
                director="Peter Jackson", release_year="2002", budget="$94 million", runtime="179 min", rating="PG-13", genre="Fantasy")
movie3.save()

movie4 = Movie(title="The Lord of the Rings: The Return of the King",
                description="Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
                director="Peter Jackson", release_year="2003", budget="$94 million", runtime="201 min", rating="PG-13", genre="Fantasy")
movie4.save()

movie5 = Movie(title="The Prince of Egypt",
                description="Egyptian Prince Moses learns of his identity as a Hebrew and his destiny to become the chosen deliverer of his people.",
                director="Brenda Chapman", release_year="1998", budget="$60 million", runtime="99 min", rating="PG", genre="Animation")
movie5.save()

movie6 = Movie(title="A Silent Voice",
                description="A young man is ostracized by his classmates after he bullies a deaf girl to the point where she moves away. Years later, he sets off on a path for redemption.",
                director="Taichi Ishidate", release_year="2016", budget="$500 thousand", runtime="130 min", rating="PG-13", genre="Animation")
movie6.save()

movie7 = Movie(title="Interstellar",
                description="When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.",
                director="Christopher Nolan", release_year="2014", budget="$165 million", runtime="169 min", rating="PG-13", genre="Science Fiction")
movie7.save()

movie8 = Movie(title="X-Men: First Class",
                description="In the 1960s, superpowered humans Charles Xavier and Erik Lensherr work together to find others like them, but Erik's vengeful pursuit of an ambitious mutant who ruined his life causes a schism to divide them.",
                director="Matthew Vaughn", release_year="2011", budget="$140-160 million", runtime="132 min", rating="PG-13", genre="Science Fiction")
movie8.save()

movie9 = Movie(title="Willy Wonka & the Chocolate Factory",
                description="A poor but hopeful boy seeks one of the five coveted golden tickets that will send him on a tour of Willy Wonka's mysterious chocolate factory.",
                director="Mel Stuart", release_year="1971", budget="$3 million", runtime="100 min", rating="G", genre="Musical")
movie9.save()

movie10 = Movie(title="Oppenheimer",
                description="The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb.",
                director="Christopher Nolan", release_year="2023", budget="100 million", runtime="180 min", rating="R", genre="History")
movie10.save()

#3. Add 3 user objects to the database

user1 = User(username="XxVikingSlayerxX", password="D3nm4rksux!", first_name="Alfred", last_name="Great")
user1.save()

user2 = User(username="Henry I", password="lod$ofMon3", first_name="Henry", last_name="First", email="goldenrule@gmail.com")
user2.save()

user3 = User(username="Athelred the Unready", password="password", first_name="Athelred", last_name="Unred", email="danegeld@aol.com")
user3.save()

#4. Move query statements

#retrieve all movies
movie_list = Movie.objects.all()

#filter for movies starting with some text
filtered_movies = Movie.objects.filter(title__startswith="The Lord of the Rings")

#get one movie
single_movie = Movie.objects.get(title="Joker")

#update one movie
single_movie.budget = "$70 million"
single_movie.save()

#delete one movie
deleted_movie = Movie.objects.get(title="Oppenheimer")
deleted_movie.delete()

#5. User query statements

#get data for user given a username
vikingslayer = User.objects.get(username="XxVikingSlayerxX")