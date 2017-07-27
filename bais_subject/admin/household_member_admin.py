from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..forms import HouseholdMemberForm
from ..models import HouseholdMember


@admin.register(HouseholdMember)
class HouseholdMemberAdmin(admin.ModelAdmin):

    form = HouseholdMemberForm

    radio_fields = {
        'bedridden_member': admin.VERTICAL,
        'household_help': admin.VERTICAL,
        'household_help_received': admin.VERTICAL,
        'household_help_received': admin.VERTICAL,
        'household_help_received_from': admin.VERTICAL,
        'household_illness': admin.VERTICAL,
        'household_illness_support': admin.VERTICAL,
        'household_illness_help': admin.VERTICAL,
        'household_help_provider': admin.VERTICAL,
        'household_help_review': admin.VERTICAL,
        'household_deaths': admin.VERTICAL,
        'household_death_age': admin.VERTICAL,
        'household_death_cause': admin.VERTICAL,
        'household_time_sick': admin.VERTICAL}

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
                'household_death_age',
                'household_death_cause',
                'household_time_sick',)},
         ),
        audit_fieldset_tuple
    )
