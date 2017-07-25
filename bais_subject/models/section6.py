from django.db import models

from edc_base.model_fields import OtherCharField

from ..choices import (YES_NO, TESTING_REASONS, TB_NONDISCLOSURE)


class Section6(models.Model):

    meal_sharing = models.CharField(
        verbose_name='Would you ever share a meal (from the same plate)'
        ' with a person you knew or suspected had HIV AND AIDS?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    household_care = models.CharField(
        verbose_name='If a member of your family became sick with HIV AND AIDS,'
        ' would you be willing to care for him or her in your household?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    aids_household_care = models.CharField(
        verbose_name='If a member of your family became sick with HIV AND AIDS,'
        ' would you be willing to care for him or her in your household?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_household_care = models.CharField(
        verbose_name='If a member of your family got diagnosed with TB,'
        ' would you be willing to care for him or her in your household?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    aids_housekeeper = models.CharField(
        verbose_name='If your housekeeper, nanny or anybody looking'
        ' after your child has HIV but is not sick, '
        'would you allow him/her to continue'
        ' working/assisting with babysitting in your house? ',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    aids_teacher = models.CharField(
        verbose_name='If a teacher has HIV but is not sick,'
        ' should s/he be allowed to continue teaching in school?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    aids_shopkeeper = models.CharField(
        verbose_name='If you knew that a shopkeeper or food seller had'
        ' HIV or AIDS, would you buy vegetables from them?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    aids_family_member = models.CharField(
        verbose_name='If a member of your family got infected'
        'with HIV, would you want it to remain a secret?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    aids_children = models.CharField(
        verbose_name='Do you think that children living with HIV '
        'should attend school with children who are HIV negative?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    aids_room_sharing = models.CharField(
        verbose_name='Would you share a room '
        'with a person you knew has been diagnosed with TB?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    aids_hiv_testing = models.CharField(
        verbose_name='Have you ever been tested for HIV?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    aids_hiv_times_tested = models.IntegerField(
        verbose_name='In the past 12 months how many times'
        ' have you been tested for HIV and received your results?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    aids_hiv_times_tested_other = OtherCharField(
        verbose_name='Did you test together with your partner?',
        max_length=250,
        choices=YES_NO,
        blank=True,
        null=True
    )

    aids_hiv_times_tested_other = OtherCharField(
        verbose_name='What was the main reason for testing?',
        max_length=35,
        choices=TESTING_REASONS,
        help_text="",
        null=True,
        blank=False
    )

    aids_hiv_not_tested = OtherCharField(
        verbose_name='Why haven’t you tested?',
        max_length=35,
        choices=TESTING_REASONS,
        help_text="",
        null=True,
        blank=False
    )

    tb_diagnosis = models.CharField(
        verbose_name='If you were diagnosed with Tb,would you tell anyone?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_diagnosis_disclosure = models.CharField(
        verbose_name='If yes, whom would you tell?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_diagnosis_tested_other = OtherCharField(
        verbose_name='If No,why not',
        max_length=35,
        choices=TB_NONDISCLOSURE,
        help_text="",
        null=True,
        blank=False
    )

    class Meta:
        app_label = 'bais_subject'
