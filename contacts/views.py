from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views import generic
from django.db.models import Q

from .models import Person

class IndexView(generic.ListView):
    context_object_name = 'person_list'

    def get_queryset(self):
        return Person.objects.all()

class DetailView(generic.DetailView):
    model = Person

def search_results(request):
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box', None)
        results = Person.objects.filter(Q(name__icontains=search_query))
        return render(request,'contacts/search_results.html', {"results": results})
