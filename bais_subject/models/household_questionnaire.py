from django.db import models

from edc_base.model_fields import OtherCharField

from ..choices import (
    MALE_FEMALE,
    MARITAL_STATUS,
    YES_NO_DNTKNW,
    YES_NO,
    HOUSEHOLD_RELATION,
    CITIZENSHIP,
    PERSON_HOUSEHOLD_LIVE,
    ATTENDED_SCHOOL,
    STUDY_LEVEL,
    UNPAID_REASON,
    MAIN_WORK)


class HouseholdQuestionnaire(models.Model):

    persons_list = models.CharField(
        verbose_name='Please give me names of all persons who slept '
        'with this household last night.',
        max_length=50,
    )

    person_household_head_rel = models.CharField(
        verbose_name='What is the person\'s relationship to head '
        'of this household?',
        max_length=45,
        choices=HOUSEHOLD_RELATION,
    )

    person_gender = models.CharField(
        verbose_name='What is the person\'s relationship to head '
        'of this household?',
        max_length=45,
        choices=MALE_FEMALE,
    )

    person_age = models.CharField(
        verbose_name='How old is the person in completed years?',
        max_length=45,
        help_text='RECORD EXACT AGE IN YEARS AND MONTHS FOR THOSE '
        'LESS THAN YEARS IN THE FORMAT( YY MM)',
    )

    person_citizenship = models.CharField(
        verbose_name='What is the country of person\'s citizenship?',
        max_length=45,
        choices=CITIZENSHIP,
    )

    person_citizenship_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    person_household_live = models.CharField(
        verbose_name='Does the person usually live in this household?',
        max_length=45,
        choices=PERSON_HOUSEHOLD_LIVE,
    )

    person_marital_status = models.CharField(
        verbose_name='What is the person\'s current marital status?',
        max_length=45,
        choices=MARITAL_STATUS,
    )

    person_biological_mother_alive = models.CharField(
        verbose_name='Is the person\'s biological mother alive?',
        max_length=45,
        choices=YES_NO_DNTKNW,
    )

    person_biological_mother_household_live = models.CharField(
        verbose_name='Does the person\'s biological mother usually '
        'live in this household?',
        max_length=45,
        choices=YES_NO_DNTKNW,
    )

    person_biological_father_alive = models.CharField(
        verbose_name='Is the person\'s biological father alive?',
        max_length=45,
        choices=YES_NO_DNTKNW,
    )

    person_biological_father_household_live = models.CharField(
        verbose_name='Does the person\'s biological father usually '
        'live in this household?',
        max_length=45,
        choices=YES_NO_DNTKNW,
    )

    person_attended_school = models.CharField(
        verbose_name='Has the person ever attended school?',
        max_length=45,
        choices=ATTENDED_SCHOOL,
    )

    person_currently_studying = models.CharField(
        verbose_name='What level or grade is the person '
        'currently studying?',
        max_length=45,
        choices=STUDY_LEVEL,
    )

    person_highest_study_level = models.CharField(
        verbose_name='What is the highest level that the person '
        'has completed?',
        max_length=45,
        choices=STUDY_LEVEL,
    )

    person_work_profit = models.CharField(
        verbose_name='In the past 7 days did the person work for '
        'payment, profit or home use for at least 1 hour?',
        max_length=45,
        choices=YES_NO,
    )

    person_work_unpaid = models.CharField(
        verbose_name='Has the person worked unpaid at own '
        'lands/cattlepost, or unpaid in family business?',
        max_length=45,
        choices=YES_NO,
    )

    person_work_unpaid_reason = models.CharField(
        verbose_name='Since the person did not work for payment, '
        'profit or home use, what did he/she do?',
        max_length=45,
        choices=UNPAID_REASON,
    )

    person_work_unpaid_reason_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    person_main_work = models.CharField(
        verbose_name='What was the person\'s mainly working as '
        'during the past 7 days?',
        max_length=45,
        choices=MAIN_WORK,
    )

    person_work_type = models.CharField(
        verbose_name='What type of work did the person do in the '
        'past 7 days?',
        max_length=145,
        help_text='To be precise, what were the main tasks and '
        'duties?',
    )

    person_work_product = models.CharField(
        verbose_name='What was the main product, service or activity '
        'at the person\'s place of work?',
        max_length=145,
        help_text='Probe as necessary.  Use two or more words to '
        'describe the Industry.',
    )

    class Meta:
        app_label = 'bais_subject'
