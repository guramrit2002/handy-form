from rest_framework import serializers
from .models import Field
from django import forms

class DynamicForm(forms.Form):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', [])
        super(DynamicForm, self).__init__(*args, **kwargs)
        
        # Dynamically add fields to the form
        print(fields)
        for field in fields:
            print(field)
            field_type = field.get("type")
            field_name = field.get("name")
            field_label = field.get("label")
            field_required = True if field.get("required") else False
            # field_choices = field.get('choices', [])

            if field_type == 'text':
                self.fields[field_name] = forms.CharField(label=field_label, required=field_required)
            elif field_type == 'email':
                self.fields[field_name] = forms.EmailField(label=field_label, required=field_required)
            elif field_type == 'number':
                self.fields[field_name] = forms.IntegerField(label=field_label, required=field_required)
            elif field_type == 'float':
                self.fields[field_name] = forms.FloatField(label=field_label, required=field_required)
            elif field_type == 'date':
                self.fields[field_name] = forms.DateField(label=field_label, required=field_required)
            elif field_type == 'datetime':
                self.fields[field_name] = forms.DateTimeField(label=field_label, required=field_required)
            elif field_type == 'boolean':
                self.fields[field_name] = forms.BooleanField(label=field_label, required=field_required)
            elif field_type == 'choice':
                self.fields[field_name] = forms.ChoiceField(label=field_label, choices=field_choices, required=field_required)
            elif field_type == 'url':
                self.fields[field_name] = forms.URLField(label=field_label, required=field_required)
            elif field_type == 'file':
                self.fields[field_name] = forms.FileField(label=field_label, required=field_required)
            elif field_type == 'image':
                self.fields[field_name] = forms.ImageField(label=field_label, required=field_required)
            
class Fieldserialiser(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields=('name','label','required')

# class MultiplOptionField(serializers.ModelSerializer):
#     class Meta:
#         model = MultipleField
#         pass
    