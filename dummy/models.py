import turtle
from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=20)
    phone = models.IntegerField(max_length=20)
    address = models.TextField(max_length=100)
class TODOS(models.Model):
    title = models.CharField(max_length=50)
    contnt = models.TextField(max_length=250)
    completed = models.BooleanField(default=False)
class Product(models.Model):
    product_ID = models.IntegerField(max_length=4,primary_key= True,null=False)
    product_name = models.CharField(max_length=20)
    company_name = models.TextField(blank=True,null=True)
    company_email = models.EmailField(max_length=20)
    company_contact = models.IntegerField(max_length=13)
