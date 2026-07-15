from django.db import models
from django.conf import settings


class Project(models.Model):
    class ProjectStatusChoices(models.TextChoices):
        ACTIVE = 'ACTIVE'
        ARCHIVED = 'ARCHIVED'

    name = models.CharField(max_length=250)
    description = models.TextField(
        blank=True
    )
    status = models.CharField(
        choices=ProjectStatusChoices.choices,
        max_length=10,
        default=ProjectStatusChoices.ACTIVE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


