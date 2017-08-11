from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..forms import Section4Form
from ..models import Section4


@admin.register(Section4)
class Section4Admin(admin.ModelAdmin):

    form = Section4Form

    filter_horizontal = ('circumcission_reason',)

    radio_fields = {
        'circumcission': admin.VERTICAL,
        #         'circumcission_reason': admin.VERTICAL,
        'circumcission_place': admin.VERTICAL,
        'circumcised_complications': admin.VERTICAL,
        'circumcission_intent': admin.VERTICAL,
        'circumcission_intent_reason': admin.VERTICAL,
        'circumcission_reject_reason': admin.VERTICAL,
        'sti_symptoms': admin.VERTICAL, }

    fieldsets = (
        ('Section 4', {
            'fields': (
                'circumcission',
                'circumcission_year',
                'circumcission_reason',
                'circumcission_place',
                'circumcised_complications',
                'circumcission_intent',
                'circumcission_intent_reason',
                'circumcission_intent_reason_other',
                'circumcission_reject_reason',
                'circumcission_reject_reason_other',
                'sti_symptoms',
                'sti_symptoms_other',)},
         ),
        audit_fieldset_tuple
    )
