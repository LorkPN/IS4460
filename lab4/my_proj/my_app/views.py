from django.views import View
from django.shortcuts import render, redirect
from . import my_functions, my_objects

class HomePageView(View):
    def get(self, request):
        
        my_name = "MATTHEW"

        new_name = my_functions.title_name(my_name)

        names = ["EDWARD", "HAROLD", "WILLIAM"]

        new_names = my_functions.title_names(names)

        car1 = my_objects.Car("black", "honk honk")
        car2 = my_objects.Car("yellow", "honk honk")
        motorcycle1 = my_objects.Motorcycle("red", "vroom vroom")

        context = {'hi':'salutations earthling ', 
                   'original_name':my_name, 
                   'new_name':new_name,
                   "name_list":names,
                   'title_name_list':new_names,
                   'car1':car1, 
                   'car2':car2,
                   'motorcycle1':motorcycle1}

        return render(request, 'my_app/index.html', context)