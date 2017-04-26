from django.db import models

class Category(models.Model):
    name = models.CharField('nome', max_length=255)

