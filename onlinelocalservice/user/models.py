from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=20)

    class Meta():
        db_table = 'customer'

class ServiceProvider(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    website = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta():
        db_table = 'service_provider'