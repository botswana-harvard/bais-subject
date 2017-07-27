from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import bais_subject_admin
from ..forms import Section7Form
from ..models import Section7


@admin.register(Section7, site=bais_subject_admin)
class Section7Admin(admin.ModelAdmin):

    form = Section7Form

    radio_fields = {
        'given_birth': admin.VERTICAL,
        'given_birth_past_5yrs': admin.VERTICAL,
        'baby_hiv_test': admin.VERTICAL,
        'baby_feeding': admin.VERTICAL,
        'currently_pregnant': admin.VERTICAL,
        'ante_natal_clinic_test': admin.VERTICAL,
        'ante_natal_clinic_partner_test': admin.VERTICAL,
    }

    fieldsets = (
        ('Section 7', {
            'fields': (
                'given_birth',
                'given_birth_past_5yrs',
                'baby_dob',
                'baby_hiv_test',
                'baby_feeding',
                'currently_pregnant',
                'ante_natal_clinic_test',
                'ante_natal_clinic_partner_test',)},
         ),
        audit_fieldset_tuple
    )
