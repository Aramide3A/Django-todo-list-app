from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name= 'task'),
    path('<str:pk>', views.modify_page, name = 'modify'),
    path('delete/<str:pk>', views.delete, name = 'delete'),  
]
