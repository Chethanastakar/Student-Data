from django.db import models

# Create your models here.
class Student4(models.Model):
    sid=models.IntegerField(max_length=20,primary_key=True)
    sname=models.CharField(max_length=30)
    sbranch=models.CharField(max_length=30)
    telugu=models.IntegerField(max_length=3)
    hindi = models.IntegerField(max_length=3)
    english = models.IntegerField(max_length=3)
    mathes = models.IntegerField(max_length=3)
    science = models.IntegerField(max_length=3)
    social= models.IntegerField(max_length=3)
    total=models.IntegerField(max_length=5)
    sperc=models.DecimalField(max_digits=4,decimal_places=2)
    result=models.CharField(max_length=100)



    #smarks=models.IntegerField(max_length=4)
    #sperc=models.FloatField(max_length=5)
    #srank=models.CharField(max_length=20)
