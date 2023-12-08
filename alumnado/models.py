from django.db import models


class MusicStyle(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name


class Alumnado(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    birthday = models.CharField(max_length=200)
    is_from = models.CharField(max_length=250)
    job = models.CharField(max_length=250)
    hobbies = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)
    eliminated = models.BooleanField(null=True)
    music_style = models.ManyToManyField(MusicStyle)

    def __str__(self):
        return self.name
