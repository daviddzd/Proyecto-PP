from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import EmpForm, VacanteForm
from .models import Empresa, Vacante
from django.core.paginator import Paginator

# Create your views here.
def registro_emp(request):
    return HttpResponse('<h1>Registro Para Empresas</h1>')


def signUp(request):
    if request.method == 'GET':
        return render(request, 'signUp.html', {
            'form' : EmpForm(),

        })

    else:
        
        if request.POST['contrasena'] == request.POST['verifica_contrasena']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['contrasena'])
                user.save()
                empresa = Empresa.objects.create(nombre=request.POST['nombre_emp'], descripcion = request.POST['descripcion'], direccion = request.POST['direccion'], usuario = user)
                empresa.save()
                print(f'Se registró la empresa: {empresa.nombre}')
                return redirect('/signin')
            except:
                return render(request, 'plant_error.html', {
                    'error':'Este Nombre de Usuario Ya Existe'
                }) #cambiar por una vista de error

        else:
            return render(request, 'signup.html', {
                'form' : EmpForm(),
                'error': 'Las contraseñas no coinciden'
            })


def signIn(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm()
        })
    else:
        print(request.POST)
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        print(user)
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm(),
            'error':'Usuario o constraseña no encontrado'
            })
        else:
            login(request, user)
            print(f'El usuario: {request.user} con id: {request.user.id} ha inciado sesion')
            return redirect('/home')
        

def signout(request):
    logout(request)
    return redirect('/signin')


def mis_vacantes(request):
    if request.user.is_anonymous == False:
        empresa = Empresa.objects.get(usuario_id= request.user.id)
        vacantes = Vacante.objects.filter(empresa_id = empresa.id)
        vacantes_activas = vacantes.filter(activa=True)
        print(request.user.id)
        print(vacantes)
        return render(request, 'mis_vacantes.html', {
            'vacantes': vacantes_activas,
            'empresa' : empresa
        })
    else:
        print('Debes iniciar sesion primero')
        return render (request, 'plant_error.html', {
            'error' : 'Para Acceder a Este Recurso Debes Iniciar Sesion Antes'
        })


def agregar_vacante(request):
    if request.user.is_anonymous == False:
        if request.method == 'GET':
            return render(request, 'agregar_vacante.html', {
                'form': VacanteForm()
            })
        else:
            try:
                print(request.POST)
                empresa = Empresa.objects.get(usuario_id= request.user.id)
                nueva_vacante = Vacante.objects.create(
                    puesto=request.POST['puesto'],
                    descripcion_vacante = request.POST['descripcion_vacante'],
                    empresa = empresa,
                    salario = int(request.POST['salario']),
                    prestaciones = request.POST['prestaciones'],
                    requisitos = request.POST['requisitos']
                    )
                nueva_vacante.save()
                print('Se ha creado una nueva vacante')
                return redirect('/home')
            except:
                return render(request, 'plant_error.html', {
                    'error':'No se pudo crear la vacante'
                })
    else:
        print('Debes iniciar sesion primero')
        return render (request, 'plant_error.html', {
            'error' : 'Para Acceder a Este Recurso Debes Iniciar Sesion Antes'
        })
        


def detalle_vacante(request, id):
    vacante = Vacante.objects.get(id=id)
    data = {'vacante': vacante}
    return render(request, 'detalle_vacante.html', data)

def eliminar_vacante(request, id):
    vacante_a_eliminar = Vacante.objects.get(id=id)
    vacante_a_eliminar.activa = False
    vacante_a_eliminar.save()
    return redirect('/home')

def activar_vacante(request, id):
    vacante_a_activar = Vacante.objects.get(id=id)
    vacante_a_activar.activa = True
    vacante_a_activar.save()
    return redirect('/home')


def mod_vacante(request, id):

    if request.method == 'GET':
        vacante = Vacante.objects.get(id=id)
        return render(request, 'modificar_vacante.html', {
            'vacante':vacante,
        })
    else:
        try:
            vacante = Vacante.objects.get(id=id)

            print(request.POST)
            mod1 = request.POST['puesto']
            print(mod1)
            vacante.puesto = mod1

            mod2 = request.POST['descripcion_vacante']
            print(mod2)
            vacante.descripcion_vacante = mod2

            mod3 = request.POST['salario']
            print(mod3)
            vacante.salario = mod3

            mod4 = request.POST['requisitos']
            print(mod4)
            vacante.requisitos = mod4

            mod5 = request.POST['prestaciones']
            print(mod5)
            vacante.prestaciones = mod5

            print('Se ha modificado una vacante')
            vacante.save()
            return redirect(f'/detalle-vacante/{id}')
        except:
            return render(request, 'plant_error.html', {
                'error':'No se pudo actualizar la vacante'
            })
        

def historial(request):
    if request.user.is_anonymous == False:
        empresa = Empresa.objects.get(usuario_id= request.user.id)
        lista_vacantes = Vacante.objects.filter(empresa_id = empresa.id)
        paginator = Paginator(lista_vacantes, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'historial_vacantes.html', {'page_obj': page_obj})
    else:
        print('Debes iniciar sesion primero')
        return render (request, 'plant_error.html', {
            'error' : 'Para Acceder a Este Recurso Debes Iniciar Sesion Antes'
        })
    
def perfil(request):
    if request.user.is_anonymous == False:
        username = request.user.username
        empresa = Empresa.objects.get(usuario_id= request.user.id)
        return render(request, 'perfil.html', {
            'username':username,
            'empresa':empresa
        })
    else:
        print('Debes iniciar sesion primero')
        return render (request, 'plant_error.html', {
            'error' : 'Para Acceder a Este Recurso Debes Iniciar Sesion Antes'
        })