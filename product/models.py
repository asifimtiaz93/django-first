from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=120)
    price=models.DecimalField(max_digits=100,decimal_places=2)
    description=models.TextField(default="This is cool",blank=False,null=False)