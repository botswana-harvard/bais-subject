from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_mixins import BaseUuidModel

from .list_models import CircumcissionReason

from ..choices import (
    YES_NO_DNTKNW,
    CIRCUMICISSION_PLACE,
    CIRCUMICISSION_INTENT_REASON,
    CIRCUMICISSION_REJECT_REASON,
    STI_SYMPTOMS,)


class Section4(BaseUuidModel):

    circumcission = models.CharField(
        verbose_name='Are you circumcised?',
        max_length=45,
        choices=YES_NO_DNTKNW,
    )

    circumcission_year = models.CharField(
        verbose_name='When were you circumcised?',
        max_length=45,
        blank=True,
        null=True,
        help_text='YEAR'
    )

    circumcission_reason = models.ManyToManyField(
        CircumcissionReason,
        verbose_name='Why were you circumcised?',
        max_length=45,
    )

    circumcission_place = models.CharField(
        verbose_name='Where were you circumcised?',
        max_length=45,
        choices=CIRCUMICISSION_PLACE,
    )

    circumcised_complications = models.CharField(
        verbose_name='Did you have any complications during or '
        'after circumcision?',
        max_length=45,
        choices=YES_NO_DNTKNW,
    )

    circumcission_intent = models.CharField(
        verbose_name='Do you intend to get circumcised in the next '
        '12 months?  ',
        max_length=45,
        choices=YES_NO_DNTKNW,
    )

    circumcission_intent_reason = models.CharField(
        verbose_name='Why would you want to get circumcised?',
        max_length=45,
        choices=CIRCUMICISSION_INTENT_REASON,
    )

    circumcission_intent_reason_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    circumcission_reject_reason = models.CharField(
        verbose_name='Why would you want to get circumcised?',
        max_length=45,
        choices=CIRCUMICISSION_REJECT_REASON,
    )

    circumcission_reject_reason_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    sti_symptoms = models.CharField(
        verbose_name='What signs and symptoms would lead you to '
        'think that a man or a woman has STIs? ',
        max_length=45,
        choices=STI_SYMPTOMS,
    )

    sti_symptoms_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    class Meta(BaseUuidModel.Meta):
        app_label = 'bais_subject'
