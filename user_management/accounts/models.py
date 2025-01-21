from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255) 
    phone_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True) 
    is_super_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email
