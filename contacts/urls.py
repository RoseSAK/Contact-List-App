from django.conf.urls import url

from contacts import views

app_name = 'contacts'

urlpatterns = [
    # example: /contacts/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # example: /contacts/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
