from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_validators import date_not_future

from ..choices import (YES_NO, TB_TREATMENT_SOURCE, TB_TIMES_TREATED,
                       TB_SPUTUM_SAMPLE, TB_NO_SPUTUM, TB_HELP,
                       TB_HELP_RESULT, TB_NO_HELP_REASON, CANCER_TEST)


class Section8(models.Model):

    tb_current_treatment = models.CharField(
        verbose_name='Are you on TB treatment now?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_treatment_source = models.CharField(
        verbose_name='Where are you getting your TB treatment?',
        max_length=35,
        choices=TB_TREATMENT_SOURCE,
        help_text="",
        null=True,
        blank=False
    )

    tb_previous_treatment = models.CharField(
        verbose_name='Have you been on TB treatment before?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_previous_times_treated = models.CharField(
        verbose_name='How many times have you been treated for TB?',
        max_length=35,
        choices=TB_TIMES_TREATED,
        help_text="",
        null=True,
        blank=False
    )

    tb_treatment_date = models.DateField(
        verbose_name='In which month and year did you start treatment?',
        validators=[date_not_future],
    )

    tb_cough = models.CharField(
        verbose_name='Do you have a cough?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_cough_duration = models.CharField(
        verbose_name='How long have you had this cough? ',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_cough_sputum = models.CharField(
        verbose_name='Do you cough up sputum?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_bloody_sputum = models.CharField(
        verbose_name='Does that sputum have blood in it?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_sputum_sample = models.CharField(
        verbose_name='Did you submit a sputum sample?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_sputum_sample_result = OtherCharField(
        verbose_name='If YES,What was the result?',
        max_length=35,
        choices=TB_SPUTUM_SAMPLE,
        help_text="",
        null=True,
        blank=False
    )

    tb_sputum_sample_result = OtherCharField(
        verbose_name='If NO,Why not?',
        max_length=35,
        choices=TB_NO_SPUTUM,
        help_text="",
        null=True,
        blank=False
    )

    tb_fever = models.CharField(
        verbose_name='Do you have a fever?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_sputum_sample_result = OtherCharField(
        verbose_name='If YES,for how long?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_night_sweat = models.CharField(
        verbose_name='Do you have drenching night sweats?'
        '(So that you have to change your bedclothes)',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_night_sweat_other = OtherCharField(
        verbose_name='IF YEs, for how long?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_weight_loss = models.CharField(
        verbose_name='In the past month, have you unexpectedly lost weight?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_help = models.CharField(
        verbose_name='Thinking about these current symptoms,'
        ' did you consult with someone for help?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    tb_first_help = models.CharField(
        verbose_name='Where did you FIRST go for help?',
        max_length=35,
        choices=TB_HELP,
        help_text="",
        null=True,
        blank=False
    )

    tb_first_help_result = models.CharField(
        verbose_name='If you consulted, what happened?',
        max_length=35,
        choices=TB_HELP_RESULT,
        help_text="",
        null=True,
        blank=False
    )

    tb_no_help = models.CharField(
        verbose_name='If you did not seek help, what were the reasons?',
        max_length=35,
        choices=TB_NO_HELP_REASON,
        help_text="",
        null=True,
        blank=False
    )

    diabetes_diagnosis = models.CharField(
        verbose_name='Have you ever been diagnosed with diabetes?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    diabetes_treatment = models.CharField(
        verbose_name='Are you currently taking treatment for your diabetes?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    cervical_cancer_screening = models.CharField(
        verbose_name='Have you ever been screened by a doctor'
        ' or other health professional for cervical cancer?',
        max_length=35,
        choices=YES_NO,  # MOnth ago
        help_text="",
        null=True,
        blank=False
    )

    last_cancer_test = OtherCharField(
        verbose_name='In the last 2 years when was the last time'
        'you tested for cancer? ',
        max_length=35,
        choices=CANCER_TEST,
        help_text="",
        null=True,
        blank=False
    )

    cancer_test_result = models.CharField(
        verbose_name='Did the Doctor tell you that you may'
        ' have problems with your cervix?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    cancer_treatment_referral = models.CharField(
        verbose_name='Were you referred for cervical cancer treatment?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    class Meta:
        app_label = 'bais_subject'
