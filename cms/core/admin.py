from django.contrib import admin
from .models import Card, Content, Tag

# Register your models here.
admin.site.register(Card)
admin.site.register(Content)


class TagModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Tag, TagModelAdmin)
