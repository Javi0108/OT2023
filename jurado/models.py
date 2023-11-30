from django.db import models


class Jurado(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    is_from = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name
