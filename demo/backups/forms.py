from django import forms

from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('maiden_name', 'birth_date', 'city_of_birth')