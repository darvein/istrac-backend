from django.contrib import admin
from .models import TPlace, Category, Event, Photo, Video, Comment, Like, Favorite

# Register your models here.
admin.site.register(TPlace)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Favorite)
