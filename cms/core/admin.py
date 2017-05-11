from django.contrib import admin
from .models import Card, Content, Tag


class ContentModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Content, ContentModelAdmin)


class TagModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Tag, TagModelAdmin)


class CardModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Card, CardModelAdmin)
