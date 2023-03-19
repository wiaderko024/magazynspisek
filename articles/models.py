from django.db import models

from authors.models import Author


class Article(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    cover = models.ImageField(upload_to='articles_photos', blank=False, null=False)
    cover_author = models.ForeignKey(
        Author,
        on_delete=models.DO_NOTHING,
        related_name='cover_author',
        blank=True,
        null=True
    )
    date = models.DateField(blank=True, null=True)
    article = models.TextField(blank=False, null=False)
    ARTICLE_TYPES = [
        ('Akt I', 'Akt I'),
        ('Akt II', 'Akt II'),
        ('Akt III', 'Akt III'),
        ('Inne', 'Inne')
    ]
    act = models.CharField(max_length=10, choices=ARTICLE_TYPES, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self):
        return self.title
