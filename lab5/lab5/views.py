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
        sup = ""

        service_selected = False;

        if form.is_valid():
            my_message = form.cleaned_data['my_message']
            service_selected = 'srvc' in form.cleaned_data['review_area']

            return redirect('thanks/')

        #you don't need an else here because the return function exits the 'post' method
        context = {'form':form,
                   'my_message':my_message, 
                   'service_selected':service_selected}

        return render(request, self.template_name, context)
        


class ThankYouPageView(View):

    template_name = 'lab5/thanks.html'

    def get(self, request):

        my_name = "Matt Young"

        context = {'my_name':my_name}

        return render(request, self.template_name, context)
