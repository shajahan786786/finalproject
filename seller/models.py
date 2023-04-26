from django.db import models

from common.models import Seller
 
# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    prod_name = models.CharField(max_length=100)
    prod_des = models.CharField(max_length=500)
    prod_stock = models.BigIntegerField()
    prod_price = models.FloatField()
    prod_image = models.ImageField(upload_to='product/')


    class Meta:
        db_table = "products"