from operator import mod
from tkinter import N
from tkinter.tix import Tree
from django.db import models
from pyrsistent import b

# Create your models here.
class StudentInfo(models.Model):
    Roll_no = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30, blank=True, null= True)
    Class= models.CharField(max_length=4,blank=True,null=True)
    School=models.CharField(max_length=40, blank=True, null=True)
    Mobile=models.BigIntegerField()
    Address=models.CharField(max_length=40,blank=True,null=True)


class StudentAcadamics(models.Model):
    Roll_no=models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    Maths=models.IntegerField()
    Physics=models.IntegerField()
    Chemistry=models.IntegerField()
    Biology=models.IntegerField()
    English=models.IntegerField()