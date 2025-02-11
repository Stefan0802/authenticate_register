from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Userprofile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)

    def __str__(self):
        return self.user.username

