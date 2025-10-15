from django.shortcuts import render
from .forms import EmpForm

# Create your views here.
def registro_aplicantes(request):
    print(request.POST)
    a =request.POST['nombre']
    return render(request, 'pantalla_registro.html', {
        'form': EmpForm()
    })