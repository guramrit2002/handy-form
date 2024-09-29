from rest_framework import serializers
from .models import Field, Form, FormAttribute,FieldAttributes


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

class FormAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FormAttribute
        fields = '__all__'

class MasterFormSerializer(serializers.Serializer):
    form = FormSerializer()
    form_attribute = FormAttributeSerializer()



class Fieldserialiser(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('name', 'label')

class FieldAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldAttributes
        fields = '__all__'
