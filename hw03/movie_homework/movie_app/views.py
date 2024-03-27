from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .models import Movie, User, Role
from .forms import MovieForm, LoginForm

# Create your views here.
class LoginView(View):

    def get(self, request):

        form = LoginForm()

        context = {'form':form}

        return render(request = request, template_name='movie_app/movie-login.html', context=context)
    
    def post(self, request):
        
        return redirect(reverse('movie-list'))

class MovieListView(View):

    def get(self, request):

        movies = Movie.objects.all()

        context = {'movies' : movies}

        return render(request = request, template_name='movie_app/movie-list.html', context = context)

class MovieAddView(View):
    
    def get(self, request):

        movie_form = MovieForm()

        context = {'form':movie_form, 'action':'Add', 'back_text':'Movies', 'back_target':'list'}

        return render(request = request, template_name='movie_app/movie-update.html', context = context)
    
    def post(self, request, movie_id=None):

        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

        movie_form = MovieForm(request.POST, instance=movie)

        if movie_form.is_valid():

            movie_form.save()
            return redirect(reverse('movie-list'))
        
        context = {'form':movie_form, 'action':'Add', 'back_text':'Movies', 'back_target':'list'}

        return render(request = request, template_name='movie_app/movie-add.html', context = context)
    

class MovieUpdateView(View):
    
    def get(self, request, movie_id=None):

        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

        movie_form = MovieForm(instance=movie)

        context = {'form':movie_form, 'movie':movie, 'action':'Update', 'back_text':'Details', 'back_target':"movie-details"}

        return render(request = request, template_name='movie_app/movie-update.html', context = context)
    
    def post(self, request, movie_id=None):
        
        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

        movie_form = MovieForm(request.POST, instance=movie)

        if movie_form.is_valid():

            movie_form.save()
            return redirect(reverse('movie-details') + str(movie_id))
        
        context = {'form':movie_form, 'movie':movie, 'action':'Update', 'back_text':'Details', 'back_target':'movie-details'}

        return render(request = request, template_name='movie_app/movie-update.html', context = context)
    
class MovieDetailView(View):
    
    def get(self, request, movie_id=None):

        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

        context = {'movie':movie}

        return render(request = request, template_name='movie_app/movie-details.html', context = context)
    
class MovieDeleteView(View):
    
    def get(self, request, movie_id=None):

        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

        movie_form = MovieForm(instance=movie)

        for field in movie_form.fields:
            movie_form.fields[field].widget.attrs['disabled'] = True

        context = {'form':movie_form, 'movie':movie, 'action':'Delete', 'back_text':'Details', 'back_target':'movie-details'}

        return render(request = request, template_name='movie_app/movie-update.html', context = context)

    def post(self, request, movie_id=None):

        movie = Movie.objects.get(pk=movie_id)
        
        movie.delete()
            
        return redirect(reverse('movie-list'))
