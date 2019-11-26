
from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
   path('', views.index, name='index'),
   path('search/', views.search, name='search'),
   path('<int:restaurant_pk>/', views.detail, name='detail'),
   path('comments/<int:restaurant_pk>', views.comments_create, name='comment'),
   path('how_to_use_chatbot/', views.how_to_use_chatbot, name='how_to_use_chatbot'),
   path('people/<int:people>/', views.people, name='people'),
   path('csvfilesave/',views.csvfilesave,name='csvfilesave'),
]
