from django.shortcuts import render

# Create your views here.
def registro_aplicantes(request):
    return render(request, 'registro_aplicantes.html')