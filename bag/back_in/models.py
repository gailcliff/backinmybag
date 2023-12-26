from django.db import models

# Create your models here.

DbModel = models.Model


class User(models.Model):

    user_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.user_name
