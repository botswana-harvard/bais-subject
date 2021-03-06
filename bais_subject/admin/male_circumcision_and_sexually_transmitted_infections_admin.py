from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..forms import (
    MaleCircumcissionAndSexuallyTransmittedInfectionsForm)
from ..models import MaleCircumcissionAndSexuallyTransmittedInfections


@admin.register(MaleCircumcissionAndSexuallyTransmittedInfections)
class MaleCircumcissionAndSexuallyTransmittedInfectionsAdmin(
        admin.ModelAdmin):

    form = MaleCircumcissionAndSexuallyTransmittedInfectionsForm

    filter_horizontal = (
        'circumcission_reason',
        'circumcission_intent_reason',
        'circumcission_reject_reason',
        'sti_symptoms',)

    radio_fields = {
        'circumcission': admin.VERTICAL,
        #         'circumcission_reason': admin.VERTICAL,
        'circumcission_place': admin.VERTICAL,
        'circumcised_complications': admin.VERTICAL,
        'circumcission_intent': admin.VERTICAL,
        #         'circumcission_intent_reason': admin.VERTICAL,
        #         'circumcission_reject_reason': admin.VERTICAL,
        #         'sti_symptoms': admin.VERTICAL,
    }

    fieldsets = (
        ('Male Circumcission And Sexually Transmitted Infections', {
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
