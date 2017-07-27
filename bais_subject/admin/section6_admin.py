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
        'aids_housekeeper': admin.VERTICAL,
        'aids_teacher': admin.VERTICAL,
        'aids_shopkeeper': admin.VERTICAL,
        'aids_family_member': admin.VERTICAL,
        'aids_children': admin.VERTICAL,
        'aids_room_sharing': admin.VERTICAL,
        'aids_hiv_testing': admin.VERTICAL,
        'aids_hiv_times_tested': admin.VERTICAL,
        'tb_fever': admin.VERTICAL,
        'tb_fever_duration': admin.VERTICAL,
        'tb_night_sweat': admin.VERTICAL,
        'tb_night_sweat_duration': admin.VERTICAL,
        'tb_weight_loss': admin.VERTICAL,
        'tb_help': admin.VERTICAL,
        'tb_first_help': admin.VERTICAL,
        'tb_first_help_result': admin.VERTICAL,
        'tb_no_help': admin.VERTICAL,
        'diabetes_diagnosis': admin.VERTICAL,
        'diabetes_treatment': admin.VERTICAL,
        'cervical_cancer_screening': admin.VERTICAL,
        'last_cancer_test': admin.VERTICAL,
        'cancer_test_result': admin.VERTICAL,
        'cancer_treatment_referral': admin.VERTICAL}

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
                'aids_hiv_times_tested',
                'tb_fever_duration',
                'tb_night_sweat',
                'tb_night_sweat_duration',
                'tb_weight_loss',
                'tb_help',
                'tb_first_help',
                'tb_first_help_result',
                'tb_no_help',
                'diabetes_diagnosis',
                'diabetes_treatment',
                'cancer_test_result')},
         ),
        audit_fieldset_tuple
    )
