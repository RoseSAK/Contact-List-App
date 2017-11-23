from django.conf.urls import url

from contacts import views

urlpatterns = [
    # example: /contacts/
    url(r'^$', views.index, name='index'),
    # example: /contacts/5/
    url(r'^(?P<person_id>[0-9]+)/$', views.contact, name='contact'),
]
