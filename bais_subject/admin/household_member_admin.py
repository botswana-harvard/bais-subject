from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import bais_subject_admin
from ..forms import HouseholdMemberForm


@admin.register(HouseholdMember site=bais_subject_admin)
class HouseholdMemberAdmin(admin.ModelAdmin):

    form = HouseholdMemberForm

    radio_fields = {
        'bedridden_member': admin.VERTICAL,
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
        ('Household Member', {
            'fields': (
                'bedridden_member',
                'member_age',
                'household_help',
                'household_help_received',
                'household_help_received_from',
                'household_illness',
                'household_illness_support',
                'household_illness_help',
                ' household_help_provider',
                'household_help_review',
                'household_deaths',
                ' household_deaths_review',
                'household_death_name',
                'phousehold_death_age',
                'household_death_cause',
                'household_time_sick',)},
         ),
        audit_fieldset_tuple
    )
