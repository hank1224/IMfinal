from django.db import models

class lineUser(models.Model):
    sLineID=models.CharField(max_length=33, primary_key=True)
    sName=models.CharField(max_length=20, blank=False, null=True)
    sCity=models.CharField(max_length=3, blank=False, null=True)
    
    def __str__(self):
        return self.sLineID
    #讓object預設回傳 <lineUser: Uf496dcee2f5c542148d67e7a2a418a22>


# Create your models here.
