from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_validators import date_not_future

from ..choices import (HOUSEHOLD_RELATION)


class HouseholdMember(models.Model):

    household_relationship = models.CharField(
        verbose_name='What is relationship to head of this household?',
        max_legth=35,
        choices=HOUSEHOLD_RELATION,
    )

    household_relationship = models.CharField(
        verbose_name='What is relationship to head of this household?',
        max_legth=35,
        choices=HOUSEHOLD_RELATION,
    )
