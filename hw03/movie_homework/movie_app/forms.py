from django import forms
from movie_app.models import Movie, User

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']