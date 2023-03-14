from django.shortcuts import render
from .models import Article


def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles_list.html', {'articles': articles})
