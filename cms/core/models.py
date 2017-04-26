from django.db import models


class Category(models.Model):
    name = models.CharField('nome', max_length=100)


class Tag(models.Model):
    name = models.CharField('nome', max_length=100)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)


class Content(models.Model):
    name = models.CharField('nome', max_length=100)
    title = models.CharField('titulo', max_length=255)
    content = models.TextField('conteudo', blank=True)
    position = models.IntegerField('posicao')
    is_listable = models.IntegerField('listavel')
    tags = models.ManyToManyField(Tag)


class Card(models.Model):
    name = models.CharField('nome', max_length=100)
    title = models.CharField('titulo', max_length=255)
    subtitle = models.CharField('subtitulo', max_length=255)
    content = models.TextField('conteudo', blank=True)
    position = models.IntegerField('posicao')
    parent = models.ForeignKey(Content, on_delete=models.CASCADE)
