from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_text


# Create your models here.

class Movie(models.Model):
    number = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    date = models.CharField(max_length=1000)

    def str_title(self):
        return smart_text(self.title, encoding='utf-8', strings_only=False, errors='strict')
