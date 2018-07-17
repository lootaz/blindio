from django.db import models

from blindio_common.models import AbstractEntity


class FSItem(AbstractEntity):
    path = models.CharField(max_length=1024)

    class Meta:
        db_table = 'blindio_fsitem'


class Study(models.Model):
    start_ts = models.DateTimeField(null=True)
    finish_ts = models.DateTimeField(null=True)
    state = models.CharField(max_length=255, null=True)

    fs_item = models.ForeignKey(
        "FSItem",
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        db_table = 'blindio_study'
