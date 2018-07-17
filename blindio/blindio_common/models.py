import uuid

from django.db import models


class AbstractEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_ts = models.DateTimeField(auto_now_add=True)
    update_ts = models.DateTimeField(auto_now=True)
    delete_ts = models.DateTimeField(null=True)

    class Meta:
        abstract = True
