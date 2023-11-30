from django.db import models


class Profesorado(models.Model):
    name = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=250, default='')
    image = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)
    origen = models.TextField(blank=True)
    edad = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
