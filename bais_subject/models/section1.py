from django.db import models

from ..choices import MALE_FEMALE


class Section1:

    respondent_sex = models.CharField(
        verbose_name='Choose sex of the respondent',
        max_length=15,
        choices=MALE_FEMALE)

    class Meta:
        app_label = 'bais_subject'
