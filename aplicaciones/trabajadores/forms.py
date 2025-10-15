from django import forms


class EmpForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=200)
    edad = forms.IntegerField()
    genero = forms.CharField(max_length=10)
    cod_post = forms.CharField(max_length=10)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=15)
    username = forms.CharField(max_length=200)
    contrasena = forms.CharField(max_length=20, widget=forms.PasswordInput)
    verifica_contrasena = forms.CharField(max_length=20, widget=forms.PasswordInput)
    
    exp_laboral = forms.CharField(max_length=400)
    educacion = forms.CharField(max_length=400)
    area = forms.CharField(max_length=100)
    best_work = forms.CharField(max_length=400)
    last_work = forms.CharField(max_length=400)
    nivel_experiencia = forms.CharField(max_length=50)
    
    