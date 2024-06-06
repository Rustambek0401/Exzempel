from django.db import models

# Create your models here.
class Customers(models.Model):
    first_name = models.CharField(max_length=300,null=True,blank=True)
    last_name = models.CharField(max_length=300,null=True,blank=True)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images')
    # address = models.CharField(max_length=300 )
    joined = models.DateTimeField(auto_now  =True)
    # address = models.ForeignKey('app.Address',on_delete=models.CASCADE, related_name='Address')

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'

class Address(models.Model):
    address = models.CharField(max_length=300)
    customers = models.ForeignKey('app.Customers', on_delete=models.CASCADE, related_name='Address')
