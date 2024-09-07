from enum import unique
from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "bronze"),
        (MEMBERSHIP_SILVER, "silver"),
        (MEMBERSHIP_GOLD, "gold"),
    ]
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(max_length=255)
    birth_rate = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default="MEMBERSHIP_BRONZE"
    )


class Order(models.Model):
    PENDING = "P"
    COMPLETE = "C"
    FAILED = "F"
    PAYMENT_CHOICES_STATUS = [
        (PENDING, "pending"),
        (COMPLETE, "complete"),
        (FAILED, "failed"),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_CHOICES_STATUS, PENDING="P"
    )


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer, primary_key=True, on_delete=models.CASCADE
    )
