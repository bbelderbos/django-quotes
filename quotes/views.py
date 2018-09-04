from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Quote


class QuoteList(ListView):
    model = Quote


class QuoteView(DetailView):
    model = Quote


class QuoteCreate(CreateView):
    model = Quote
    fields = ['quote', 'author', 'source', 'cover']
    success_url = reverse_lazy('quotes:quote_list')


class QuoteUpdate(UpdateView):
    model = Quote
    fields = ['quote', 'author', 'source', 'cover']
    success_url = reverse_lazy('quotes:quote_list')


class QuoteDelete(DeleteView):
    model = Quote
    success_url = reverse_lazy('quotes:quote_list')
