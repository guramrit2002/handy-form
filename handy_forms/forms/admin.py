from django.contrib import admin
from .models import Field, Form, FormAttribute, FieldStyling
# Register your models here.

admin.site.register(Field)
admin.site.register(Form)
admin.site.register(FormAttribute)
admin.site.register(FieldStyling)