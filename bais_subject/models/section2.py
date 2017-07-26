from django.db import models

from edc_base.model_fields import OtherCharField

from ..choices import (
    YES_NO,
    METHODS_OF_USE,
    SUBSTANCE_FREQUENCY)


class Section2(models.Model):

    #    TODO: Make this an inline form

    taken_alcohol = models.CharField(
        verbose_name='Have you taken any Alcohol',
        max_length=5,
        choices=YES_NO,
        help_text='Alcohol'
    )

    substance_method = models.CharField(
        verbose_name='Method of use',
        max_length=15,
        choices=METHODS_OF_USE,
    )

    substance_age = models.IntegerField(
        verbose_name='Age at First Use',
        max_length=15,
    )

    substance_frequency = models.CharField(
        verbose_name='During the past 12 months, how frequently have '
        'you had the following substance?',
        max_length=15,
        choices=SUBSTANCE_FREQUENCY,
    )

    taken_tobacco = models.CharField(
        verbose_name='Have you taken any Tobacco',
        max_length=5,
        choices=YES_NO,
        help_text='Tobacco'
    )

    substance_age = models.IntegerField(
        verbose_name='Age at First Use',
        max_length=15,
    )

    taken_marijuana = models.CharField(
        verbose_name='Have you taken any of the following SUBSTANCE?',
        max_length=5,
        choices=YES_NO,
        help_text='Marijuana'
    )

    substance_age = models.IntegerField(
        verbose_name='Age at First Use',
        max_length=15,
    )

    substance_frequency = models.CharField(
        verbose_name='During the past 12 months, how frequently have '
        'you had the following substance?',
        max_length=15,
        choices=SUBSTANCE_FREQUENCY,
    )

    taken_cocaine = models.CharField(
        verbose_name='Have you taken any Cocaine',
        max_length=5,
        choices=YES_NO,
        help_text='Cocaine'
    )

    substance_age = models.IntegerField(
        verbose_name='Age at First Use',
        max_length=15,
    )

    substance_frequency = models.CharField(
        verbose_name='During the past 12 months, how frequently have '
        'you had the following substance?',
        max_length=15,
        choices=SUBSTANCE_FREQUENCY,
    )

    taken_crack_cocaine = models.CharField(
        verbose_name='Have you taken any Crack Cocaine',
        max_length=5,
        choices=YES_NO,
        help_text='Crack Cocaine'
    )

    substance_age = models.IntegerField(
        verbose_name='Age at First Use',
        max_length=15,
    )

    substance_frequency = models.CharField(
        verbose_name='During the past 12 months, how frequently have '
        'you had the following substance?',
        max_length=15,
        choices=SUBSTANCE_FREQUENCY,
    )

    taken_methcathinone = models.CharField(
        verbose_name='Have you taken any Methcathinone',
        max_length=5,
        choices=YES_NO,
        help_text='Methcathinone'
    )

    substance_age = models.IntegerField(
        verbose_name='Age at First Use',
        max_length=15,
    )

    substance_frequency = models.CharField(
        verbose_name='During the past 12 months, how frequently have '
        'you had the following substance?',
        max_length=15,
        choices=SUBSTANCE_FREQUENCY,
    )

    taken_nyaope = models.CharField(
        verbose_name='Have you taken any Nyaope',
        max_length=5,
        choices=YES_NO,
        help_text='Nyaope'
    )

    substance_age = models.IntegerField(
        verbose_name='Age at First Use',
        max_length=15,
    )

    substance_frequency = models.CharField(
        verbose_name='During the past 12 months, how frequently have '
        'you had the following substance?',
        max_length=15,
        choices=SUBSTANCE_FREQUENCY,
    )

    taken_heroine = models.CharField(
        verbose_name='Have you taken any Heroine',
        max_length=5,
        choices=YES_NO,
        help_text='Heroine'
    )

    substance_age = models.IntegerField(
        verbose_name='Age at First Use',
        max_length=15,
    )

    substance_frequency = models.CharField(
        verbose_name='During the past 12 months, how frequently have '
        'you had the following substance?',
        max_length=15,
        choices=SUBSTANCE_FREQUENCY,
    )

    taken_ecstasy = models.CharField(
        verbose_name='Have you taken any Ecstasy (MDMA)',
        max_length=5,
        choices=YES_NO,
        help_text='Ecstasy (MDMA)'
    )

    taken_codeine = models.CharField(
        verbose_name='Have you taken any Codeine',
        max_length=5,
        choices=YES_NO,
        help_text='Codeine'
    )

    substance_age = models.IntegerField(
        verbose_name='Age at First Use',
        max_length=15,
    )

    substance_frequency = models.CharField(
        verbose_name='During the past 12 months, how frequently have '
        'you had the following substance?',
        max_length=15,
        choices=SUBSTANCE_FREQUENCY,
    )

    substance_other = OtherCharField(
        verbose_name='Other: ',
        max_length=250,
        blank=True,
        null=True,
        help_text='specify'
    )

#   End of inline form

    passive_smoke = models.CharField(
        verbose_name='During the past 7 days, on how many days did '
        'someone smoke around you?',
        max_length=15,
        blank=True,
        null=True,
    )

    message = models.CharField(
        verbose_name='In the past 12 months have you ever seen or '
        'heard any anti-alcoholic messages?',
        max_length=15,
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'bais_subject'
