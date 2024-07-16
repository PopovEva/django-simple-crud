from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50, null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    createdTime = models.DateTimeField(auto_now_add=True)
    desc = models.TextField(null=True, blank=True)  # Add this line to define the desc attribute
    
    def __str__(self):
        return self.desc
