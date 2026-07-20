from django.db import models
from django.conf import settings
from projects.models import Project
from .managers import TaskDoneManager


class Task(models.Model):
    class TaskStatusChoices(models.TextChoices):
        TODO = 'TODO'
        IN_PROGRESS = 'IN_PROGRESS'
        DONE = 'DONE'

    title = models.CharField(max_length=250)
    description = models.TextField(
        blank=True
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks',
    )
    status = models.CharField(
        choices=TaskStatusChoices.choices,
        max_length=15,
        default=TaskStatusChoices.TODO,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_tasks',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    done = TaskDoneManager()

    def __str__(self):
        return self.title