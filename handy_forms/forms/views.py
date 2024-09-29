from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from .forms.dynamic_forms import DynamicForm
from .serializers import Fieldserialiser, FormSerializer, FormAttributeSerializer, MasterFormSerializer, FieldAttributesSerializer
from .models import Field,Form
from django.shortcuts import redirect,reverse, get_object_or_404
from .models import FIELD_TYPE_CHOICES
from .utils import get_field_type_choices, clean_html
from rest_framework.decorators import api_view
from .html_directory.section import Sections
from .constants import field_attributes


class FormView(ViewSet):
    def list(self, request,form_id):
        fields = Field.objects.filter(form_id=form_id).values()
        form_fetched = Form.objects.get(id=form_id)
        print(fields)
        form = DynamicForm(fields=fields)
        print('dynamic forms')
        form_html = form.as_p()
        form_html = form_html.replace('\n', '').replace('\r', '').strip()
        field_serializer = Fieldserialiser(fields,many=True)
        form_serializer = FormSerializer(form_fetched,many=False)
        return Response({"form": form_serializer.data, "fields": field_serializer.data, "html": form_html}, status=status.HTTP_200_OK)
    def create(self,request):
        try:
            print(request.data)
            form_serializer = FormSerializer(data=request.data.get('form'))
            result = {}
            if form_serializer.is_valid():
                new_form = form_serializer.save()
                attributes = request.data.get('form_attribute')
                attributes['form'] = new_form.id
                form_attribute_serializer = FormAttributeSerializer(data=attributes)
                result = {"form":form_serializer.data}
                if form_attribute_serializer.is_valid():
                    new_form_attribute = form_attribute_serializer.save()
                    result['form_attribute'] = form_attribute_serializer.data
                else:
                    raise Exception(form_attribute_serializer.errors)
            else:
                raise Exception(form_serializer.errors)
        except Exception as e:
            raise Exception(e)
        return Response({"message":"success",**result})


class FieldView(ViewSet):
    
    def get_fields(self,id):
        values = ['id','name','type','form__id','form__form_name','form__created_by']
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
    def create(self, request,form_id):
        try:
            result = {}
            data_to_serializer = {
                "name": request.data.get('field').get('name'),
                "label": request.data.get('field').get('label')
            }
            form = Fieldserialiser(data=data_to_serializer)
            if form.is_valid():
                field = form.save(type=request.data.get('field').get('type').lower(), form=Form.objects.get(id=form_id))
                result = {
                    "field": form.data
                }
                attribute_field = {
                    "field": field.id,
                    **request.data.get("field_attribute")
                }
                field_attribute_serializer = FieldAttributesSerializer(data=attribute_field)
                if field_attribute_serializer.is_valid():
                    field_attribute = field_attribute_serializer.save()
                    result["field_attribute"] = field_attribute_serializer.data
                else:
                    import traceback
                    traceback.print_exc()
                    raise Exception(field_attribute_serializer.errors)
            else:
                print(form.errors)

                raise Exception(form.errors)
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise Exception(e)
        print(result)
        return Response({"message":"success",**result},status=status.HTTP_201_CREATED)
    def destroy(self, request, field_id):
        try:
            field = get_object_or_404(Field, id=field_id)
            field.delete()
            print('Field deleted successfully')

            # Optionally, you can return a success message or redirect
            return Response({'message':'success'},status=status.HTTP_200_OK)

        except Field.DoesNotExist:
            # Redirect to the form if the field does not exist
            return Response({'message':'not found'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'error','error':str(e)},status=status.HTTP_400_BAD_REQUEST)


class CustomHTML(ViewSet):

    def list(self, request):
        # Check if 'type' parameter is in the GET request
        field_type = request.GET.get("type")

        if field_type:
            # Create a dynamic form with the specified type
            field_html = DynamicForm(fields=[{
                "type": field_type,
                "name": "",
                "label": ""
            }])
            # Prepare the response
            response = {
                "type": field_type,
                "html": clean_html(field_html.as_div())
            }
            print(response)
            return Response(response, status=status.HTTP_200_OK)
        else:
            # Create a default dynamic form
            form = DynamicForm(fields=field_attributes)

            section = Sections()

            # Prepare the response
            response = {
                "type": request.GET.get("form"),
                "html": section.final_html(form.as_p())
            }
            return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
def all_types(request):
    return Response({"types": get_field_type_choices(FIELD_TYPE_CHOICES)}, status=status.HTTP_200_OK)