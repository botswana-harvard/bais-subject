from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..forms import HouseholdQuestionnaireForm
from ..models import HouseholdQuestionnaire

# TODO: confirm the syntax


@admin.register(HouseholdQuestionnaire)
class HouseholdQuestionnaireAdmin(admin.ModelAdmin):

    form = HouseholdQuestionnaireForm

    radio_fields = {
        'person_household_head_rel': admin.VERTICAL,
        'person_gender': admin.VERTICAL,
        'person_citizenship': admin.VERTICAL,
        'person_household_live': admin.VERTICAL,
        'person_marital_status': admin.VERTICAL,
        'person_biological_mother_alive': admin.VERTICAL,
        'person_biological_mother_household_live': admin.VERTICAL,
        'person_biological_father_alive': admin.VERTICAL,
        'person_biological_father_household_live': admin.VERTICAL,
        'person_attended_school': admin.VERTICAL,
        'person_currently_studying': admin.VERTICAL,
        'person_highest_study_level': admin.VERTICAL,
        'person_work_profit': admin.VERTICAL,
        'person_work_unpaid': admin.VERTICAL,
        'person_work_unpaid_reason': admin.VERTICAL,
        'person_main_work': admin.VERTICAL}

    fieldsets = (
        ('Household Questionnaire', {
            'fields': (
                'persons_list',
                'person_household_head_rel',
                'person_gender',
                'person_age',
                'person_citizenship',
                'person_citizenship_other',
                'person_household_live',
                'person_marital_status',
                'person_biological_mother_alive',
                'person_biological_mother_household_live',
                'person_biological_father_alive',
                'person_biological_father_household_live',
                'person_attended_school',
                'person_currently_studying',
                'person_highest_study_level',
                'person_work_profit',
                'person_work_unpaid',
                'person_work_unpaid_reason',
                'person_work_unpaid_reason_other',
                'person_main_work',
                'person_work_type',
                'person_work_product',)},
         ),
        audit_fieldset_tuple
    )
