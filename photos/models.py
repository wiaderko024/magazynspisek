from django.db import models

from authors.models import Author
from articles.models import Article


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos', blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, blank=False, null=False)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self):
        return f'{self.article.title} - {self.photo.name}'
