from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_mixins import BaseUuidModel

from .list_models import (
    CircumcissionReason,
    CircumcissionIntentReason,
    CircumcissionRejectReason,
    StiSymptoms)

from ..choices import (
    YES_NO_DNTKNW,
    CIRCUMICISSION_PLACE)


class MaleCircumcissionAndSexuallyTransmittedInfections(BaseUuidModel):

    circumcission = models.CharField(
        verbose_name='Are you circumcised?',
        max_length=45,
        choices=YES_NO_DNTKNW,
        blank=True,
        null=True
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
        blank=True,
        null=True
    )

    circumcission_place = models.CharField(
        verbose_name='Where were you circumcised?',
        max_length=45,
        choices=CIRCUMICISSION_PLACE,
        blank=True,
        null=True
    )

    circumcised_complications = models.CharField(
        verbose_name='Did you have any complications during or '
        'after circumcision?',
        max_length=45,
        choices=YES_NO_DNTKNW,
        blank=True,
        null=True
    )

    circumcission_intent = models.CharField(
        verbose_name='Do you intend to get circumcised in the next '
        '12 months?  ',
        max_length=45,
        choices=YES_NO_DNTKNW,
    )

    circumcission_intent_reason = models.ManyToManyField(
        CircumcissionIntentReason,
        verbose_name='Why would you want to get circumcised?',
        max_length=45,
        blank=True,
        null=True
    )

    circumcission_intent_reason_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    circumcission_reject_reason = models.ManyToManyField(
        CircumcissionRejectReason,
        verbose_name='Why would you want to get circumcised?',
        max_length=45,
        blank=True,
        null=True

    )

    circumcission_reject_reason_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    sti_symptoms = models.ManyToManyField(
        StiSymptoms,
        verbose_name='What signs and symptoms would lead you to '
        'think that a man or a woman has STIs? ',
        max_length=45,
        blank=True,
        null=True
    )

    sti_symptoms_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    class Meta(BaseUuidModel.Meta):
        app_label = 'bais_subject'
