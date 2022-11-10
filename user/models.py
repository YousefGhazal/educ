from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
            return self.title

class Course(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True,blank=True)
    modules = models.IntegerField(default=0)
    hours = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
