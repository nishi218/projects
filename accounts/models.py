from django.db import models
from django.urls import reverse
# Create your models here.

import uuid


class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=10)
    username = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name}, {self.last_name}'
