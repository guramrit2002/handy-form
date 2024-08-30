from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.viewsets import ViewSet
from rest_framework import status
from .serializers import DynamicForm,Fieldserialiser
from .models import Field,Form
from django.shortcuts import redirect

class FormCreate(ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'forms_template/form.html'
    
    fields = [
        {'type': 'text', 'name': 'first_name', 'label': 'First Name', 'required': True},
        {'type': 'email', 'name': 'email', 'label': 'Email Address', 'required': True},
    ]
    
    def list(self, request):
        fields = Field.objects.all().values()
        form = DynamicForm(fields=fields)
        print('------------------------form ',form)
        return Response({"serializer": form}, template_name=self.template_name, status=status.HTTP_200_OK)
    
class FieldView(ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'forms_template/new_form.html'
    
    def get_fields(self,id):
        values = ['id','name','type','required','form__id','form__form_name','form__created_by']
        fields_query = Field.objects.select_related("form").filter(form__id=id).values(*values)
        field_ = fields_query[0]
        form = {
                    "id":field_.get('form_id'),
                    "name":field_.get('form__form_name'),
                    "created_by":field_.get('created_by'),
                }
        fields_ = []
        for field in fields_query:
            fields = {
                "id":field.get("id"),
                "type":field.get("type"),
                "name":field.get("name"),
                "label":field.get("label"),
                "required":field.get("required")
            }
            fields_.append(fields)
        return {
            "form":form,
            "fields":fields_
        }
    
    def list(self, request,form_id):
        fields = self.get_fields(form_id)
        form = Fieldserialiser()
        _form = DynamicForm(fields=fields.get('fields'))
        return Response({"serializer": form,"form": _form,"method":"get"}, template_name=self.template_name, status=status.HTTP_200_OK)
    
    def create(self, request,form_id):
        fields = self.get_fields(form_id)
        print(fields)
        data_to_serializer = {
            "name":request.data.get('name'),
            "label":request.data.get('label'),
            "required":True if request.data.get("required") else False
        } 
        print(data_to_serializer)
        form = Fieldserialiser(data=data_to_serializer)
        _form = DynamicForm(fields=fields.get('fields'))
        
        if form.is_valid():
            field = form.save(type=request.data.get('type').lower(),form=Form.objects.get(id=form_id))
            print(field)
            return redirect('get-form')
        else:
            print(form.errors)
        return Response({"serializer": form, "form": _form,"method":"post"}, template_name=self.template_name, status=status.HTTP_400_BAD_REQUEST)
