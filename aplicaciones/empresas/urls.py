from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.signUp),
    path('signin/', views.signIn),
    path('signout/', views.signout),
    path('home/', views.mis_vacantes),
    path('agregar-vacante/', views.agregar_vacante),
    path('detalle-vacante/<int:id>', views.detalle_vacante),
    path('eliminar-vacante/<int:id>', views.eliminar_vacante),
    path('mod-vacante/<int:id>', views.mod_vacante),
    path('historial-vacantes/', views.historial),
    path('activar-vacante/<int:id>', views.activar_vacante),
    path('perfil/', views.perfil)
]