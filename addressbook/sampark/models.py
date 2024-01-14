from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=10)
    linkedin = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.id)
    
            
