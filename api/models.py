from django.db import models

class TPlace(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Photo(models.Model):
    tplace = models.ForeignKey(TPlace, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')

