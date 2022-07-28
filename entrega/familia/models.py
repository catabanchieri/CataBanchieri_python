from django.db import models

# Create your models here.
class family_members(models.Model):
    relation=models.CharField(max_length=20)
    name=models.CharField(max_length=20,default=True)
    age=models.IntegerField()
    date=models.DateField(auto_now_add=True,null=True, blank=True)
    gender=models.CharField(max_length=15,null=True, blank=True)

