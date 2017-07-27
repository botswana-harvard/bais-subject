from django.db import models

from edc_base.model_fields import OtherCharField

from ..choices import (YES_NO, YES_NO_UNSURE, YES_NO_DNTKNW, TRANSMISSION_PREVENTION,
                       TREATMENT_OPTIONS, ARV_USES, ARV_CONCERN,
                       ARV_INFLUENCE, SEXUAL_BEHAVIOUR,
                       TB_INFECTION, TB_SPREAD, TB_CURE, SMC_SOURCE,
                       CONDOM_CONSENT)


class Section5(models.Model):

    """ Knowledge About HIV and AIDS and TB
     and level of Access to Interventions
     """
    hiv_and_aids_awareness = models.CharField(
        verbose_name='Have you ever heard of HIV or an illness called AIDS?',
        max_length=35,
        choices=YES_NO,
    )

    hiv_and_aids_awareness_b = models.CharField(
        verbose_name="In the past 4 weeks, have you heard or seen information about HIV/AIDS?",
        max_length=35,
        choices=YES_NO,
        help_text="",
    )

    hiv_and_aids_information = models.CharField(
        verbose_name="From what source(s) did you recieve information about HIV and AIDS?",
        max_length=35,
        choices=YES_NO,
        help_text="Circle all that are mentioned more than one anwser is possible"
    )

    hiv_and_aids_prevention = models.CharField(
        verbose_name="What can people do to prevent becoming infected with HIV?",
        max_length=35,
        choices=YES_NO,
        help_text="Circle all that are mentioned more than one anwser is possible"
    )

    tb_awareness = models.CharField(
        verbose_name="Have you ever heard of TB?",
        max_length=35,
        choices=YES_NO,
        help_text="",
    )

    tb_recent_information = models.CharField(
        verbose_name="In the past 4 weeks,have you heard or seen any information about TB?",
        max_length=35,
        choices=YES_NO,
        help_text="",
    )

    tb_information_source = models.CharField(
        verbose_name="From what source(s) did you recieve information about TB?",
        max_length=35,
        choices=YES_NO,
        help_text="Circle all that are mentioned more than one anwser is possible"
    )

    tb_information_source_other = OtherCharField(
        verbose_name='Other,Specify',
        blank=True,
    )

    tb_prevention = models.CharField(
        verbose_name="What can people do to prevent becoming infected with TB?",
        max_length=35,
        choices=YES_NO,
        help_text="Circle all that are mentioned more than one anwser is possible"
    )

    tb_prevention_other = OtherCharField(
        verbose_name='Other,Specify',
        null=True,
        blank=True,
    )

    hiv_and_aids_appearance = models.CharField(
        verbose_name="Is it possible for a healthy looking person to have HIV?",
        max_length=35,
        choices=YES_NO_DNTKNW,
        help_text="",
    )

    hiv_and_aids_condom_use = models.CharField(
        verbose_name='Can people reduce their chances of getting HIV'
        ' and AIDS by using condom correctly everytime they have sex?',
        max_length=35,
        choices=YES_NO_DNTKNW,
    )

    hiv_and_aids_mosquito_bite = models.CharField(
        verbose_name='Do you think a person can get infected'
        ' with HIV through mosquito bites?',
        max_length=35,
        choices=YES_NO_DNTKNW,
    )

    hiv_and_aids_partners = models.CharField(
        verbose_name='Can people reduce their chances of getting'
        'HIV and AIDS by having only one uninfected'
        'sex partner who has no other partners?',
        max_length=35,
        choices=YES_NO_DNTKNW,
    )

    hiv_and_aids_sharing_meal = models.CharField(
        verbose_name='Can a person get infected with HIv by sharing a '
        ' meal (from the same plate) with a person who has HIV and aids?',
        max_length=35,
        choices=YES_NO_DNTKNW,
    )

    hiv_and_aids_witchcraft = models.CharField(
        verbose_name="Can people get HIV because of witchcraft?",
        max_length=35,
        choices=YES_NO_DNTKNW,
    )

    hiv_and_aids_mother_to_child = models.CharField(
        verbose_name="Can HIV be transmitted from mother to child?",
        max_length=35,
        choices=YES_NO_DNTKNW,
    )

    hiv_and_aids_unborn_baby = models.CharField(
        verbose_name='If a mother is infected with HIV AND AIDS,'
        ' is there any way to avoid transmission to the unborn baby?',
        max_length=35,
        choices=YES_NO_DNTKNW,
    )

    hiv_and_aids_unborn_baby_transmission = models.CharField(
        verbose_name='If yes, what ways',
        max_length=250,
        choices=TRANSMISSION_PREVENTION,
    )

    hiv_and_aids_unborn_baby_transmission_other = OtherCharField(
        verbose_name='Other, Specify',
        max_length=35,
    )

    hiv_and_aids_newborn_baby = models.CharField(
        verbose_name='If a mother is infected with HIV AND AIDS,'
        ' is there any way to avoid transmission to the newborn baby?',
        max_length=35,
        choices=YES_NO_DNTKNW,
    )

    hiv_and_aids_newborn_baby_transmission = models.CharField(
        verbose_name='If yes, what ways',
        max_length=250,
        choices=TRANSMISSION_PREVENTION,
    )

    hiv_and_aids_newborn_baby_transmission_other = OtherCharField(
        verbose_name='Other, Specify',
        max_length=250,
    )

    hiv_and_aids_treatment_options = models.CharField(
        verbose_name='What treatment options are available'
        ' for HIV infected people?',
        max_length=35,
        choices=TREATMENT_OPTIONS,
    )

    hiv_and_aids_treatment_options_other = OtherCharField(
        verbose_name='OTHER, SPECIFY',
        max_length=35,
    )

    arv_treatment = models.CharField(
        verbose_name='What do you believe anti -retroviral (ARVs) do?',
        max_length=35,
        choices=ARV_USES,
    )

    arv_treatment_concern = models.CharField(
        verbose_name='Has your personal concern about getting HIV changed'
        'since the introduction of ARV’s?',
        max_length=35,
        choices=ARV_USES,
    )

    arv_treatment_concern_yes = models.CharField(
        verbose_name='If yes, what ways',
        max_length=250,
        choices=ARV_CONCERN,
    )

    arv_treatment_concern_yes_other = OtherCharField(
        verbose_name='Other, Specify',
        max_length=250,
    )

    arv_treatment_condomize = models.CharField(
        verbose_name='Do you think that people on ARV’s should always use condoms?',
        max_length=35,
        choices=YES_NO_DNTKNW,
    )

    arv_sexual_behaviour = models.CharField(
        verbose_name='Has introduction of ARVs influenced your sexual behavior?',
        max_length=35,
        choices=ARV_INFLUENCE,
    )

    arv_sexual_behaviour_yes = models.CharField(
        verbose_name='If yes, what ways',
        max_length=250,
        choices=SEXUAL_BEHAVIOUR,
    )

    arv_sexual_behaviour_yes_other = OtherCharField(
        verbose_name='OTHER, SPECIFY',
        max_length=250,
    )

    arv_intake = models.CharField(
        verbose_name='Do you think a person on ARVs should '
        'discontinue/stop taking them once they feel better?',
        max_length=35,
        choices=YES_NO_DNTKNW,
    )

    tb_appearance = models.CharField(
        verbose_name='Is it possible for a healthy looking person to have TB?',
        max_length=35,
        choices=YES_NO_DNTKNW,
    )

    tb_infection = models.CharField(
        verbose_name='In your opinion, who can be infected with TB?',
        max_length=35,
        choices=TB_INFECTION,
    )

    tb_infection_other = OtherCharField(
        verbose_name='OTHER, SPECIFY',
        max_length=250,
    )

    tb_spread = models.CharField(
        verbose_name='How can a person get tb?',
        max_length=35,
        choices=TB_SPREAD,
    )

    tb_spread_other = OtherCharField(
        verbose_name='OTHER, SPECIFY',
        max_length=35,
    )

    tb_cure = models.CharField(
        verbose_name='Do you think that TB can be treated /curable?',
        max_length=35,
        choices=YES_NO_DNTKNW,
    )

    tb_cure_yes = models.CharField(
        verbose_name='How can Tb be cured?',
        max_length=250,
        choices=TB_CURE,
    )

    tb_cure_yes_other = OtherCharField(
        verbose_name='OTHER, SPECIFY',
        max_length=250,
    )

    smc_programme = models.CharField(
        verbose_name='Have you ever heard of Safe Male Circumcision or SMC programme?',
        max_length=35,
        choices=YES_NO,
    )

    smc_programme_awareness = models.CharField(
        verbose_name='In the past 4 weeks, have you heard or '
        'seen any information on Safe Male Circumcision (SMC)?',
        max_length=35,
        choices=YES_NO,
    )

    smc_programme_source = models.CharField(
        verbose_name='From what source(s) did you receive this'
        'information about Safe Male Circumcision or SMC',
        max_length=35,
        choices=SMC_SOURCE,
    )

    smc_programme_source_other = OtherCharField(
        verbose_name='OTHER, SPECIFY',
        max_length=35,
    )

    smc_programme_interest = models.CharField(
        verbose_name='Suppose you had male children aged below 18 years'
        ' would you get them circumcised?',
        max_length=35,
        choices=YES_NO,
    )

    smc_condomize = models.CharField(
        verbose_name='Do you think a circumcised male should stop using condoms?',
        max_length=35,
        choices=YES_NO,
    )

    condom_male_collection = models.CharField(
        verbose_name='Do you think it should be acceptable for a woman to obtain male condoms?',
        max_length=35,
        choices=YES_NO,
    )

    condom_collection_man = models.CharField(
        verbose_name='Do you think it should be acceptable'
        ' for a man to obtain female condoms?',
        max_length=250,
        choices=YES_NO_UNSURE,
    )

    condom_consent = models.CharField(
        verbose_name=' Do you agree that a woman has a right to decide'
        'if she will have safe sex? (e.g use a condom)',
        max_length=35,
        choices=YES_NO_UNSURE,
    )

    condom_consent_woman = models.CharField(
        verbose_name=' Why not?',
        max_length=35,
        choices=CONDOM_CONSENT,
        null=True,
        blank=True,
    )

    condom_consent_woman_other = OtherCharField(
        verbose_name=' OTHER, SPECIFY',
        max_length=35,
    )

    class Meta:
        app_label = 'bais_subject'
