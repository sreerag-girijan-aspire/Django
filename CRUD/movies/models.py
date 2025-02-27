from django.db import models

# Create your models here.
class DirectorInfo(models.Model):
    name=models.CharField(max_length=50)
    num_of_movies=models.IntegerField()
    def __str__(self):
        return self.name


class MovieInfo(models.Model):
    title=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    success=models.CharField(max_length=4)
    director=models.ForeignKey(DirectorInfo,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.title
    
class Actor(models.Model):
    name=models.CharField(max_length=50)
    movie=models.ManyToManyField(MovieInfo)
