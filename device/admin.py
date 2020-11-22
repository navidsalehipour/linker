from django.contrib import admin
from .models import  Device
# Register your models here.


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'user',
        'is_active',
        'pending_count',
        'received_count',
        'downloaded_count',
    ]

    list_filter = [
        'user',
        'is_active',
    ]