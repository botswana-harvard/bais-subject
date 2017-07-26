from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_validators import date_not_future

from ..choices import (YES_NO, YES_NO_DNTKNW,
                       HELP_RECIEVED, HELP_RECIEVED_FROM, HELP_TYPE)


class HouseholdMember(models.Model):

    bedridden_member = models.CharField(
        verbose_name='Among the persons who are household members'
        ' of this household is there anybody who stayed for atleast '
        '3 months and bedridden for atleast 3months in the past 12months',
        max_length=35,
        choices=YES_NO,
    )

    member_age = models.IntegerField(
        verbose_name='How old is this person in completed years?',
        max_length=35,
        null=True,
        blank=False,
    )

    household_help = models.CharField(
        verbose_name='Has your household recieved any care or assistance'
        ' from outside in relation to the reported illnesses?',
        max_length=35,
        choices=YES_NO_DNTKNW,
        null=True,
        blank=False,
    )

    household_help_received = models.CharField(
        verbose_name='What kind of assistance did you recieve?',
        max_legth=35,
        choices=HELP_RECIEVED,
        null=True,
        blank=False,
    )

    household_help_received_other = OtherCharField(
        verbose_name='Other (Specify)',
        max_legth=35,
        null=True,
        blank=False,
    )

    household_help_received_from = models.CharField(
        verbose_name='Who provided the care or assistance?',
        max_legth=35,
        choices=HELP_RECIEVED_FROM,
        null=True,
        blank=False,
    )

    household_help_received_from_other = OtherCharField(
        verbose_name='Anyone else?',
        max_legth=35,
        null=True,
        blank=False,
    )

    household_illness = models.CharField(
        verbose_name='In the past 12 months have any gaurdians/children '
        'been continously ill for atleast 3 months',
        max_length=35,
        choices=YES_NO,
    )

    household_illness = models.CharField(
        verbose_name='In the past 12 months has your household recieved  any help or support specifically for'
        'children living with sick parents/gaurdians ',
        max_length=35,
        choices=YES_NO_DNTKNW,
    )

    household_illness_help = models.CharField(
        verbose_name='What kind of help or support did you recieve? ',
        max_length=35,
        choices=HELP_TYPE,
    )

    household_illness_help_other = OtherCharField(
        verbose_name='Other (Specify) ',
        max_length=35,
        null=True,
        blank=False,
    )
