from django.urls import path
from .import views

urlpatterns = [
    path('registro-aplicantes/', views.registro_aplicantes)
]