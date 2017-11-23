from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.template import loader

# Create your views here.


def index(request):
    contact_list = Person.objects.all()
    #output = print('\n').join([c.name for c in contact_list])
    template = loader.get_template('contacts/index.html')
    context = {
        'contact_list': contact_list,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    contact_list = Person.objects.all()
    output = print('\n').join([c.name for c in contact_list])
    return HttpResponse(output)

def view_list(request):
    return HttpResponse("Contact List:")

def contact(request, person_id):
    output = str(Person.objects.order_by('-name')[person_id])
    return HttpResponse("Showing contact %s" % person_id, output )

# Create your views here.
