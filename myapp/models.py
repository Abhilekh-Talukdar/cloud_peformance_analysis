from django.db import models

# Create your models here.

class Review(models.Model):
    reviewid = models.IntegerField()
    title = models.TextField()
    artist = models.TextField()
    url = models.TextField()
    score = models.FloatField()
    best_new_music = models.IntegerField()
    author = models.TextField()
    author_type = models.TextField()
    pub_date = models.TextField()
    pub_weekday = models.IntegerField()
    pub_day = models.IntegerField()
    pub_month = models.IntegerField()
    pub_year = models.IntegerField()

class Artist(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='artists')
    artist = models.TextField()

class Genre(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='genres')
    genre = models.TextField()

class Label(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='labels')
    label = models.TextField()

class Year(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='years')
    year = models.IntegerField()

class Content(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='content')
    content = models.TextField()
