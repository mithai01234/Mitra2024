
from django.db import models

from registration.models import CustomUser
from django.utils import timezone
from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

class Statusapp(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='videos/')
    caption = models.TextField(default='')
    # uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now)
    expiration_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(minutes=2))

    status = models.BooleanField(default=True)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     # Calculate the cutoff time (24 hours ago)
    #     cutoff_time = timezone.now() - timedelta(minutes=1)
    #
    #     # Delete objects older than cutoff_time
    #     Statusapp.objects.filter(uploaded_at__lt=cutoff_time).delete()

    def __str__(self):
        return str(self.id)
