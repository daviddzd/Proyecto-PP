from django import forms

class EmpForm(forms.Form):
    nombre_emp = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=200)
    direccion = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    contrasena = forms.CharField(max_length=20, widget=forms.PasswordInput)
    verifica_contrasena = forms.CharField(max_length=20, widget=forms.PasswordInput)


class VacanteForm(forms.Form):
    puesto = forms.CharField(max_length=200)
    descripcion_vacante = forms.CharField(max_length=300)
    salario = forms.IntegerField()
    prestaciones = forms.CharField(max_length=400)
    requisitos = forms.CharField(max_length=400)

