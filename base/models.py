from django.db import models
from .manager import ActiveManager, DeletedManager


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        abstract = True
        ordering = ['-created_date']


