from django.views import View
from django.shortcuts import render, redirect
from . import my_functions, my_objects

def lower_name(the_name):
    return the_name.casefold()

class HomePageView(View):
    def get(self, request):
        
        my_name = "MATTHEW"

        new_name = lower_name(my_name)

        names = ["EDWARD", "HAROLD", "WILLIAM"]

        new_names = my_functions.title_names(names)

        boat1 = my_objects.Boat("black", "AHOOGA")
        car1 = my_objects.Car("yellow", "honk honk")

        context = {'hi':'salutations earthling ', 
                   'name':new_name, 
                   'names':new_names,
                   'boat':boat1, 
                   'car':car1}

        return render(request, 'my_app/index.html', context)