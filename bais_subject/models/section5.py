from django.db import models

from ..choices import YES_NO, YES_NO_DNTKNW


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

    hiv_and_aids_awareness = models.CharField(
        verbose_name="Have you ever heard of TB?",
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False,
    )

    hiv_and_aids_awareness = models.CharField(
        verbose_name="In the past 4 weeks,have you heard or seen any information about TB?",
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False,
    )

    hiv_and_aids_awareness = models.CharField(
        verbose_name="From what source(s) did you recieve information about TB?",
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False,
        help_text="Circle all that are mentioned more than one anwser is possible"
    )

    hiv_and_aids_awareness = models.CharField(
        verbose_name="What can people do to prevent becoming infected with TB?",
        max_length=35,
        choices=YES_NO,
        help_text="",
        null=True,
        blank=False,
        help_text="Circle all that are mentioned more than one anwser is possible"
    )

    hiv_and_aids_awareness = models.CharField(
        verbose_name="Is it possible for a healthy looking person to have HIV?",
        max_length=35,
        choices=YES_NO_DNTKNW,
        help_text="",
        null=True,
        blank=False,
    )

    hiv_and_aids_awareness = models.CharField(
        verbose_name="Can people reduce their chances of getting HIV and AIDS by using condom correctly everytime they have sex?",
        max_length=35,
        choices=YES_NO_DNTKNW,
        help_text="",
        null=True,
        blank=False,
    )

    hiv_and_aids_awareness = models.CharField(
        verbose_name="Do you think a person can get infected with HIV through mosquito bites?",
        max_length=35,
        choices=YES_NO_DNTKNW,
        help_text="",
        null=True,
        blank=False,
    )

    hiv_and_aids_awareness = models.CharField(
        verbose_name="Can people reduce their chances of getting HIV and AIDS by having only one uninfected sex partner who has no other partners?",
        max_length=35,
        choices=YES_NO_DNTKNW,
        help_text="",
        null=True,
        blank=False,
    )

    hiv_and_aids_awareness = models.CharField(
        verbose_name="Can a person get infected with HIv by sharing a  meal (from the same plate) with a person who has HIV and aids? ",
        max_length=35,
        choices=YES_NO_DNTKNW,
        help_text="",
        null=True,
        blank=False,
    )

    hiv_and_aids_awareness = models.CharField(
        verbose_name="Can people get HIV because of witchcraft?",
        max_length=35,
        choices=YES_NO_DNTKNW,
        help_text="",
        null=True,
        blank=False,
    )

    hiv_and_aids_awareness = models.CharField(
        verbose_name="Can HIV be transmitted from mother to child?",
        max_length=35,
        choices=YES_NO_DNTKNW,
        help_text="",
        null=True,
        blank=False,
    )

    class Meta:
        app_label = 'bais_subject'
