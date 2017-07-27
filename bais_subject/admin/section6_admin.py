from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import bais_subject_admin
from ..forms import Section6Form
from ..models import Section6


@admin.register(Section6, site=bais_subject_admin)
class Section8Admin(admin.ModelAdmin):

    form = Section6Form

    radio_fields = {
        'meal_sharing': admin.VERTICAL,
        'aids_household_care': admin.VERTICAL,
        'tb_household_care': admin.VERTICAL,
        'aids_housekeeper': admin.VERTICAL,
        'aids_teacher': admin.VERTICAL,
        'aids_shopkeeper': admin.VERTICAL,
        'aids_family_member': admin.VERTICAL,
        'aids_children': admin.VERTICAL,
        'aids_room_sharing': admin.VERTICAL,
        'aids_hiv_testing': admin.VERTICAL,
        'aids_hiv_times_tested': admin.VERTICAL,
        'aids_hiv_tested_partner': admin.VERTICAL,
        'aids_hiv_test_reason': admin.VERTICAL,
        'aids_hiv_test_reason_other': admin.VERTICAL,
        'aids_hiv_not_tested': admin.VERTICAL,
        'aids_hiv_not_tested_other': admin.VERTICAL,
        'aids_hiv_test_result': admin.VERTICAL,
        'aids_hiv_test_result_disclosure': admin.VERTICAL,
        'current_arv_therapy': admin.VERTICAL,
        'current_arv_supplier': admin.VERTICAL,
        'current_arv_supplier_other': admin.VERTICAL,
        'not_on_arv_therapy': admin.VERTICAL,
        'not_on_arv_therapy_other': admin.VERTICAL,
        ' tb_reaction': admin.VERTICAL,
        'tb_reaction_other': admin.VERTICAL,
        'tb_diagnosis': admin.VERTICAL,
        'tb_diagnosis_disclosure': admin.VERTICAL,
        'tb_diagnosis_no_disclosure': admin.VERTICAL}

    fieldsets = (
        ('Section 6', {
            'fields': (
                'meal_sharing',
                'aids_household_care',
                'aids_housekeeper',
                'aids_teacher',
                'aids_shopkeeper',
                'aids_family_member',
                'aids_children',
                'aids_room_sharing',
                'aids_hiv_testing',
                'aids_hiv_test_result',
                'aids_hiv_test_result_disclosure',
                'current_arv_therapy',
                'tb_diagnosis',
                'tb_diagnosis_disclosure',)},
         ),
        audit_fieldset_tuple
    )