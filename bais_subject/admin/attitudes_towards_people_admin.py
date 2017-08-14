from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..forms import AttitudesTowardsPeopleForm
from ..models import AttitudesTowardsPeople


@admin.register(AttitudesTowardsPeople)
class AttitudesTowardsPeopleAdmin(admin.ModelAdmin):

    form = AttitudesTowardsPeopleForm

    radio_fields = {
        'meal_sharing': admin.VERTICAL,
        'aids_household_care': admin.VERTICAL,
        'tb_household_care': admin.VERTICAL,
        'tb_household_empathy': admin.VERTICAL,
        'aids_housekeeper': admin.VERTICAL,
        'aids_teacher': admin.VERTICAL,
        'aids_shopkeeper': admin.VERTICAL,
        'aids_family_member': admin.VERTICAL,
        'aids_children': admin.VERTICAL,
        'aids_room_sharing': admin.VERTICAL,
        'aids_hiv_testing': admin.VERTICAL,
        'aids_hiv_times_tested': admin.VERTICAL,
        'aids_hiv_test_reason': admin.VERTICAL,
        'aids_hiv_not_tested': admin.VERTICAL,
        'aids_hiv_test_partner': admin.VERTICAL,
        'aids_hiv_test_result': admin.VERTICAL,
        'aids_hiv_test_result_disclosure': admin.VERTICAL,
        'current_arv_therapy': admin.VERTICAL,
        'current_arv_supplier': admin.VERTICAL,
        'not_on_arv_therapy': admin.VERTICAL,
        'current_arv_supplier': admin.VERTICAL,
        'not_on_arv_therapy': admin.VERTICAL,
        'tb_reaction': admin.VERTICAL,
        'tb_diagnosis': admin.VERTICAL,
        'tb_diagnosis_disclosure': admin.VERTICAL,
        'tb_diagnosis_no_disclosure': admin.VERTICAL}

    fieldsets = (
        ('Attitudes Towards People', {
            'fields': (
                'meal_sharing',
                'aids_household_care',
                'tb_household_care',
                'tb_household_empathy',
                'aids_housekeeper',
                'aids_teacher',
                'aids_shopkeeper',
                'aids_family_member',
                'aids_children',
                'aids_room_sharing',
                'aids_hiv_testing',
                'aids_hiv_times_tested',
                'aids_hiv_test_partner',
                'aids_hiv_test_reason',
                'aids_hiv_test_reason_other',
                'aids_hiv_not_tested',
                'aids_hiv_not_tested_other',
                'aids_hiv_test_result',
                'aids_hiv_test_result_disclosure',
                'current_arv_therapy',
                'current_arv_supplier',
                'current_arv_supplier_other',
                'not_on_arv_therapy',
                'not_on_arv_therapy_other',
                'tb_reaction',
                'tb_reaction_other',
                'tb_diagnosis',
                'tb_diagnosis_disclosure',
                'tb_diagnosis_no_disclosure',
                'tb_diagnosis_no_disclosure_other',)},
         ),
        audit_fieldset_tuple
    )
