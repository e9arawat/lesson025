from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    linkedin = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contact")
    
    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return reverse("Contact_details", kwargs={"pk": self.pk})
            
