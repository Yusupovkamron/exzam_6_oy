from django.db import models
from django.contrib.auth.models import User




class Shop_Detail(models.Model):
    title = models.CharField(max_length=20)
    discount = models.TextField()
    image = models.ImageField(upload_to="shop-detail.html/shop-detail.html/")
    author = models.CharField(max_length=30)
    last_update = models.DateField(auto_now_add=True)
    create_data = models.DateField(auto_created=True)


    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_detail = models.ManyToManyField(Shop_Detail)

    def __str__(self):
        return self.user
