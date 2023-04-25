from django.shortcuts import render

from photos.models import Photo
from .models import Article
from .utils import MONTHS


def articles_list(request):
    articles = Article.objects.all().order_by('-date')

    dates = {}
    for article in articles:
        dates[article.pk] = f'{article.date.day} {MONTHS[article.date.month]} {article.date.year}'

    context = {
        'articles': articles,
        'dates': dates
    }

    return render(request, 'articles_list.html', context)


def articles_details(request, pk):
    article = Article.objects.get(pk=pk)
    photos = Photo.objects.filter(article=article)
    context = {
        'article': article,
        'photos': photos,
        'date_pl': f'{article.date.day} {MONTHS[article.date.month]} {article.date.year}'
    }
    return render(request, 'articles_details.html', context)
