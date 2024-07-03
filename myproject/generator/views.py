from django.shortcuts import render, get_object_or_404
from .models import Person
from django.http import HttpResponse

def generator(request):
    people = Person.objects.all()
    return render(request, 'generator/generator.html', {'people': people})

def generate_text(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    greeting_text = person.greeting
    return HttpResponse(greeting_text)