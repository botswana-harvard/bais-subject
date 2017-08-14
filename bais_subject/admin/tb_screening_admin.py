from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..forms import TBScreeningForm
from ..models import TBScreening


@admin.register(TBScreening)
class TBScreeningAdmin(admin.ModelAdmin):

    form = TBScreeningForm

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
        'tb_sputum_sample_no_result': admin.VERTICAL,
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
        ('TB Screening', {
            'fields': (
                'tb_current_treatment',
                'tb_treatment_source',
                'tb_previous_treatment',
                'tb_previous_times_treated',
                'tb_treatment_date',
                'tb_cough',
                'tb_cough_duration',
                'tb_cough_sputum',
                'tb_bloody_sputum',
                'tb_sputum_sample',
                'tb_sputum_sample_result',
                'tb_sputum_sample_result_other',
                'tb_sputum_sample_no_result',
                'tb_sputum_sample_no_result_other',
                'tb_fever',
                'tb_fever_duration',
                'tb_fever_duration_other',
                'tb_night_sweat',
                'tb_night_sweat_duration',
                'tb_weight_loss',
                'tb_help',
                'tb_first_help',
                'tb_first_help_other',
                'tb_first_help_result',
                'tb_first_help_result_other',
                'tb_no_help',
                'diabetes_diagnosis',
                'diabetes_treatment',
                'cervical_cancer_screening',
                'last_cancer_test',
                'last_cancer_test_other',
                'cancer_test_result',
                'cancer_treatment_referral')},
         ),
        audit_fieldset_tuple
    )
