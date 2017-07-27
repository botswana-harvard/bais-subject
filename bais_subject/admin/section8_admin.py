from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..forms import Section8Form
from ..models import Section8


@admin.register(Section8)
class Section8Admin(admin.ModelAdmin):

    form = Section8Form

    radio_fields = {
        'tb_current_treatment': admin.VERTICAL,
        'tb_treatment_source': admin.VERTICAL,
        'tb_previous_treatment': admin.VERTICAL,
        'tb_previous_times_treated': admin.VERTICAL,
        'tb_cough': admin.VERTICAL,
        'tb_cough_duration': admin.VERTICAL,
        'tb_cough_sputum': admin.VERTICAL,
        'tb_bloody_sputum': admin.VERTICAL,
        'tb_sputum_sample': admin.VERTICAL,
        'tb_sputum_sample_result': admin.VERTICAL,
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
        ('Section 8', {
            'fields': (
                'tb_current_treatment',
                'tb_previous_treatment',
                'tb_previous_times_treated',
                'tb_treatment_date',
                'tb_cough',
                'tb_cough_duration',
                'tb_cough_sputum',
                'tb_bloody_sputum',
                'tb_sputum_sample',
                'tb_fever',
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
