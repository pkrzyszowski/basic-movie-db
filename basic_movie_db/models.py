from django.db import models


class Movie(models.Model):
    title = models.CharField('Title', max_length=255, unique=True)
    year = models.CharField('Year', max_length=255, null=True, blank=True)
    released = models.CharField('Released', max_length=255, null=True, blank=True)
    runtime = models.CharField('Runtime', max_length=255, null=True, blank=True)
    genre = models.CharField('Genre', max_length=255, null=True, blank=True)
    director = models.CharField('Director', max_length=255, null=True, blank=True)
    writer = models.CharField('Writer', max_length=255, null=True, blank=True)
    actors = models.CharField('Actors', max_length=255, null=True, blank=True)
    plot = models.TextField('Plot', null=True, blank=True)
    language = models.CharField('Language', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Text')