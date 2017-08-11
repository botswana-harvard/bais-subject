from edc_base.model_mixins import ListModelMixin, BaseUuidModel


class CircumcissionReason(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'bais_subject'


class CircumcissionIntentReason(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'bais_subject'


class CircumcissionRejectReason(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'bais_subject'


class StiSymptoms(ListModelMixin, BaseUuidModel):

    class Meta(ListModelMixin.Meta):
        app_label = 'bais_subject'
