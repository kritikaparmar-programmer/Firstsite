

# Create your views here.
from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView, UpdateView


class IndexView(generic.ListView):
    template_name = 'books/index.html'

    def get_queryset(self):
        return Book.objects.all()


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'type', 'book_image']


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'


class BookUpdate(generic.UpdateView):
    model = Book
    fields = ['name', 'author', 'price', 'type', 'book_image']
    template_name = 'books/book_update_form.html'


"""from django.http import HttpResponse
from .models import Book
# from django.template import loader
from django.shortcuts import render
from django.http import Http404


def index(request):
    # all the object
    all_books = Book.objects.all()
    context = {
        'all_books': all_books
    }
    return render(request, 'books/index.html', context)


def detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404('This book does not exist')
    return render(request, 'books/detail.html', {'book': book})"""
