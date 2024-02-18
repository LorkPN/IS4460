from django import forms

class FeedbackForm(forms.Form):
    my_message = forms.CharField(label='Feedback Message', widget=forms.Textarea)
    your_name = forms.CharField(max_length=100)
    review_area = forms.MultipleChoiceField(choices=[('food','Food'), ('srvc','Service'), ('abm','Ambiance')],
                                            widget=forms.CheckboxSelectMultiple)

    def clean_my_message(self):

        my_message: str = self.cleaned_data.get('my_message')

        badWords = ["bad", "terrible", "awful", "not cool", "stupid", "bland", "dirty", "sucks", "subpar", "lame"]

        for word in badWords:
            if word in my_message:
                raise forms.ValidationError(f"Hey, be nice. Don't use words like '{word}' in your review :(")
        
        return my_message

