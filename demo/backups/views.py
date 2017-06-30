from django.shortcuts import render, get_object_or_404
from .models import Person

# Create your views here.
def demo_list(request):
    people = Person.objects.order_by('unique_id')
    return render(request, 'demo/demo_list.html', {'people': people})

def demo_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'demo/demo_detail.html', {'person': person})    