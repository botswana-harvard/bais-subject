from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..forms import Section2Form
from ..models import Section2


@admin.register(Section2)
class Section2Admin(admin.ModelAdmin):

    form = Section2Form

    radio_fields = {
        'taken_alcohol': admin.VERTICAL,
        'substance_method_alcohol': admin.VERTICAL,
        'substance_frequency_alcohol': admin.VERTICAL,
        'taken_tobacco': admin.VERTICAL,
        'substance_method_tobacco': admin.VERTICAL,
        'substance_frequency_tobacco': admin.VERTICAL,
        'taken_marijuana': admin.VERTICAL,
        'substance_method_marijuana': admin.VERTICAL,
        'substance_frequency_marijuana': admin.VERTICAL,
        'taken_cocaine': admin.VERTICAL,
        'substance_method_cocaine': admin.VERTICAL,
        'substance_frequency_cocaine': admin.VERTICAL,
        'taken_crack': admin.VERTICAL,
        'substance_method_crack': admin.VERTICAL,
        'substance_frequency_crack': admin.VERTICAL,
        'taken_meth': admin.VERTICAL,
        'substance_method_meth': admin.VERTICAL,
        'substance_frequency_meth': admin.VERTICAL,
        'taken_nyaope': admin.VERTICAL,
        'substance_method_nyaope': admin.VERTICAL,
        'substance_frequency_nyaope': admin.VERTICAL,
        'taken_heroine': admin.VERTICAL,
        'substance_method_heroine': admin.VERTICAL,
        'substance_frequency_heroine': admin.VERTICAL,
        'taken_ecstasy': admin.VERTICAL,
        'substance_method_ecstasy': admin.VERTICAL,
        'substance_frequency_ecstacy': admin.VERTICAL,
        'taken_codeine': admin.VERTICAL,
        'substance_method_codeine': admin.VERTICAL,
        'substance_frequency_codeine': admin.VERTICAL}

    fieldsets = (
        ('Section 2', {
            'fields': (
                'taken_alcohol',
                'substance_method_alcohol',
                'substance_age_alcohol',
                'substance_frequency_alcohol',
                'taken_tobacco',
                'substance_method_tobacco',
                'substance_age_tobacco',
                'substance_frequency_tobacco',
                'taken_marijuana',
                'substance_method_marijuana',
                'substance_age_marijuana',
                'substance_frequency_marijuana',
                'taken_cocaine',
                'substance_method_cocaine',
                'substance_age_cocaine',
                'substance_frequency_cocaine',
                'taken_crack',
                'substance_method_crack',
                'substance_age_crack',
                'substance_frequency_crack',
                'taken_meth',
                'substance_method_meth',
                'substance_age_meth',
                'substance_frequency_meth',
                'taken_nyaope',
                'substance_method_nyaope',
                'substance_age_nyaope',
                'substance_frequency_nyaope',
                'taken_heroine',
                'substance_method_heroine',
                'substance_age_heroine',
                'substance_frequency_heroine',
                'taken_ecstasy',
                'substance_method_ecstasy',
                'substance_age_ecstacy',
                'substance_frequency_ecstacy',
                'taken_codeine',
                'substance_method_codeine',
                'substance_age_codeine',
                'substance_frequency_codeine',
                'substance_other',
                'passive_smoke',
                'message',)},
         ),
        audit_fieldset_tuple
    )
