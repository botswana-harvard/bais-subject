from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import bais_subject_admin
from ..forms import Section8Form
from ..models import Section8


@admin.register(Section8, site=bais_subject_admin)
class Section8Admin(admin.ModelAdmin):

    form = Section8Form

    radio_fields = {
        'tb_current_treatment': admin.VERTICAL,
        'tb_treatment_source': admin.VERTICAL,
        'tb_previous_treatment': admin.VERTICAL,
        'tb_treatment_date': admin.VERTICAL,
        'tb_cough': admin.VERTICAL,
        'tb_cough_duration': admin.VERTICAL,
        'tb_cough_sputum': admin.VERTICAL,
        'tb_bloody_sputum': admin.VERTICAL,
        'tb_sputum_sample': admin.VERTICAL,
        'tb_sputum_sample_result': admin.VERTICAL,
        'tb_fever': admin.VERTICAL,
        'tb_sputum_sample_result': admin.VERTICAL,
        'tb_night_sweat': admin.VERTICAL,
        'tb_night_sweat_other': admin.VERTICAL,
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
