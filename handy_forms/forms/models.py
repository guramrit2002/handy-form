from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Form(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    form_name = models.CharField(max_length=200,default=" ")
class Field(models.Model):
    
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
    
    form = models.ForeignKey(Form,on_delete=models.CASCADE)
    type = models.CharField(max_length=200,choices=FIELD_TYPE_CHOICES)
    name = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    required = models.BooleanField()
    
    def __str__(self) -> str:
        return self.name
    


# class MultipleField(models.Model):
#     form = 
#     name = models.CharField(max_length=200)
#     label = models.CharField(max_length=200)