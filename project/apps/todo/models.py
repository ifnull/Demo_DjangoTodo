from django.db import models


class Todo(models.Model):

    title = models.CharField(max_length=155)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
