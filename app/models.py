from django.db import models

# Create your models here.


class UserType(models.Model):
    id = models.IntegerField(unique=True)
    name = models.CharField(max_length=32, primary_key=True)


class User(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    ut = models.ForeignKey(to='UserType', to_field='id', on_delete=True)



