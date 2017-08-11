from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist

from edc_constants.constants import OTHER, DONT_KNOW

list_data = {
    'bais_subject.circumcissionreason': [
        ('HIV_PREVENTION', 'HIV PREVENTION'),
        ('PEER_INFLUENCE', 'PEER INFLUENCE'),
        ('CULTURAL_RIGHT', 'CULTURAL RIGHT'),
        ('HYGIENIC_REASON', 'HYGIENIC REASON'),
        ('FASHION_COSMETIC', 'FASHION/COSMETIC'),
        ('RELIGION', 'RELIGION'),
        ('SEXUAL_PLEASURE', 'SEXUAL PLEASURE'),
        ('PARENTS_DECISION', 'PARENTS DECISION'),
        ('MEDICAL_REASONS', 'MEDICAL REASONS (eg. STI)'),
        (DONT_KNOW, 'DON’T KNOW'),
        (OTHER, 'OTHER'),
    ],
}


for list_obj in list_data.keys():
    try:
        model = django_apps.get_app_config(
            list_obj.split('.')[0]).get_model(list_obj.split('.')[1])
        for tpl in list_data.get(list_obj):
            short_name, display_value = tpl
            try:
                obj = model.objects.get(short_name=short_name)
            except ObjectDoesNotExist:
                model.objects.create(short_name=short_name,
                                     name=display_value)
            else:
                obj.name = display_value
                obj.save()
    except Exception as e:
        print(e)
