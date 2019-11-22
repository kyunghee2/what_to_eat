
from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
   path('', views.index, name='index'),
   # path('csvfilesave/',views.csvfilesave, name='csvfilesave'),
   path('search/', views.search, name='search'),
   path('<int:restaurant_pk>/', views.detail, name='detail'),
   # path('detail/', views.detail, name='detail')
]
