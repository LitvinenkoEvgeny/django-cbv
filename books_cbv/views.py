from django.core.urlresolvers import reverse_lazy
from django.shortcuts import HttpResponse

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from books_cbv.models import Book


class BookList(ListView):
    model = Book
    paginate_by = 3


class BookCreate(CreateView):
    model = Book
    fields = ["name", "pages"]
    success_url = reverse_lazy("books_cbv:book_list")


class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('books_cbv:book_list')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books_cbv:book_list')

class BookDetail(DetailView):
    model = Book
