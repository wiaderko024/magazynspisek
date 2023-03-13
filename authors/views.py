from django.shortcuts import render

from .models import Author


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})


def authors_details(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'authors_details.html', {'author': author})
