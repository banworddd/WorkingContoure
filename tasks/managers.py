from django.db import models


class TaskDoneManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            status=self.model.TaskStatusChoices.DONE
        )

