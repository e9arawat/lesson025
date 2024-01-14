from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'email', 'address', 'phoneNumber', 'linkedin']

class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255)
