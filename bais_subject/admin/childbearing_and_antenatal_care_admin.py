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
        'baby_hiv_test_result': admin.VERTICAL,
        'baby_arv': admin.VERTICAL,
        'baby_feeding': admin.VERTICAL,
        'currently_pregnant': admin.VERTICAL,
        'ante_natal_clinic': admin.VERTICAL,
        'ante_natal_clinic_none': admin.VERTICAL,
        'ante_natal_clinic_test': admin.VERTICAL,
        'ante_natal_clinic_partner_test': admin.VERTICAL,
        'ante_natal_clinic_test_result': admin.VERTICAL,
        'ante_natal_clinic_partner_test_result': admin.VERTICAL
    }

    fieldsets = (
        ('Childbearing And Antenatal Care', {
            'fields': (
                'given_birth',
                'given_birth_past_5yrs',
                'baby_dob',
                'baby_hiv_test',
                'baby_hiv_test_result',
                'baby_arv',
                'baby_feeding',
                'currently_pregnant',
                'ante_natal_clinic',
                'ante_natal_clinic_none',
                'ante_natal_clinic_none_other',
                'ante_natal_clinic_test',
                'ante_natal_clinic_test_result',
                'ante_natal_clinic_partner_test',
                'ante_natal_clinic_partner_test_result')},
         ),
        audit_fieldset_tuple
    )
