from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    address = models.TextField()
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)  
    salary = models.PositiveIntegerField()
    department = models.CharField(max_length=50)  
    qualification = models.CharField(max_length=100,null=True)

    def __str__(self):

        return self.name
