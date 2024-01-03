from django.db import models

class TPlace(models.Model):
    name = models.CharField(max_length=200)
    whatever = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
