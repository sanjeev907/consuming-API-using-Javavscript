from django.db import models

# Create your models here.
status = [('pending','pending'),('complete','complete'),('cancel','cancel')]
status1 = [('pending','pending'),('complete','complete'),('cancel','cancel')]


class Patient(models.Model):
     name = models.CharField(max_length=100)
     age = models.IntegerField()
     test = models.CharField(max_length=100)
     B2B_price = models.IntegerField()
     status = models.CharField(max_length=50,choices=status,default='pending')
     B2C_price = models.IntegerField()
     B2C_Status = models.CharField(max_length=50,choices=status1,default='pending')
     # date = models.DateField(blank=True, null=True)

     def __str__(self):
         return self.name
     