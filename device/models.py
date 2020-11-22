from django.db import models
from accounts.models import  User
# Create your models here.


class Device(models.Model):
    """ device list """
    user = models.ForeignKey(User, related_name="udevice", verbose_name="user", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="device title")
    is_active = models.BooleanField(default=True, verbose_name="is device active")


    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="created date")
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="update date")



    def pending_count(self):
        """ this device pending link count"""
        return  self.dlink.filter(status = "0").count()

    def received_count(self):
        """ this device received link count"""
        return  self.dlink.filter(status = "1").count()

    def downloaded_count(self):
        """ this device downloaded link count"""
        return  self.dlink.filter(status = "2").count()


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "device"
        verbose_name_plural = "Devices"

