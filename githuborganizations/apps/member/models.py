from django.db import models
from apps.organization.models import Organizations


class Members(models.Model):
    login = models.CharField(max_length=50, default=None)
    avatar_url = models.URLField()
    html_url = models.URLField(default=None)
    organization = models.ForeignKey(
        Organizations,
        default=None,
        on_delete=models.CASCADE
    )
