from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    publish_date = models.DateField(default=datetime.date.today)
