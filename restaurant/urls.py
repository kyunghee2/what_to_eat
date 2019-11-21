
from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
   path('', views.index, name='index'),
   # path('csvfilesave/',views.csvfilesave, name='csvfilesave'),
   path('query/', views.query, name='query'),
]
