from django.db import models
from accounts.models import User
from device.models import Device


# Create your models here.

class Link(models.Model):
    """ download links """
    # status lists
    STATUS_TYPE = (
        ("0", "pending"),
        ("1", "received"),
        ("2", "downloaded"),
    )

    user = models.ForeignKey(User, related_name="ulink", on_delete=models.CASCADE, verbose_name="user")
    device = models.ForeignKey(Device, related_name="dlink", on_delete=models.CASCADE, verbose_name="device")
    title = models.CharField(max_length=255, verbose_name="link title")
    url = models.TextField(verbose_name="download link")
    status = models.CharField(max_length=1, default="0", choices=STATUS_TYPE, verbose_name="link status")

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="created date")
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="update date")


    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = "link"
        verbose_name_plural = "links"
