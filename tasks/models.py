from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField("Created", auto_now_add=True)
    updated_at = models.DateTimeField("Updated", auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
