from django import forms
from sender.models import Newsletter
from client.models import Client
from django.forms import DateTimeInput


class NewsletterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        owner = self.request.user
        super().__init__(*args, **kwargs)
        self.fields['clients'].queryset = Client.objects.filter(owner=owner)

    class Meta:
        model = Newsletter
        exclude = ('owner', 'status', 'next_date', 'is_active')
        widgets = {
            'start_date': DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
            'stop_date': DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
        }

    def clean(self):
        data = self.cleaned_data
        if 'start_date' in data.keys() and 'stop_date' in data.keys():
            start_date = data['start_date']
            stop_date = data['stop_date']
            if start_date >= stop_date:
                raise forms.ValidationError("Stop date must be bigger than start date")
