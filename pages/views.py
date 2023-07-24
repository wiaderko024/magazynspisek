from django.shortcuts import render

from articles.models import Article


def home_page(request):
    article = Article.objects.get(main_article=True)
    articles = Article.objects.all().order_by('created_at')[0:8]

    print(f'DEBUG -> {len(articles)}')

    if article.long_cover_theme == 'dark':
        styles = {
            'logo_color': '#EDEADE',
            'archive_color': '#EDEADE',
            'h1_color': '#EDEADE',
            'color': '#EDEADE'
        }
    else:
        styles = {
            'logo_color': '#323d47',
            'archive_color': '#EDEADE',
            'h1_color': '#323d47',
            'color': '#fff'
        }

    context = {
        'article': article,
        'articles': articles,
        'styles': styles
    }

    return render(request, 'index.html', context)
