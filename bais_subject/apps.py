from django.apps import AppConfig as DjangoApponfig
from django.conf import settings

from datetime import datetime
from dateutil.tz import gettz

from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_device.constants import CENTRAL_SERVER, SERVER
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig, SubjectType, Cap


class AppConfig(DjangoApponfig):
    name = 'bais_subject'


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP093'
    protocol_number = '093'
    protocol_name = 'BAIS'
    protocol_title = ''
    study_open_datetime = datetime(2016, 12, 31, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(2019, 12, 31, 0, 0, 0, tzinfo=gettz('UTC'))

    @property
    def site_name(self):
        return 'Gaborone'

    @property
    def site_code(self):
        return '40'


class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
    device_role = CENTRAL_SERVER
    device_id = '99'
