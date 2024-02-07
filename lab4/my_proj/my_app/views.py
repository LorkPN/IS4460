from django.views import View
from django.shortcuts import render, redirect

def title_name(the_name):
    return the_name.casefold()

class HomePageView(View):
    def get(self, request):
        
        my_name = "MATTHEW"

        new_name = title_name(my_name)

        context = {'hi':title_name('salutations earthling '), 'name':new_name}

        return render(request, 'my_app/index.html', context)