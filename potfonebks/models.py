# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ContactCreate(models.Model):
    """ User add contact details."""
    name = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=10)
    phone = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=75, blank=True)
    address = models.TextField(blank=True)
    # image = models.ImageField(upload_to='uploads/', blank=True)
    owner = models.ForeignKey(User)
