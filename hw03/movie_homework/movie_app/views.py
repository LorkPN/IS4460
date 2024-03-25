from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .models import Movie, User, Role
from .forms import MoiveForm

# Create your views here.
class LoginView(View):

    def get(self, request):

        return render(request = request, template_name='movie_app/movie-login.html')
    
    def post(self, request):
        
        return redirect('movie-list')

class MovieListView(View):

    def get(self, request):

        movies = Movie.objects.all()

        context = {'movies' : movies}

        return render(request = request, template_name='movie_app/movie-list.html', context = context)

class MovieAddView(View):
    
    def get(self, request):

        movie_form = MoiveForm()

        context = {'form':movie_form}

        return render(request = request, template_name='movie_app/movie-add.html', context = context)
    
    def post(self, request):

        movie_form = MoiveForm(request.POST)

        if movie_form.is_valid():

            movie_form.save()
            redirect(reverse('movie-list'))
        
        context = {'form':movie_form}

        return render(request = request, template_name='movie_app/movie-add.html', context = context)
    

class MovieUpdateView(View):
    
    def get(self, request, movie_id=None):

        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

        movie_form = MoiveForm(instance=movie)

        context = {'form':movie_form, 'movie':movie}

        return render(request = request, template_name='movie_app/movie-update.html', context = context)
    
    def post(self, request, movie_id=None):
        
        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

        movie_form = MoiveForm(request.POST, instance=movie)

        if movie_form.is_valid():

            movie_form.save()
            redirect(reverse('movie-details'))
        
        context = {'form':movie_form, 'movie':movie}

        return render(request = request, template_name='movie_app/movie-update.html', context = context)
    
class MovieDetailView(View):
    
    def get(self, request, movie_id=None):

        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

        context = {'movie':movie}

        return render(request = request, template_name='movie_app/movie-details.html', context = context)