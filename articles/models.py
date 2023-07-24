from django.db import models

from authors.models import Author

from ckeditor.fields import RichTextField


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

    main_article = models.BooleanField(default=False, blank=False, null=False)
    long_cover = models.ImageField(upload_to='articles_long_covers', blank=True, null=True)
    long_cover_author = models.ForeignKey(
        Author,
        on_delete=models.DO_NOTHING,
        related_name='long_cover_author',
        blank=True,
        null=True
    )
    LONG_COVER_THEMES = [
        ('white', 'white'),
        ('dark', 'dark')
    ]
    long_cover_theme = models.CharField(max_length=5, choices=LONG_COVER_THEMES, blank=True, null=True)

    date = models.DateField(blank=True, null=True)
    article = RichTextField(blank=False, null=False)
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

    def save(self, *args, **kwargs):
        if self.main_article:
            for article in Article.objects.filter(main_article=True):
                article.main_article = False
                article.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
