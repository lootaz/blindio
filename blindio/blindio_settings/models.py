from django.db import models

from blindio_common.models import AbstractEntity


class Setting(AbstractEntity):
    name = models.CharField(max_length=512, unique=True)
    label = models.CharField(max_length=512, blank=True)
    value = models.CharField(max_length=1024, blank=True)

    class Meta:
        db_table = 'blindio_setting'
