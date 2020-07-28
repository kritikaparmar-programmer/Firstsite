from django.conf.urls import url
from django.contrib import admin
from . import views  # . (dot) means this directory

app_name = 'books'  # app name which we have

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    # /books/2(id)
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'books/add/$', views.BookCreate.as_view(), name='book-add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.BookUpdate.as_view(), name='book_edit'),
]
