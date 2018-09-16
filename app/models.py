from django.db import models

# Create your models here.


class UserType(models.Model):
    type_name = models.CharField(max_length=32)

    def __str__(self):
        return self.type_name


class User(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, db_index=True)
    password = models.CharField(max_length=32, db_index=True)
    email = models.EmailField(max_length=64)
    ut = models.ForeignKey(to='UserType', to_field='id', on_delete=True)

