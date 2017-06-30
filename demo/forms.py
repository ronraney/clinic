from django import forms

from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('maiden_name', 'birth_date', 'city_of_birth')
        help_texts = {
            'birth_date': 'Format: 1984-02-31',
            'maiden_name': "Mother's last name by birth",
            'city_of_birth': "Just the city, no state needed"
        }