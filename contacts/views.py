from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.template import loader
from django.views import generic

from .models import Person

# Create your views here.

class IndexView(generic.ListView):
    #template_name = 'templates/contacts/person_list.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        return Person.objects.all()


    #def get_context_data(self, **kwargs):
    #    context = super(IndexView, self).get_context_data(**kwargs)
    #    return context

class DetailView(generic.DetailView):
    model = Person

#def index(request):
#    contact_list = Person.objects.all()
#    template = loader.get_template('contacts/index.html')
#    context = {'contact_list': contact_list}
#    return HttpResponse(template.render(context, request))
