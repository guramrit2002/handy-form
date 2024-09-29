from ..models import FormAttribute, FieldAttributes, LayoutSizing, Border, Text, Visuals, FieldStyling
from django import forms


class FormAttributeForm(forms.ModelForm):
    class Meta:
        model = FormAttribute
        fields = '__all__'
        # exclude = ()


class FieldAttributesForm(forms.ModelForm):

    class Meta:
        model = FieldAttributes
        fields = '__all__'
        # exclude = ()


class LayoutSizingForm(forms.ModelForm):
    class Meta:
        model = LayoutSizing
        fields = '__all__'
        # exclude = ()


class BorderForm(forms.ModelForm):
    class Meta:
        model = Border
        fields = '__all__'
        # exclude = ()


class TextForm(forms.ModelForm):

    class Meta:
        model = Text
        fields = '__all__'
        # exclude = ()


class VisualForm(forms.ModelForm):

    class Meta:
        model = Visuals
        fields = '__all__'
        # exclude = ()


class FieldStylingForm(forms.ModelForm):

    class Meta:
        model = FieldStyling
        fields = '__all__'
        # exclude = ()