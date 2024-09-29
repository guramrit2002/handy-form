from django import forms
from .fields.custom_fields import ButtonField

class DynamicForm(forms.Form):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', [])
        print("fields : ", fields)
        super(DynamicForm, self).__init__(*args, **kwargs)

        # Dynamically add fields to the form
        for field in fields:
            print("field object : ")
            print(field)
            print("text is chosen")
            field_type = field.get("type")
            field_name = field.get("name")
            field_label = field.get("label")
            field_choices = field.get('choices', [])
            field_regex = field.get('choices', [])
            print("field name : ")
            print(field_name)
            print(field_type)
            if field_type == 'text':
                print("text is chosen check")
                if field_regex:
                    self.fields[field_name] = forms.RegexField(required=True, regex=field_regex)
                else:
                    self.fields[field_name] = forms.CharField(label=field_label, required=True)

            elif field_type == 'email':
                self.fields[field_name] = forms.EmailField(label=field_label, required=True)
            elif field_type == 'number':
                self.fields[field_name] = forms.IntegerField(label=field_label, required=True)
            elif field_type == 'float':
                self.fields[field_name] = forms.FloatField(label=field_label, required=True)
            elif field_type == 'date':
                self.fields[field_name] = forms.DateField(label=field_label, required=True)
            elif field_type == 'datetime':
                self.fields[field_name] = forms.DateTimeField(label=field_label, required=True)
            elif field_type == 'bool':
                self.fields[field_name] = forms.BooleanField(label=field_label, required=True)
            elif field_type == 'dropdown':
                self.fields[field_name] = forms.ChoiceField(label=field_label, choices=field_choices, required=True)
            elif field_type == 'url':
                self.fields[field_name] = forms.URLField(label=field_label, required=True)
            elif field_type == 'file':
                self.fields[field_name] = forms.FileField(label=field_label, required=True)
            elif field_type == 'image':
                self.fields[field_name] = forms.ImageField(label=field_label, required=True)
            elif field_type == 'multiple_choice':
                self.fields[field_name] = forms.MultipleChoiceField(choices=field_choices, required=True)
            elif field_type == 'button':
                self.fields[field_name] = ButtonField(label="")
