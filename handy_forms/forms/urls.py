from django.urls import path
from forms.views import FormView, FieldView, CustomHTML, all_types

urlpatterns = [
    path('get/<form_id>',FormView.as_view({'get': 'list'}),name="getform"),
    path('post/',FormView.as_view({'post': 'create'})),
    path('getfield/<form_id>',FieldView.as_view({'post': 'create'}),name="get-form"),
    path('deletefield/<field_id>/', FieldView.as_view({'post': 'destroy'}), name="delete-field"),
    path('get/field/',CustomHTML.as_view({'get': 'list'})),
    path('alltypes',all_types,name="all-types")
]
