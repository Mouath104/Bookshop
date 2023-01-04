from statistics import mode
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Books(models.Model):
    title= models.CharField(max_length=40)
    author= models.CharField(max_length=40)
    Desc=models.TextField()
    img=models.CharField(max_length=40)
    price=models.CharField(max_length=40)


class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT)

    #addtional Attrs
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username


class CartBooks(models.Model):
    book  = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
