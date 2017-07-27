from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import bais_subject_admin
from ..forms import Section5Form
from ..models import Section5


@admin.register(Section5, site=bais_subject_admin)
class Section5Admin(admin.ModelAdmin):

    form = Section5Form

    radio_fields = {
        'hiv_and_aids_awareness': admin.VERTICAL,
        'hiv_and_aids_awareness_b': admin.VERTICAL,
        'hiv_and_aids_information': admin.VERTICAL,
        'hiv_and_aids_prevention': admin.VERTICAL,
        'tb_awareness': admin.VERTICAL,
        'tb_recent_information': admin.VERTICAL,
        'tb_information_source': admin.VERTICAL,
        'ttb_information_source_other': admin.VERTICAL,
        'tb_prevention': admin.VERTICAL,
        'tb_prevention_other': admin.VERTICAL,
        'hiv_and_aids_appearance': admin.VERTICAL,
        'hiv_and_aids_condom_use': admin.VERTICAL,
        'hiv_and_aids_mosquito_bite': admin.VERTICAL,
        'hiv_and_aids_sharing_meal': admin.VERTICAL,
        'hiv_and_aids_partners': admin.VERTICAL,
        'hiv_and_aids_witchcraft': admin.VERTICAL,
        'hiv_and_aids_mother_to_child': admin.VERTICAL,
        'hiv_and_aids_unborn_baby': admin.VERTICAL,
        'hiv_and_aids_unborn_baby_transmission': admin.VERTICAL,
        'hiv_and_aids_unborn_baby_transmission_other': admin.VERTICAL,
        'hiv_and_aids_newborn_baby': admin.VERTICAL,
        'hiv_and_aids_newborn_baby_transmission': admin.VERTICAL,
        'hiv_and_aids_newborn_baby_transmission_other': admin.VERTICAL,
        'hiv_and_aids_treatment_options': admin.VERTICAL,
        'hiv_and_aids_treatment_options_other': admin.VERTICAL,
        'arv_treatment': admin.VERTICAL,
        ' arv_treatment_concern': admin.VERTICAL,
        'arv_treatment_concern_yes_other': admin.VERTICAL,
        'arv_treatment_condomize': admin.VERTICAL,
        'arv_sexual_behaviour': admin.VERTICAL,
        'arv_sexual_behaviour_yes': admin.VERTICAL,
        'arv_sexual_behaviour_yes_other': admin.VERTICAL,
        'arv_intake': admin.VERTICAL,
        'tb_appearance': admin.VERTICAL,
        'tb_infection': admin.VERTICAL,
        'tb_infection_other': admin.VERTICAL,
        'tb_spread': admin.VERTICAL,
        'tb_spread_other': admin.VERTICAL,
        'tb_cure': admin.VERTICAL,
        'tb_cure_yes': admin.VERTICAL,
        'tb_cure_yes_other': admin.VERTICAL,
        'smc_programme': admin.VERTICAL,
        'smc_programme_awareness': admin.VERTICAL,
        'smc_programme_source': admin.VERTICAL,
        'smc_programme_source_other': admin.VERTICAL,
        'smc_programme_interest': admin.VERTICAL,
        'smc_condomize': admin.VERTICAL,
        'condom_male_collection': admin.VERTICAL,
        'condom_collection_man': admin.VERTICAL,
        'condom_consent': admin.VERTICAL,
        'condom_consent_woman': admin.VERTICAL,
        'condom_consent_woman_other': admin.VERTICAL}

    fieldsets = (
        ('Section 5', {
            'fields': (
                'hiv_and_aids_awareness',
                'hiv_and_aids_information',
                'hiv_and_aids_prevention',
                'tb_awareness',
                'tb_recent_information',
                'tb_information_source',
                'tb_prevention',
                'hiv_and_aids_appearance',
                'hiv_and_aids_condom_use',
                'hiv_and_aids_mosquito_bite',
                'hiv_and_aids_partners',
                'hiv_and_aids_sharing_meal',
                'hiv_and_aids_witchcraft',
                'hiv_and_aids_mother_to_child',
                'hiv_and_aids_unborn_baby',
                'hiv_and_aids_unborn_baby_transmission',
                'hiv_and_aids_newborn_baby',
                'hiv_and_aids_treatment_options'
                'arv_treatment'
                'arv_treatment_concern'
                'arv_treatment_condomize'
                'arv_sexual_behaviour'
                'arv_intake'
                'tb_appearance'
                'tb_infection'
                'tb_spread'
                'tb_cure'
                'smc_programme'
                'smc_programme_awareness'
                'smc_programme_source'
                'smc_programme_interest'
                'smc_condomize'
                'condom_male_collection')},
         ),
        audit_fieldset_tuple
    )
