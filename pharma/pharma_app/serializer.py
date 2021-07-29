from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from pharma_app.models import Pharma, Drug


class DrugSerializer(ModelSerializer):
    class Meta:
        model = Drug
        fields = ['drugName', 'condition', 'review', 'date']


class DynamicFieldsModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.

    See:
        http://tomchristie.github.io/rest-framework-2-docs/api-guide/serializers
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class PharmaSerializer(DynamicFieldsModelSerializer, HyperlinkedModelSerializer):

    class Meta:
        model = Pharma
        fields = '__all__'
