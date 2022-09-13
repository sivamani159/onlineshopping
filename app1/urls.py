from django.urls import path
from app1 import views

app_name='app1'

urlpatterns=[
    path('ajio',views.ajio,name='ajio'),
    path('gopaldigitals',views.gopaldigitals,name='gopaldigitals')
]