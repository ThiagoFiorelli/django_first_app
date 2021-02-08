from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=255, null=True)


class Sport(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=255, null=True)


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=255, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)


class Customer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    num_doc = models.CharField(max_length=100, null=False, blank=False, unique=True)
    phone = models.CharField(max_length=20, null=True)