from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username= models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    friends = models.ManyToManyField('Friend')
    def __str__self():
        return {self.username}

class Friend(models.Model):
    profile = models.OneToOneField(Account, on_delete=models.CASCADE)
    
    def __str__(self):
        return {self.profile.name}
