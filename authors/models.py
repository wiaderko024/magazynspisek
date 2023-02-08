from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    surname = models.CharField(max_length=64, blank=False, null=False)
    birth_date = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=False, null=False)
    department = models.TextField(blank=True, null=True)
    instagram = models.CharField(max_length=128, blank=True, null=True)
    facebook = models.TextField(blank=True, null=True)
    portrait = models.ImageField(upload_to='authors_portraits', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
