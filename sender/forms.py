from django import forms
from sender.models import Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'

    def clean_time_send(self):
        cleaned_data = self.cleaned_data['time_send']
        if ':' not in cleaned_data or cleaned_data.count(':') > 1:
            raise forms.ValidationError("Enter correct value time_send")
        else:
            split_data = cleaned_data.split(':')
            if (split_data[0] not in (f"{i}" for i in range(24)) or
                    split_data[1] not in (f"{i}" for i in range(60))):
                raise forms.ValidationError("Enter correct value time_send")
        return cleaned_data

    def clean_time_stop(self):
        cleaned_data = self.cleaned_data['time_stop']
        if ':' not in cleaned_data or cleaned_data.count(':') > 1:
            raise forms.ValidationError("Enter correct value time_stop")
        else:
            split_data = cleaned_data.split(':')
            if (split_data[0] not in (f"{i}" for i in range(24)) or
                    split_data[1] not in (f"{i}" for i in range(60))):
                raise forms.ValidationError("Enter correct value time_stop")
        return cleaned_data
