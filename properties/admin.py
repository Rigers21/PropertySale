from django.contrib import admin
from .models import Property, Picture


class PicturesInLine(admin.TabularInline):
    model = Picture
    max_num = 20


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'location', 'city']
    prepopulated_fields = {
        'slug': ('title', )
    }
    inlines = [PicturesInLine]
