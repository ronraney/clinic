from django.shortcuts import render
from .models import Person

# Create your views here.
def demo_list(request):
    people = Person.objects.order_by('unique_id')
    return render(request, 'demo/demo_list.html', {'people': people})
