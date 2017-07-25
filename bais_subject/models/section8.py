from django.db import models

from edc_base.model_fields import OtherCharField

from ..choices import (YES_NO, TB_TREATMENT_SOURCE, TB_TIMES_TREATED)


class Section8:

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

    tb_treatment_date = models.CharField(
        verbose_name='In which month and year did you start treatment?',
        max_length=35,
        choices=,
        help_text="",
        null=True,
        blank=False
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

    tb_sputum_sample_result = models.OtherField(
        verbose_name='If YES,What was the result?',
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )               
