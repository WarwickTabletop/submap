import random
import string

from django.db import models


def new_key():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(128))


def new_url():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(64))


# Create your models here.
class Map(models.Model):
    map = models.TextField()
    slug = models.CharField(max_length=128, default=new_url, unique=True, auto_created=True)


class APIKey(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=128, default=new_key, unique=True, auto_created=True)
