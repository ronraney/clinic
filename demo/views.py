from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from .forms import PersonForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def demo_list(request):
    people = Person.objects.order_by('unique_id')
    return render(request, 'demo/demo_list.html', {'people': people})

@login_required
def demo_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'demo/demo_detail.html', {'person': person})   

@login_required
def demo_new(request):    
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            #post.author = request.user ###We should add data entry person
            #post.published_date = timezone.now() ###We should add entry timestamp
            person.save()
            return redirect('demo_detail', pk=person.pk)
    else:
        form = PersonForm()
    return render(request, 'demo/demo_edit.html', {'form': form})

@login_required
def demo_edit(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            person.save()
            return redirect('demo_detail', pk=person.pk)
    else:
        form = PersonForm(instance=person)
    return render(request, 'demo/demo_edit.html', {'form': form})