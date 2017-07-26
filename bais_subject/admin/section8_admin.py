from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import bais_subject_admin
from ..forms import Section8Form
from ..models import Section8


@admin.register(Section8, site=bais_subject_admin)
class Section8Admin(admin.ModelAdmin):

    form = Section8Form

    radio_fields = {
        'tb_current_treatment': admin.VERTICAL,
        'tb_treatment_source': admin.VERTICAL,
        'tb_previous_treatment': admin.VERTICAL,
    }
