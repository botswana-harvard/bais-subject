from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_validators import date_not_future
from edc_base.model_mixins import BaseUuidModel

from ..choices import (YES_NO, TB_TREATMENT_SOURCE, TB_TIMES_TREATED,
                       TB_SPUTUM_SAMPLE, TB_NO_SPUTUM, TB_HELP,
                       TB_HELP_RESULT, TB_NO_HELP_REASON, CANCER_TEST)


class Section8(BaseUuidModel):

    tb_current_treatment = models.CharField(
        verbose_name='Are you on TB treatment now?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    tb_treatment_source = models.CharField(
        verbose_name='Where are you getting your TB treatment?',
        max_length=35,
        choices=TB_TREATMENT_SOURCE,
        help_text="",
        null=True,
        blank=True
    )

    tb_previous_treatment = models.CharField(
        verbose_name='Have you been on TB treatment before?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    tb_previous_times_treated = models.CharField(
        verbose_name='How many times have you been treated for TB?',
        max_length=35,
        choices=TB_TIMES_TREATED,
        help_text="",
        null=True,
        blank=True
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
        blank=True
    )

    tb_cough_duration = models.CharField(
        verbose_name='How long have you had this cough? ',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    tb_cough_sputum = models.CharField(
        verbose_name='Do you cough up sputum?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    tb_bloody_sputum = models.CharField(
        verbose_name='Does that sputum have blood in it?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    tb_sputum_sample = models.CharField(
        verbose_name='Did you submit a sputum sample?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    tb_sputum_sample_result = models.CharField(
        verbose_name='If YES,What was the result?',
        max_length=35,
        choices=TB_SPUTUM_SAMPLE,
        help_text="",
        null=True,
        blank=True
    )

    tb_sputum_sample_result_other = OtherCharField(
        verbose_name='Other,Specify',
        blank=True
    )

    tb_sputum_sample_no_result = models.CharField(
        verbose_name='If NO,Why not?',
        max_length=35,
        choices=TB_NO_SPUTUM,
        help_text="",
        null=True,
        blank=True
    )

    tb_sputum_sample_no_result_other = OtherCharField(
        verbose_name='Other,Specify',
        max_length=35,
        blank=True
    )

    tb_fever = models.CharField(
        verbose_name='Do you have a fever?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    tb_fever_duration = models.CharField(
        verbose_name='If YES,for how long?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    tb_fever_duration_other = OtherCharField(
        verbose_name='Other,Specify',
        max_length=35,
        blank=True
    )

    tb_night_sweat = models.CharField(
        verbose_name='Do you have drenching night sweats?'
        '(So that you have to change your bedclothes)',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    tb_night_sweat_duration = models.CharField(
        verbose_name='IF YEs, for how long?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    tb_weight_loss = models.CharField(
        verbose_name='In the past month, have you unexpectedly lost weight?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    tb_help = models.CharField(
        verbose_name='Thinking about these current symptoms,'
        ' did you consult with someone for help?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    tb_first_help = models.CharField(
        verbose_name='Where did you FIRST go for help?',
        max_length=35,
        choices=TB_HELP,
        help_text="",
        null=True,
        blank=True
    )

    tb_first_help_result = models.CharField(
        verbose_name='If you consulted, what happened?',
        max_length=35,
        choices=TB_HELP_RESULT,
        help_text="",
        null=True,
        blank=True
    )

    tb_no_help = models.CharField(
        verbose_name='If you did not seek help, what were the reasons?',
        max_length=35,
        choices=TB_NO_HELP_REASON,
        help_text="",
        null=True,
        blank=True
    )

    diabetes_diagnosis = models.CharField(
        verbose_name='Have you ever been diagnosed with diabetes?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    diabetes_treatment = models.CharField(
        verbose_name='Are you currently taking treatment for your diabetes?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    cervical_cancer_screening = models.CharField(
        verbose_name='Have you ever been screened by a doctor'
        ' or other health professional for cervical cancer?',
        max_length=35,
        choices=YES_NO,  # MOnth ago
        help_text="",
        null=True,
        blank=True
    )

    last_cancer_test = models.CharField(
        verbose_name='In the last 2 years when was the last time'
        'you tested for cancer? ',
        max_length=35,
        choices=CANCER_TEST,
        help_text="",
        null=True,
        blank=True
    )

    last_cancer_test_other = OtherCharField(
        verbose_name='Other,specify',
        max_length=35,
        blank=True
    )

    cancer_test_result = models.CharField(
        verbose_name='Did the Doctor tell you that you may'
        ' have problems with your cervix?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    cancer_treatment_referral = models.CharField(
        verbose_name='Were you referred for cervical cancer treatment?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=True
    )

    class Meta(BaseUuidModel.Meta):
        app_label = 'bais_subject'
