from django.db import models
from django.contrib.auth.models import User
# Create your models here.
FIELD_TYPE_CHOICES = (
    ('text', 'Text'),
    ('email', 'Email'),
    ('number', 'Number'),
    ('float', 'Float'),
    ('date', 'Date'),
    ('datetime', 'DateTime'),
    ('boolean', 'Boolean'),
    ('choice', 'Choice'),
    ('url', 'URL'),
    ('file', 'File'),
    ('image', 'Image'),
)


class Form(models.Model):
    '''
    
    '''
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    form_name = models.CharField(max_length=200)
    
class FormAttribute(models.Model):
    form = models.OneToOneField(Form,on_delete=models.CASCADE)
    action = models.CharField(max_length=2048)
    target = models.CharField(max_length=200)
    method = models.CharField(max_length=4)
    
    
class Field(models.Model):
    

    '''
    {
        "form":{
            "form_name":"",
            "attributes":{
                "action":"",
                "target":"",
                "method":""
            }
        }
        "fields":[
            {
                "id":1,
                "form":"",
                "type":"",
                "name":"",
                "label":"",
                "attributes":{
                    "value":"",
                    "readonly":False,
                    "disabled":False,
                    "size":0,
                    "maxlength":0,
                    "min":0,
                    "max":0,
                    "multiple":False,
                    "pattern":"",
                    "placeholder":"",
                    "autofocus":False,
                    "autocomplete":False,
                    "required":False,
                    "height":0,
                    "width":0,
                }
                
            },
            {
                "id":2,
                "form":"",
                "type":"",
                "name":"",
                "label":"",
                "attributes":{
                    "value":"",
                    "readonly":False,
                    "disabled":False,
                    "size":0,
                    "maxlength":0,
                    "min":0,
                    "max":0,
                    "multiple":False,
                    "pattern":"",
                    "placeholder":"",
                    "autofocus":False,
                    "autocomplete":False,
                    "required":False,
                    "height":0,
                    "width":0,
                }
                
            }
            
        ]
    }
    '''
    
    form = models.ForeignKey(Form,on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=FIELD_TYPE_CHOICES)
    
    def __str__(self) -> str:
        return self.name
    
class FieldAttributes(models.Model):
    '''
    Readonly --> there should be "value"
    min and max --> these are for numeric values to compare
    multiple --> workes with email and file.
    pattern --> works with ext, date, search, url, tel, email, and password.
    placeholder --> will work with text, search, url, number, tel, email, and password.
    required --> works with text, search, url, tel, email, password, date pickers, number, checkbox, radio, and file.
    height and width --> works with text, search, url, tel, email, password, date pickers, number, checkbox, radio, and file.
    autocomplete --> works with text, search, url, tel, email, password, datepickers, range, and color.
    '''
    SIZE_CHART = (
        ('QUARTER',25),
        ('HALF',50),
        ('FULL',100)
    )
    field = models.OneToOneField(Field,on_delete=models.CASCADE)
    value = models.CharField(max_length=200)
    readonly = models.BooleanField()
    disabled = models.BooleanField()
    size = models.CharField(max_length=200,choices=SIZE_CHART)
    maxlength = models.PositiveIntegerField()
    min = models.PositiveIntegerField()
    max = models.PositiveIntegerField()
    multiple = models.BooleanField()
    pattern = models.CharField(max_length=200)
    placeholder = models.CharField(max_length=200)
    autofocus = models.BooleanField()
    autocomplete = models.BooleanField()
    required = models.BooleanField()
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
class LayoutSizing(models.Model):
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    padding = models.PositiveIntegerField()
    margin = models.PositiveIntegerField()
    display = models.PositiveIntegerField()
class Border(models.Model):
    BORDER_STYLE = (
        ('dotted','dotted'),
        ('dashed','dashed'),
        ('solid','solid'),
        ('double','double'),
        ('none','none')
    )
    border = models.CharField(max_length=200)
    border_radius = models.PositiveIntegerField()
    border_color = models.CharField(max_length=200)
    border_style = models.CharField(max_length=200,choices=BORDER_STYLE)
class Background(models.Model):
    background_color = models.CharField(max_length=200)
    background_size = models.CharField(max_length=200)
    background_position = models.CharField(max_length=200)
class Text(models.Model):
    ALIGN_TYPE = (
        ('LEFT','LEFT'),
        ('RIGHT','RIGHT'),
        ('CENTER','CENTER'),
        ('JUSTIFY','JUSTIFY')
    )
    TRANSFORM_TYPE = (
        ('UPPERCASE','UPPERCASE'),
        ('LOWERCASE','LOWERCASE'),
        ('CAPITALIZE','CAPITALIZE')
    )
    font_size = models.CharField(max_length=200)
    font_family = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    text_align = models.CharField(max_length=200,choices=ALIGN_TYPE)
    text_transform = models.CharField(max_length=200,choices=TRANSFORM_TYPE)
    letter_spacing = models.PositiveIntegerField()
    line_height = models.PositiveIntegerField()
class Visuals(models.Model):
    box_shadow = models.CharField(max_length=200)
    opacity = models.PositiveIntegerField()
    visibility = models.PositiveIntegerField()
class FieldStyling(models.Model):
    field = models.ForeignKey(Field,on_delete=models.CASCADE)
    layout = models.OneToOneField(LayoutSizing,on_delete=models.CASCADE)
    border = models.OneToOneField(Border,on_delete=models.CASCADE)
    text = models.OneToOneField(Text,on_delete=models.CASCADE)
    visuals = models.OneToOneField(Visuals,on_delete=models.CASCADE)