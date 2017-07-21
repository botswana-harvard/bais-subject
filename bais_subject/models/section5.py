from django.db import models

from ..choices import YES_NO


class Section5:

    """ Knowledge About HIV and AIDS and TB
     and level of Access to Interventions
     """
    hiv_and_aids_awareness = models.CharField(
        verbose_name="Have you ever heard of HIV or an illness called AIDS?",
        max_length=35,
        choices=YES_NO,
        help_text="",
    )
