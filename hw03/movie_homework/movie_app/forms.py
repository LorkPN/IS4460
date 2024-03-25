from django import forms
from movie_app.models import Movie, User

class MoiveForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']