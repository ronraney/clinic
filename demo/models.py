from django.db import models
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

class Person(models.Model):
    unique_id = models.CharField(max_length=6, blank=True)
    maiden_name = models.CharField(max_length=25)
    birth_date = models.DateField()
    city_of_birth = models.CharField(max_length=25)

    @property
    def get_unique_id(self):
        a = self.maiden_name[:2].upper()     #First 2 letters of maiden name
        b = self.birth_date.strftime('%d')     #Day of the month as string
        c = self.city_of_birth[:2].upper()     #First 2 letters of city
        return a + b + c 
        
    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def save(self, *args, **kwarg):
        self.unique_id = self.get_unique_id
        super(Person, self).save(*args, **kwarg)

    def __str__(self):
        return self.unique_id
