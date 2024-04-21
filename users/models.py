from django.db import models



class Types(models.Model):
    class PriceType(models.TextChoices):
        s = '$', '$'
        sum = "som", "som"
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="types/types/")
    description = models.TextField()
    price = models.FloatField()
    price_type = models.CharField(max_length=15, choices=PriceType.choices, default=PriceType.sum)
    def __str__(self):
        return self.price

class Vegetables_new(models.Model):
    class PriceesType(models.TextChoices):

        s = '$', '$'
        sum = "som", "som"
    image = models.ImageField(upload_to="vegetables_new/vegetables_new/")
    description = models.TextField()
    price_type = models.CharField(max_length=15, choices=PriceesType.choices, default=PriceesType.sum)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    x_link = models.URLField(null=True, blank=False)
    m_link = models.ManyToManyField(Types, choices=PriceesType.choices, default=PriceesType.s)
    create_data = models.DateField(auto_created=True)
    last_update = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.m_link


class Discounts(models.Model):
    image = models.ImageField(upload_to="discounts/discounts/")
    description = models.TextField()
    name = models.CharField(max_length=20)
    discount_price = models.FloatField()
    product = models.ManyToManyField(Types)

    def __str__(self):
        return self.description


class Products(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    type = models.CharField(max_length=20)
    image = models.ImageField(upload_to="discount/products/", null=True)
    create_data = models.DateField(auto_created=True)
    last_update = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

