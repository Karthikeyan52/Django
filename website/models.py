from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserCreationForm


class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=False, blank=False, default='')
    contact = models.BigIntegerField()
    subject = models.CharField(max_length=200, default='')
    status = models.CharField(max_length=100, default='')
    comment = models.CharField(max_length=100, default='')
    object = models.Manager()

    class Meta:
        db_table = "Enquiry"
