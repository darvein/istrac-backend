from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.conf import settings

class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} likes {self.content_object}"

class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} favorited {self.content_object}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # You can add more fields here if you want, like icons or parent categories for nested categories

    def __str__(self):
        return self.name

class Location(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    created_by = models.ForeignKey(User, related_name='photos', on_delete=models.CASCADE, default=settings.DEFAULT_USER_ID)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"Photo of "

class Video(models.Model):
    created_by = models.ForeignKey(User, related_name='videos', on_delete=models.CASCADE, default=settings.DEFAULT_USER_ID)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return f"Video of "


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = GenericRelation(Like)
    favorites = GenericRelation(Favorite)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.created_at}"


class TPlace(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.ForeignKey(Location, related_name='tplaces', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='tplaces', on_delete=models.CASCADE, default=settings.DEFAULT_USER_ID)
    photos = models.ManyToManyField(Photo, related_name='tplaces', blank=True)
    videos = models.ManyToManyField(Video, related_name='tplaces', blank=True)
    comments = models.ManyToManyField(Comment, related_name='tplaces', blank=True)
    categories = models.ManyToManyField(Category, related_name='tplaces', blank=True)
    likes = GenericRelation(Like)
    favorites = GenericRelation(Favorite)

    def __str__(self):
     return self.name

class Event(models.Model):
    tplace = models.ForeignKey(TPlace, related_name='events', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE, default=settings.DEFAULT_USER_ID)
    date = models.DateTimeField()
    title = models.CharField(max_length=200)
    photos = models.ManyToManyField(Photo, related_name='events', blank=True)
    videos = models.ManyToManyField(Video, related_name='events', blank=True)
    comments = models.ManyToManyField(Comment, related_name='events', blank=True)
    likes = GenericRelation(Like)
    favorites = GenericRelation(Favorite)

    def __str__(self):
        #return f"{self.title} at {self.tplace.name} on {self.date.strftime('%Y-%m-%d')}"
        return "event"

