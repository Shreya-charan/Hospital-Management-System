from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you need
    pass

class Department(models.Model):
    id = models.CharField(max_length = 6 , primary_key = True, default = 'ABC123')
    name = models.CharField(max_length = 20)

    def __str__(self): 
        return self.name
    

class Doctor(models.Model):
    d_id = models.CharField(max_length=6, primary_key = True, default="ABC123")
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default = 'ABC123')

    
    def __str__(self):
        return self.name


class Patient(models.Model):
    p_id = models.CharField(max_length=6, primary_key = True, default='ABC123')
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    disease = models.CharField(max_length=255)
    treatment = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

