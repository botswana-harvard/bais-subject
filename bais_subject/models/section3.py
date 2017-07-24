from django.db import models

from edc_base.model_fields import OtherCharField

from ..choices import (
    YES_NO,
    YES_NO_DNTKNW,
    SEXUAL_INTERCOURSE_INFLUENCE,
    SEXUAL_INTERCOURSE_PROTECTION,
    SEX_PARTNER,
    ASSISTANCE,
    VIOLANCE,
    VIOLANCE_WHO,
    SERIAL_CONCURRENT,
    CONDOM_REASON,
    CONDOM_NOT_USED_REASON,
    CONDOM_PLACE,
    DRUNK_HIGH_SEX,
    CONDOM_PERSUATION)


class Section3(models.Model):

    sexual_intercouse = models.CharField(
        verbose_name='Have you ever had sexual intercourse?',
        max_length=5,
        choices=YES_NO
    )

    sexual_intercourse_age = models.IntegerField(
        verbose_name='At what age did you first have sexual '
        'intercourse?',
        max_length=15,
    )

    sexual_intercouse_consent = models.CharField(
        verbose_name='Did you give consent at the time of intercourse?',
        max_length=5,
        choices=YES_NO
    )

    sexual_intercourse_influence = models.CharField(
        verbose_name='What mainly influenced your decision to agree '
        'to have sexual intercourse the first time?',
        max_length=45,
        choices=SEXUAL_INTERCOURSE_INFLUENCE
    )

    sexual_intercourse_influence_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    sexual_intercouse_protection = models.CharField(
        verbose_name='Was protection used during that sexual '
        'intercourse?',
        max_length=5,
        choices=YES_NO_DNTKNW
    )

    sexual_intercouse_protection_use = models.CharField(
        verbose_name='What did you use?',
        max_length=45,
        choices=SEXUAL_INTERCOURSE_PROTECTION
    )

    sexual_intercouse_protection_use_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    sexual_intercouse_protection_reason = models.CharField(
        verbose_name='Please state the main reason for protecting '
        'yourself',
        max_length=45,
        choices=SEXUAL_INTERCOURSE_PROTECTION
    )

    sexual_intercouse_protection_reason_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    sex_recently = models.CharField(
        verbose_name='Have you had sex in the last 12 months?',
        max_length=5,
        choices=YES_NO
    )

    sex_consentual = models.CharField(
        verbose_name='Was the sexual intercourse consensual?',
        max_length=5,
        choices=YES_NO
    )

    sex_with_whom = models.CharField(
        verbose_name='With whom?',
        max_length=45,
        choices=SEX_PARTNER
    )

    sex_with_whom_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    assistance = models.CharField(
        verbose_name='What assistance did you seek/get?',
        max_length=45,
        choices=ASSISTANCE
    )

    assistance_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    physical_sexual_violance_male = models.CharField(
        verbose_name='Have you experienced physical or sexual '
        'violence from a male intimate partner in the last 12 months?',
        max_length=45,
        choices=VIOLANCE
    )

    physical_sexual_violance_female = models.CharField(
        verbose_name='Have you experienced physical or sexual '
        'violence from a female intimate partner in the last 12 months?',
        max_length=45,
        choices=VIOLANCE
    )

    physical_sexual_violance_who = models.CharField(
        verbose_name='By who?',
        max_length=45,
        choices=VIOLANCE_WHO
    )

    sex_partners_count = models.IntegerField(
        verbose_name='In the last 12 months with how many people '
        'overall have you had sex?',
        max_length=5
    )

    partners_serial_concurrent = models.CharField(
        verbose_name='By who?',
        max_length=45,
        choices=SERIAL_CONCURRENT
    )

    partners_serial_concurrent_explain = OtherCharField(
        verbose_name='If concurrent, explain',
        max_length=250,
        blank=True,
        null=True
    )

    # TODO: Yet to find a way to represent this next questions in tabular form

    """
    Going to figure out a way to fix the redundancies
    """

    condom_main_reason_partner1 = models.CharField(
        verbose_name='What was the MAIN reason for using the condom '
        'the last time you had sex?',
        max_length=45,
        choices=CONDOM_REASON,
        help_text='Partner 1. Most recent sexual partner'
    )

    condom_main_reason_partner2 = models.CharField(
        verbose_name='What was the MAIN reason for using the condom '
        'the last time you had sex?',
        max_length=45,
        choices=CONDOM_REASON,
        help_text='Partner 2. Most recent sexual partner'
    )

    condom_main_reason_partner3 = models.CharField(
        verbose_name='What was the MAIN reason for using the condom '
        'the last time you had sex?',
        max_length=45,
        choices=CONDOM_REASON,
        help_text='Partner 3. Most recent sexual partner'
    )

    condom_not_used_reason_partner1 = models.CharField(
        verbose_name='What was the main reason for NOT using '
        'the condom?',
        max_length=45,
        choices=CONDOM_NOT_USED_REASON,
        help_text='Partner 1. Most recent sexual partner'
    )

    condom_not_used_reason_partner1_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    condom_not_used_reason_partner2 = models.CharField(
        verbose_name='What was the main reason for NOT using '
        'the condom?',
        max_length=45,
        choices=CONDOM_NOT_USED_REASON,
        help_text='Partner 2. Most recent sexual partner'
    )

    condom_not_used_reason_partner2_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    condom_not_used_reason_partner3 = models.CharField(
        verbose_name='What was the main reason for NOT using '
        'the condom?',
        max_length=45,
        choices=CONDOM_NOT_USED_REASON,
        help_text='Partner 3. Most recent sexual partner'
    )

    condom_not_used_reason_partner3_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    condom_place_partner1 = models.CharField(
        verbose_name='From what place or person did you or this '
        'partner get that condom?',
        max_length=45,
        choices=CONDOM_PLACE,
        help_text='Partner 1. Most recent sexual partner'
    )

    condom_place_partner1_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    condom_place_partner2 = models.CharField(
        verbose_name='From what place or person did you or this '
        'partner get that condom?',
        max_length=45,
        choices=CONDOM_PLACE,
        help_text='Partner 2. Most recent sexual partner'
    )

    condom_place_partner2_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    condom_place_partner3 = models.CharField(
        verbose_name='From what place or person did you or this '
        'partner get that condom?',
        max_length=45,
        choices=CONDOM_PLACE,
        help_text='Partner 3. Most recent sexual partner'
    )

    condom_place_partner3_other = OtherCharField(
        verbose_name='If other, specify',
        max_length=250,
        blank=True,
        null=True
    )

    drunk_high_sex_partner1 = models.CharField(
        verbose_name='Were you and/or your partner drunk or high on '
        'drugs the LAST time you had sex?',
        max_length=45,
        choices=DRUNK_HIGH_SEX,
        help_text='Partner 1. Most recent sexual partner'
    )

    drunk_high_sex_partner2 = models.CharField(
        verbose_name='Were you and/or your partner drunk or high on '
        'drugs the LAST time you had sex?',
        max_length=45,
        choices=DRUNK_HIGH_SEX,
        help_text='Partner 2. Most recent sexual partner'
    )

    drunk_high_sex_partner3 = models.CharField(
        verbose_name='Were you and/or your partner drunk or high on '
        'drugs the LAST time you had sex?',
        max_length=45,
        choices=DRUNK_HIGH_SEX,
        help_text='Partner 3. Most recent sexual partner'
    )

    partner_other_partners_partner1 = models.CharField(
        verbose_name='Do you think this partner has other partners?',
        max_length=45,
        choices=YES_NO_DNTKNW,
        help_text='Partner 1. Most recent sexual partner'
    )

    partner_other_partners_partner2 = models.CharField(
        verbose_name='Do you think this partner has other partners?',
        max_length=45,
        choices=YES_NO_DNTKNW,
        help_text='Partner 2. Most recent sexual partner'
    )

    partner_other_partners_partner3 = models.CharField(
        verbose_name='Do you think this partner has other partners?',
        max_length=45,
        choices=YES_NO_DNTKNW,
        help_text='Partner 3. Most recent sexual partner'

    )

    sexual_partner_recent1 = models.CharField(
        verbose_name='Was this sexual contact within the past 12 '
        'months?',
        max_length=45,
        choices=YES_NO,
        help_text='Partner 1. Most recent sexual partner'
    )

    sexual_partner_recent2 = models.CharField(
        verbose_name='Was this sexual contact within the past 12 '
        'months?',
        max_length=45,
        choices=YES_NO,
        help_text='Partner 2. Most recent sexual partner'
    )

    sexual_partner_recent3 = models.CharField(
        verbose_name='Was this sexual contact within the past 12 '
        'months?',
        max_length=45,
        choices=YES_NO,
        help_text='Partner 3. Most recent sexual partner'
    )

#    End of the tabular form

    paid_for_sex = models.CharField(
        verbose_name='In the last 12 months have you ever been paid '
        'or received gifts for sex? ',
        max_length=45,
        choices=YES_NO,
    )

    persuade_sex_partner = models.CharField(
        verbose_name='Do you believe you can persuade a sex partner '
        'to use a condom?',
        max_length=45,
        choices=CONDOM_PERSUATION,
    )

    persuade_sex_partner_not = models.CharField(
        verbose_name='Could you persuade a sex partner NOT to have '
        'sex if you weren’t interested?',
        max_length=45,
        choices=CONDOM_PERSUATION,
    )

    multiple_sex_partner_man = models.CharField(
        verbose_name='Do you think it is acceptable for a man to '
        'have more than one sexual partner?',
        max_length=45,
        choices=YES_NO,
    )

    multiple_sex_partner_woman = models.CharField(
        verbose_name='Do you think it is acceptable for a woman to '
        'have more than one sexual partner?',
        max_length=45,
        choices=YES_NO,
    )

    class Meta:
        app_label = 'bais_subject'
