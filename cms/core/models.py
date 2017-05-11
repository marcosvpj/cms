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
    # cards = models.ForeignKey('Card', on_delete=models.SET_NULL, blank=True, null=True, related_name='card')

    def __str__(self):
        return self.name

    @property
    def cards(self):
        return Card.objects.filter(parent=self.id)


class Card(models.Model):
    name = models.CharField('nome', max_length=100)
    title = models.CharField('titulo', max_length=255)
    subtitle = models.CharField('subtitulo', max_length=255)
    content = models.TextField('conteudo', blank=True)
    position = models.IntegerField('posicao')
    parent = models.ForeignKey(Content, on_delete=models.CASCADE)
    slug = models.SlugField('slug')

    def __str__(self):
        return self.name