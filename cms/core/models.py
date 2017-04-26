from django.db import models


class Tag(models.Model):
    name = models.CharField('nome', max_length=100)
    parent = models.ManyToManyField('self', blank=True)
    slug = models.SlugField('slug')

    def __str__(self):
        return self.name


class Content(models.Model):
    name = models.CharField('nome', max_length=100)
    title = models.CharField('titulo', max_length=255)
    content = models.TextField('conteudo', blank=True)
    position = models.IntegerField('posicao')
    is_listable = models.IntegerField('listavel')
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField('slug')


class Card(models.Model):
    name = models.CharField('nome', max_length=100)
    title = models.CharField('titulo', max_length=255)
    subtitle = models.CharField('subtitulo', max_length=255)
    content = models.TextField('conteudo', blank=True)
    position = models.IntegerField('posicao')
    parent = models.ForeignKey(Content, on_delete=models.CASCADE)
    slug = models.SlugField('slug')
