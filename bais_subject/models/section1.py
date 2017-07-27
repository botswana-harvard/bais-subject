from django.db import models

from edc_base.model_fields import OtherCharField

from ..choices import (
    MALE_FEMALE,
    EDUCATION,
    EMPLOYMENT_STATUS,
    YES_NO,
    MINE_OCCUPATION,
    RELIGION,
    MARITAL_STATUS,
    SPOUSE_VISIT)


class Section1(models.Model):

    respondent_sex = models.CharField(
        verbose_name='Choose sex of the respondent',
        max_length=15,
        choices=MALE_FEMALE)

    respondent_age = models.IntegerField(
        verbose_name='How old are you in complete years?',
    )

    respondent_education = models.CharField(
        verbose_name='What is the highest level of education you have'
        ' completed? ',
        max_length=45,
        choices=EDUCATION
    )

    respondent_employment = models.CharField(
        verbose_name='What is your employment status?',
        max_length=45,
        choices=EMPLOYMENT_STATUS
    )

    respondent_employment_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    current_occupation = OtherCharField(
        verbose_name='What is your current occupation?',
        max_length=250
    )

    mine = models.CharField(
        verbose_name='Have you ever worked in the mine?',
        max_length=45,
        choices=YES_NO
    )

    mine_period = OtherCharField(
        verbose_name='For how long have you worked in the mine?',
        max_length=250,
        blank=True,
        null=True,
        help_text='specify'
    )

    mine_occupation = models.CharField(
        verbose_name='What was your occupation?',
        max_length=45,
        choices=MINE_OCCUPATION
    )

    mine_occupation_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    commodity = models.CharField(
        verbose_name='What is/was the type of the commodity mined?',
        max_length=45,
        choices=MINE_OCCUPATION
    )

    commodity_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    religion = models.CharField(
        verbose_name='What is/was the type of the commodity mined?',
        max_length=45,
        choices=RELIGION
    )

    religion_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    marital_status = models.CharField(
        verbose_name='What is your current marital status?',
        max_length=45,
        choices=MARITAL_STATUS
    )

    respondent_marriage_age = models.IntegerField(
        verbose_name='How old were you when you first married/started'
        ' living together?',
        help_text='AGE IN YEARS'
    )

    living_with_spouse = models.CharField(
        verbose_name='Does your husband/wife/partner live with you?',
        max_length=45,
        choices=YES_NO
    )

    spouse_visit = models.CharField(
        verbose_name='If no, how often do you see/visit each other?',
        max_length=45,
        choices=SPOUSE_VISIT
    )

    respondent_married_years = models.IntegerField(
        verbose_name='For how many years have you been married or '
        'living together? ',
        help_text='RECORD 00 IF LESS THAN ONE YEAR.'
    )

    class Meta:
        app_label = 'bais_subject'
