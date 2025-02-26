from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    title=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    success=models.CharField(max_length=4)

    def __str__(self):
        return self.title