from django.urls import path
from .views import Calculate_spec


urlpatterns =[
    path('', Calculate_spec.as_view(), name='index'),
    path('conclusion/', Calculate_spec.as_view(), name='conclusion'),
    # path('jp/', Calculate_spec.as_view )
]