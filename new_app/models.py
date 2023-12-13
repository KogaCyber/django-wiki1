from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Category(models.Model):
    titles = models.CharField(max_length=200, unique=True, null=True, blank=True, verbose_name="title")
    components = models.TextField(blank=True, default="pustoy")

    def __str__(self):
        return self.titles

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})
