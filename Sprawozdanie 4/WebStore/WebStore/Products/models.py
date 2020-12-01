from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    price = models.FloatField()
    in_stock = models.IntegerField()

    def __string__(self):
        return self.name

