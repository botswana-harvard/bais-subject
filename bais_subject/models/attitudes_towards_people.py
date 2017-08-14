from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_mixins import BaseUuidModel

from ..choices import (YES_NO, TESTING_REASONS, TB_NONDISCLOSURE,
                       HIV_TEST_RESULT, ARV_USAGE, ARV_TREATMENT_SOURCE,
                       REASONS_ARV_NOT_TAKEN, TB_REACTION)


class AttitudesTowardsPeople(BaseUuidModel):

    meal_sharing = models.CharField(
        verbose_name='Would you ever share a meal (from the same plate)'
        ' with a person you knew or suspected had HIV AND AIDS?',
        max_length=35,
        choices=YES_NO,
    )

    aids_household_care = models.CharField(
        verbose_name='If a member of your family became sick with HIV AND AIDS,'
        ' would you be willing to care for him or her in your household?',
        max_length=35,
        choices=YES_NO,
    )

    tb_household_care = models.CharField(
        verbose_name='If a member of your family became sick with TB,'
        ' would you be willing to care for him or her in your household?',
        max_length=35,
        choices=YES_NO,
    )

    tb_household_empathy = models.CharField(
        verbose_name='If a member of your family got diagnosed with TB,'
        ' would you be willing to care for him or her in your household?',
        max_length=35,
        choices=YES_NO,
    )

    aids_housekeeper = models.CharField(
        verbose_name='If your housekeeper, nanny or anybody looking'
        ' after your child has HIV but is not sick, '
        'would you allow him/her to continue'
        ' working/assisting with babysitting in your house? ',
        max_length=35,
        choices=YES_NO,
    )

    aids_teacher = models.CharField(
        verbose_name='If a teacher has HIV but is not sick,'
        ' should s/he be allowed to continue teaching in school?',
        max_length=35,
        choices=YES_NO,
    )

    aids_shopkeeper = models.CharField(
        verbose_name='If you knew that a shopkeeper or food seller had'
        ' HIV or AIDS, would you buy vegetables from them?',
        max_length=35,
        choices=YES_NO,

    )

    aids_family_member = models.CharField(
        verbose_name='If a member of your family got infected'
        'with HIV, would you want it to remain a secret?',
        max_length=35,
        choices=YES_NO,
        help_text="",
    )

    aids_children = models.CharField(
        verbose_name='Do you think that children living with HIV '
        'should attend school with children who are HIV negative?',
        max_length=35,
        choices=YES_NO,
    )

    aids_room_sharing = models.CharField(
        verbose_name='Would you share a room '
        'with a person you knew has been diagnosed with TB?',
        max_length=35,
        choices=YES_NO,
    )

    aids_hiv_testing = models.CharField(
        verbose_name='Have you ever been tested for HIV?',
        max_length=35,
        choices=YES_NO,
    )

    aids_hiv_times_tested = models.CharField(
        verbose_name='In the past 12 months how many times'
        ' have you been tested for HIV and received your results?',
        max_length=35,
        choices=YES_NO,
    )

    aids_hiv_test_partner = models.CharField(
        verbose_name='Did you test together with your partner?',
        max_length=250,
        choices=YES_NO,
    )

    aids_hiv_test_reason = models.CharField(
        verbose_name='What was the main reason for testing?',
        max_length=35,
        choices=TESTING_REASONS,
    )

    aids_hiv_test_reason_other = OtherCharField(
        verbose_name='Specify Other',
        max_length=35,
        null=True,
        blank=True,
    )

    aids_hiv_not_tested = models.CharField(
        verbose_name='Why haven’t you tested?',
        max_length=35,
        choices=TESTING_REASONS,
    )

    aids_hiv_not_tested_other = OtherCharField(
        verbose_name='Other, Specify',
        max_length=35,
        null=True,
        blank=True,
    )

    aids_hiv_test_result = models.CharField(
        verbose_name='What was the result of your last HIV test?  ',
        max_length=35,
        choices=HIV_TEST_RESULT,
    )

    aids_hiv_test_result_disclosure = models.CharField(
        verbose_name='Did you tell anyone the result of your the test?  ',
        max_length=35,
        choices=YES_NO,
    )

    current_arv_therapy = models.CharField(
        verbose_name='Are you currently taking ARVs?',
        max_length=35,
        choices=ARV_USAGE,
    )

    current_arv_supplier = models.CharField(
        verbose_name='Where are you taking your ARVs?',
        max_length=35,
        choices=ARV_TREATMENT_SOURCE,
    )

    current_arv_supplier_other = OtherCharField(
        verbose_name='Other Specify',
        max_length=35,
        null=True,
        blank=True,
    )

    not_on_arv_therapy = models.CharField(
        verbose_name='Why aren\'t you taking your ARVs?',
        max_length=35,
        choices=REASONS_ARV_NOT_TAKEN,
    )

    not_on_arv_therapy_other = OtherCharField(
        verbose_name='Other Specify',
        max_length=35,
        blank=True,
        null=True

    )

    tb_reaction = models.CharField(
        verbose_name='What would be your reaction'
        ' if you found out you had TB ?',
        max_length=35,
        choices=TB_REACTION,
    )

    tb_reaction_other = OtherCharField(
        verbose_name='Other Specify',
        max_length=35,
        null=True,
        blank=True,
    )

    tb_diagnosis = models.CharField(
        verbose_name='If you were diagnosed with Tb,would you tell anyone?',
        max_length=35,
        choices=YES_NO,
    )

    tb_diagnosis_disclosure = models.CharField(
        verbose_name='If yes, whom would you tell?',
        max_length=35,
        choices=YES_NO,
    )

    tb_diagnosis_no_disclosure = models.CharField(
        verbose_name='If No,why not',
        max_length=35,
        choices=TB_NONDISCLOSURE,
    )

    tb_diagnosis_no_disclosure_other = OtherCharField(
        verbose_name='Other, Specify',
        max_length=35,
        blank=True,
        null=True
    )

    class Meta(BaseUuidModel.Meta):
        app_label = 'bais_subject'
