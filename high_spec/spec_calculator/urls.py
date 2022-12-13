from django.urls import path
from .views import Calculate_spec


urlpatterns =[
    path('', Calculate_spec.as_view()),
    path('conclusion/', Calculate_spec.as_view(), name='conclusion'),
]