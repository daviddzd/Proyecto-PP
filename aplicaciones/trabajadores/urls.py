from django.urls import path
from .import views

urlpatterns = [
    path('pantalla_registro/', views.registro_aplicantes)
]