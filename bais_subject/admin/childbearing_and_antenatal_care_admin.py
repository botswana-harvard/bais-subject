from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..forms import ChildbearingAndAntenatalCareForm
from ..models import ChildbearingAndAntenatalCare


@admin.register(ChildbearingAndAntenatalCare)
class ChildbearingAndAntenatalCareAdmin(admin.ModelAdmin):

    form = ChildbearingAndAntenatalCareForm

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
        ('Childbearing And Antenatal Care', {
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
