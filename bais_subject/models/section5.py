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
        null=True,
    )

    hiv_and_aids_awareness_b = models.CharField(
        verbose_name="In the past 4 weeks, have you heard or seen information about HIV/AIDS?",
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False
    )

    hiv_and_aids_awareness = models.CharField(
        verbose_name="From what source(s) did you recieve information about HIV and AIDS?",
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False,
        help_text="Circle all that are mentioned more than one anwser is possible"
    )

    hiv_and_aids_awareness = models.CharField(
        verbose_name="What can people do to prevent becoming infected with HIV?",
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False,
        help_text="Circle all that are mentioned more than one anwser is possible"
    )
