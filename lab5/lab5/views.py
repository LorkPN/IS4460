from django.views import View
from django.shortcuts import render, redirect
from .forms import FeedbackForm

class HomePageView(View):

    template_name = 'lab5/index.html'

    def get(self, request):

        form = FeedbackForm()
     
        return render(request, self.template_name,{'form':form})


    def post(self, request):

        form = FeedbackForm(request.POST)

        my_message = ""

        if form.is_valid():
            service_selected = 'srvc' in form.cleaned_data['review_area']
            my_message = form.cleaned_data['my_message']
            my_name = form.cleaned_data['your_name']
            return redirect(f'thanks/?name={my_name}&service_selected={service_selected}&message={my_message}')
            
        #you don't need an else here because the return function exits the 'post' method
        context = {'form':form}

        return render(request, self.template_name, context)
        


class ThankYouPageView(View):

    template_name = 'lab5/thanks.html'

    def get(self, request):

        my_name = request.GET.get('name')
        my_message = request.GET.get('message')
        service_selected = request.GET.get('service_selected') == "True"

        context = {'my_name':my_name, 'service_selected':service_selected, 'my_message':my_message}

        return render(request, self.template_name, context)
