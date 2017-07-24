from django.db import models

from edc_base.model_fields import OtherCharField

from ..choices import (YES_NO, TESTING_REASONS, TB_NONDISCLOSURE,
                       BABY_TEST)

# TODO: Youngest BabyDate


class Section7:

    given_birth = models.CharField(
        verbose_name='Have you ever given birth?',
        max_length=35,
        choices=YES_NO,
        null=True,
        blank=False
    )

    given_birth_past_5yrs = models.CharField(
        verbose_name='Have you given birth in the past 5 years?',
        max_length=35,
        choices=YES_NO,
        null=True,
        blank=False,
    )

    baby_dob = models.IntegerField(
        verbose_name='What is the date of birth of your youngest baby?',
        max_length=35,
        choices=YES_NO,
        null=True,
        blank=False,
    )

    baby_hiv_test = models.CharField(
        verbose_name='Was your baby tested for HIV'
        ' by the time he/she was 6 weeks to 18 months old? ',
        max_length=35,
        choices=BABY_TEST,
        null=True,
        blank=False,
    )
