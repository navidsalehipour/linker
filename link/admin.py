from django.contrib import admin
from .models import  Link
# Register your models here.

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'user',
        'device',
        'status',
        'created_at',
        'updated_at'
    ]

    list_filter = [
        'user',
        'device',
        'status',
        'created_at'
    ]