from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import bais_subject_admin
from ..forms import Section3Form
from ..models import Section3


@admin.register(Section3, site=bais_subject_admin)
class Section3Admin(admin.ModelAdmin):

    form = Section3Form

    radio_fields = {
        'sexual_intercouse': admin.VERTICAL,
        'sexual_intercouse_consent': admin.VERTICAL,
        'sexual_intercourse_influence': admin.VERTICAL,
        'sexual_intercouse_protection': admin.VERTICAL,
        'sexual_intercouse_protection_use': admin.VERTICAL,
        'sexual_intercouse_protection_reason': admin.VERTICAL,
        'sex_recently': admin.VERTICAL,
        'sex_consentual': admin.VERTICAL,
        'sex_with_whom': admin.VERTICAL,
        'assistance': admin.VERTICAL,
        'physical_sexual_violance_male': admin.VERTICAL,
        'physical_sexual_violance_female': admin.VERTICAL,
        'physical_sexual_violance_who': admin.VERTICAL,
        'partners_serial_concurrent': admin.VERTICAL,
        'condom_main_reason_partner1': admin.VERTICAL,
        'condom_main_reason_partner2': admin.VERTICAL,
        'condom_main_reason_partner3': admin.VERTICAL,
        'condom_not_used_reason_partner1': admin.VERTICAL,
        'condom_not_used_reason_partner2': admin.VERTICAL,
        'condom_not_used_reason_partner3': admin.VERTICAL,
        'condom_place_partner1': admin.VERTICAL,
        'condom_place_partner2': admin.VERTICAL,
        'condom_place_partner3': admin.VERTICAL,
        'drunk_high_sex_partner1': admin.VERTICAL,
        'drunk_high_sex_partner2': admin.VERTICAL,
        'drunk_high_sex_partner3': admin.VERTICAL,
        'partner_other_partners_partner1': admin.VERTICAL,
        'partner_other_partners_partner2': admin.VERTICAL,
        'partner_other_partners_partner3': admin.VERTICAL,
        'sexual_partner_recent1': admin.VERTICAL,
        'sexual_partner_recent2': admin.VERTICAL,
        'sexual_partner_recent3': admin.VERTICAL,
        'paid_for_sex': admin.VERTICAL,
        'persuade_sex_partner': admin.VERTICAL,
        'persuade_sex_partner_not': admin.VERTICAL,
        'multiple_sex_partner_man': admin.VERTICAL,
        'multiple_sex_partner_woman': admin.VERTICAL}

    fieldsets = (
        ('Section 3', {
            'fields': (
                'sexual_intercouse',
                'sexual_intercourse_age',
                'sexual_intercouse_consent',
                'sexual_intercourse_influence',
                'sexual_intercourse_influence_other',
                'sexual_intercouse_protection',
                'sexual_intercouse_protection_use',
                'sexual_intercouse_protection_use_other',
                'sexual_intercouse_protection_reason',
                'sexual_intercouse_protection_reason_other',
                'sex_recently',
                'sex_consentual',
                'sex_with_whom',
                'sex_with_whom_other',
                'assistance',
                'assistance_other',
                'physical_sexual_violance_male',
                'physical_sexual_violance_female',
                'physical_sexual_violance_who',
                'sex_partners_count',
                'partners_serial_concurrent',
                'partners_serial_concurrent_explain',
                'condom_main_reason_partner1',
                'condom_main_reason_partner2',
                'condom_main_reason_partner3',
                'condom_not_used_reason_partner1',
                'condom_not_used_reason_partner1_other',
                'condom_not_used_reason_partner2',
                'condom_not_used_reason_partner2_other',
                'condom_not_used_reason_partner3',
                'condom_not_used_reason_partner3_other',
                'condom_place_partner1',
                'condom_place_partner1_other',
                'condom_place_partner2',
                'condom_place_partner2_other',
                'condom_place_partner3',
                'condom_place_partner3_other',
                'drunk_high_sex_partner1',
                'drunk_high_sex_partner2',
                'drunk_high_sex_partner3',
                'partner_other_partners_partner1',
                'partner_other_partners_partner2',
                'partner_other_partners_partner3',
                'sexual_partner_recent1',
                'sexual_partner_recent2',
                'sexual_partner_recent3',
                'paid_for_sex',
                'persuade_sex_partner',
                'persuade_sex_partner_not',
                'multiple_sex_partner_man',
                'multiple_sex_partner_woman',)},
         ),
        audit_fieldset_tuple
    )
