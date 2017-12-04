from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views import generic

from .models import Person
from django.db.models import Q
import operator, functools

class IndexView(generic.ListView):
    context_object_name = 'person_list'

    def get_queryset(self):
        return Person.objects.all()

class DetailView(generic.DetailView):
    model = Person

def search_results(request):
    if request.method == 'GET': # If the search box submit button is used
        search_query = request.GET.get('search_box', None) # get query term
        results = Person.objects.filter(Q(name__icontains=search_query) # OR lookup
                                        |Q(address__icontains=search_query)
                                        |Q(department__icontains=search_query))
        return render(request,'contacts/search_results.html', {"results": results})

# Attempts that didn't work
        #search_fields = Person._meta.get_fields() # get fields to search each field
        #search_fields = ['name__icontains', 'address__icontains', 'contact_details__contains', 'department__icontains']
        #q_list = [(x, search_query) for x in search_fields]
        #query_list = [Q(x) for x in q_list]
        #q = [Q(x:query) for x in search_fields]
        #for field_name in search_fields: #construct query object
        #    q = Q(**{"%s" % field_name: search_query})
        #    print(q)
        #print(results)
