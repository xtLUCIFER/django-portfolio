from django.db import models

# Create your models here.


class Info(models.Model):
    experience = models.CharField(max_length=6)
    projects = models.CharField(max_length=6)
    company = models.CharField(max_length=6)


    def __str__(self):
        return self.projects

class Projects(models.Model):
    title = models.CharField(max_length=500)
    photo = models.ImageField()
    text = models.TextField()

    def __str__(self):
        return self.title
    

    