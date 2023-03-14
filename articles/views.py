from django.shortcuts import render
from .models import Article


def articles_list(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'articles_list.html', {'articles': articles})


def articles_details(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles_details.html', {'article': article})
