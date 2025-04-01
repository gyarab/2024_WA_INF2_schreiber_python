from django.contrib import admin

# Register your models here.

from .models import Article, Dimension, Nature

admin.site.register(Article)
admin.site.register(Dimension)
admin.site.register(Nature)

