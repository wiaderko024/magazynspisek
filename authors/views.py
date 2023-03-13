from django.shortcuts import render

from .models import Author


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'authors_list.html', {'authors': authors})
