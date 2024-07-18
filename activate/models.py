from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class ActivateLog(models.Model):
    user = models.ForeignKey(User, related_name='activate_user',on_delete=models.SET_NULL, null=True, blank=True)
    method = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{str(self.user)} - {self.method}"
