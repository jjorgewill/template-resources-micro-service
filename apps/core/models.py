from django.db import models


class Profile(models.Models):
    address = models.TextField(blank=True)
    token = models.CharField(blank=True,null=True,max_length=256)
    user_id = models.IntegerField(blank=False, null=False)


class Company(models.Model):
    address = models.TextField(blank=True)
    name = models.CharField(blank=True,null=True,max_length=256)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)