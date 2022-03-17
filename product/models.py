from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    sale_price = models.FloatField()
    purchase_price = models.FloatField()
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField()
    sell_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "PRODUCT"