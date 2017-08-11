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
    'bais_subject.circumcissionintentreason': [
        ('HIV_PREVENTION', 'HIV PREVENTION'),
        ('PEER_INFLUENCE', 'PEER INFLUENCE'),
        ('CULTURAL_RIGHT', 'CULTURAL RIGHT'),
        ('HYGIENIC_REASON', 'HYGIENIC REASON'),
        ('FASHION', 'FASHION'),
        ('RELIGION', 'RELIGION'),
        ('SEXUAL_PLEASURE', 'SEXUAL PLEASURE'),
        (OTHER, 'OTHER'),
    ],
    'bais_subject.circumcissionrejectreason': [
        ('FEAR', 'FEAR'),
        ('CULTURE', 'CULTURE'),
        ('RELIGION', 'RELIGION'),
        ('SPOUSE_CONSENT', 'SPOUSE CONSENT'),
        ('PARENTAL_CONSENT', 'PARENTAL CONSENT'),
        ('LONG_DURATION_OF_HEALING_PERIOD', 'LONG DURATION OF HEALING PERIOD'),
        ('FEAR_OF_HIV_TEST', 'FEAR OF HIV TEST'),
        (OTHER, 'OTHER'),
    ],
    'bais_subject.stisymptoms': [
        ('LOWER_ABDOMINAL_PAIN', 'LOWER ABDOMINAL PAIN'),
        ('OFFENSIVE_DISCHARGE_SMELL_FROM_VAGINA_PENIS',
            'OFFENSIVE DISCHARGE/SMELL FROM VAGINA/PENIS'),
        ('VAGINAL_DISCHARGE', 'VAGINAL DISCHARGE'),
        ('ITCHING_IN_GENITAL_AREA', 'ITCHING IN GENITAL AREA'),
        ('BURNING_PAIN_ON_URINATION', 'BURNING PAIN ON URINATION'),
        ('PAIN_DURING_INTERCOURSE', 'PAIN DURING INTERCOURSE'),
        ('GENITAL_ULCERS_OPEN_SORES', 'GENITAL ULCERS/OPEN SORES'),
        ('SWELLINGS_IN_GENITAL_AREA', 'SWELLINGS IN GENITAL AREA'),
        ('NO_SYMPTOMS', 'NO SYMPTOMS'),
        (DONT_KNOW, 'Don\'t Know'),
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
