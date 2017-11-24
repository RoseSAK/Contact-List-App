from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.template import loader

# Create your views here.

def index(request):
    contact_list = Person.objects.all()
    template = loader.get_template('contacts/index.html')
    context = {'contact_list': contact_list}
    return HttpResponse(template.render(context, request))

def contact_details(request, person_id):
    c = Person.objects.get(pk=person_id)
    c_info = c.get_fields
    #print(type(c), c)
    #output = ".".join([i for i in c_info])
    return HttpResponse(c_info)
