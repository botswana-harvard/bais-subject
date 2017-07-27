from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_validators import date_not_future

from ..choices import (YES_NO, YES_NO_DONTWANT,
                       BABY_TEST, BABY_TEST_RESULT, BABY_FEEDING,
                       ANTE_NATAL_REASONS, ANTE_NATAL_TEST_RESULT)

# TODO: Youngest BabyDate


class Section7(models.Model):

    given_birth = models.CharField(
        verbose_name='Have you ever given birth?',
        max_length=35,
        choices=YES_NO,
        null=True,
        blank=True
    )

    given_birth_past_5yrs = models.CharField(
        verbose_name='Have you given birth in the past 5 years?',
        max_length=35,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    baby_dob = models.DateField(
        verbose_name='What is the date of birth of your youngest baby?',
        validators=[date_not_future],
    )

    baby_hiv_test = models.CharField(
        verbose_name='Was your baby tested for HIV'
        ' by the time he/she was 6 weeks to 18 months old? ',
        max_length=35,
        choices=BABY_TEST,
        null=True,
        blank=True,
    )

    baby_hiv_test_result = models.CharField(
        verbose_name='What was the result of your baby’s HIV test? ',
        max_length=35,
        choices=BABY_TEST_RESULT,
        null=True,
        blank=True,
    )

    baby_arv = models.CharField(
        verbose_name='Did your baby recieve ARVs?',
        max_length=35,
        choices=YES_NO_DONTWANT,
        null=True,
        blank=True,
    )

    baby_feeding = models.CharField(
        verbose_name='How did you feed your baby in the first 6months?',
        max_length=35,
        choices=BABY_FEEDING,
        null=True,
        blank=True,
    )

    currently_pregnant = models.CharField(
        verbose_name='Are you currently pregnant?',
        max_length=35,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    ante_natal_clinic = models.CharField(
        verbose_name='Are you attending an antenatal clinic for this pregnancy?',
        max_length=35,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    ante_natal_clinic_other = OtherCharField(
        verbose_name='If not, why? ',
        max_length=35,
        choices=ANTE_NATAL_REASONS,
        null=True,
        blank=True,
    )

    ante_natal_clinic_test = models.CharField(
        verbose_name='Were you tested for HIV during'
        ' your visit to the antenatal clinic? ',
        max_length=35,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    ante_natal_clinic_test_other = OtherCharField(
        verbose_name=' What was the result of your HIV test? ',
        max_length=35,
        choices=ANTE_NATAL_TEST_RESULT,
        null=True,
        blank=True,
    )

    ante_natal_clinic_partner_test = models.CharField(
        verbose_name='Has your partner tested for HIV during this pregnancy? ',
        max_length=35,
        choices=YES_NO,
        null=True,
        blank=True,
    )

    ante_natal_clinic_partner_test = OtherCharField(
        verbose_name='What was the result of your partner’s HIV test?',
        max_length=35,
        choices=ANTE_NATAL_TEST_RESULT,
        null=True,
        blank=True,
    )

    class Meta:
        app_label = 'bais_subject'
