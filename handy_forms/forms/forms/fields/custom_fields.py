from django import forms
from django.forms.widgets import Widget


class CustomButtonWidget(Widget):

    def __init__(self, attrs=None):
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        # Combine attributes into the final HTML representation
        final_html = f'<button>Submit</button>'
        return final_html


class ButtonField(forms.Field):
    '''
    This class creates button field which is not provided by django itself
    '''
    widget = CustomButtonWidget()
