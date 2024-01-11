from django.db import models
from django.contrib.auth.models import User

class Customer(models.MOdel):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    phone = models.TextField(max_length = 10, unique=True, null=False, blank = False)
    email = models.CharField(max_length = 35, unique = True, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def username(self):
        return self.user.username if self.user else None
