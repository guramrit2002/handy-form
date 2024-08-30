from django.urls import path
from forms.views import FormCreate, FieldView

urlpatterns = [
    path('get',FormCreate.as_view({'get':'list'}),name="getform"),
    path('getfield/<form_id>',FieldView.as_view({'get': 'list', 'post': 'create'}),name="get-form"),
]