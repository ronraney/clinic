from django.contrib import admin
from .models import Person

#admin.site.register(Person)

#Define the Person class
class PersonAdmin(admin.ModelAdmin):
    list_display = ('unique_id', 'maiden_name', 'city_of_birth', 'birth_date', 'age')

admin.site.register(Person, PersonAdmin)
    


