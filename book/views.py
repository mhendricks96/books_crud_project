from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Book
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
  template_name = 'home.html'
  model = Book

class BookListView(ListView):
  template_name = 'book_list.html'
  model = Book
  context_object_name = 'list_of_books'

class BookDetailView(DetailView):
  template_name = 'book_detail.html'
  model = Book

class BookCreateView(CreateView):
  template_name = 'create_book.html'
  model = Book
  fields = ['title', 'author', 'owner']
  success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
  template_name = 'update_book.html'
  model = Book
  fields = ['title', 'author', 'owner']
  success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
  template_name = 'delete_book.html'
  model = Book
  success_url = reverse_lazy('book_list')