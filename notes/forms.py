from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ('title', 'note')
        labels = {
            'note': 'Write your thoughts here'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'note': forms.Textarea(attrs={'class': 'form-control mb5'})

        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'fuck' in title.lower():
            raise ValidationError('We only accept notes sans profanity')
        return title