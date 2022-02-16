from django.db import models
from django.utils.translation import gettext_lazy as _
from customer_support.constants import STATE_TYPES
import uuid

class BaseModel(models.Model):
    created = models.DateTimeField(
        verbose_name=_('Creation date'),
        auto_now_add=True,
        editable=False,
    )
    modified = models.DateTimeField(
        verbose_name=_('Update date'),
        auto_now=True,
        editable=False,
    )
    state = models.SmallIntegerField(
        verbose_name=_('Publish state'),
        choices=STATE_TYPES,
        default=1,
    )

    class Meta:
        abstract = True


class Chaser(BaseModel):
    message = models.CharField(
        verbose_name=_("message"),
        max_length=500,
    )
    time_delay = models.IntegerField(
        verbose_name=_("Time_Delay"),
    )

    def _send_sms(self):
        return 'sending the message'

    send_sm = property(_send_sms)

    class Meta:
        verbose_name = 'Chaser'
        verbose_name_plural = 'Chasers'


