from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist

from edc_constants.constants import OTHER, DONT_KNOW

list_data = {
    'bais_subject.circumcissionreason': [
        ('HIV_PREVENTION', 'HIV prevention'),
        ('PEER_INFLUENCE', 'Peer influence'),
        ('CULTURAL_RIGHT', 'Cultural right'),
        ('HYGIENIC_REASON', 'Hygienic reason'),
        ('FASHION_COSMETIC', 'Fashion/Cosmetic'),
        ('RELIGION', 'Religion'),
        ('SEXUAL_PLEASURE', 'Sexual pleasure'),
        ('PARENTS_DECISION', 'Parents decision'),
        ('MEDICAL_REASONS', 'Medical reason (eg. STI)'),
        (DONT_KNOW, 'Don\'t know'),
        (OTHER, 'Other, specify'),
    ],
    'bais_subject.circumcissionintentreason': [
        ('HIV_PREVENTION', 'HIV prevention'),
        ('PEER_INFLUENCE', 'PEER influence'),
        ('CULTURAL_RIGHT', 'Cultural right'),
        ('HYGIENIC_REASON', 'Hygienic reason'),
        ('FASHION', 'Fashion'),
        ('RELIGION', 'Religion'),
        ('SEXUAL_PLEASURE', 'Sexual pleasure'),
        (OTHER, 'Other, specify'),
    ],
    'bais_subject.circumcissionrejectreason': [
        ('FEAR', 'Fear'),
        ('CULTURE', 'Culture'),
        ('RELIGION', 'Religion'),
        ('SPOUSE_CONSENT', 'Spouse consent'),
        ('PARENTAL_CONSENT', 'Parental consent'),
        ('LONG_DURATION_OF_HEALING_PERIOD',
         'Long duration of healing period'),
        ('FEAR_OF_HIV_TEST', 'Fear of HIV test'),
        (OTHER, 'Other, specify'),
    ],
    'bais_subject.stisymptoms': [
        ('LOWER_ABDOMINAL_PAIN', 'Lower abdominal pain'),
        ('OFFENSIVE_DISCHARGE_SMELL_FROM_VAGINA_PENIS',
         'Offensive discharge smell from vagina/penis'),
        ('VAGINAL_DISCHARGE', 'Vaginal discharge'),
        ('ITCHING_IN_GENITAL_AREA', 'Itching in genital area'),
        ('BURNING_PAIN_ON_URINATION', 'Burning pain on urination'),
        ('PAIN_DURING_INTERCOURSE', 'Pain during intercourse'),
        ('GENITAL_ULCERS_OPEN_SORES', 'Genital ulcers/open sores'),
        ('SWELLINGS_IN_GENITAL_AREA', 'Swellings in genital area'),
        ('NO_SYMPTOMS', 'No symptoms'),
        (DONT_KNOW, 'Don\'t Know'),
        (OTHER, 'Other, specify'),
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
