from django.db import models
from users.models import Types

class Magazin(models.Model):
    title = models.CharField(max_length=40)
    name = models.CharField(max_length=20)
    adres = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    def __str__(self):
        return self.adres


class Shops(models.Model):
    title = models.CharField(max_length=20)
    discount = models.TextField()
    image = models.ImageField(upload_to="shop.html/shop.html/")
    project = models.ManyToManyField(Magazin)
    author = models.CharField(max_length=50)
    last_update = models.DateField(auto_now_add=True)
    create_data = models.DateField(auto_created=True)


    def __str__(self):
        return self.title