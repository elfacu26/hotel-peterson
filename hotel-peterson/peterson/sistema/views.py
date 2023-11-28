from django.shortcuts import render
from .models import Cliente, TipoHab, Habitacion, Reserva, Puesto, Empleado, Usuario, Caja
from .forms import buscarHab

# Create your views here.
def home(request):
    return render(request, 'home.html')

def reserva(request):
    if request.method == "POST":
        form = buscarHab(request.POST)

        if form.is_valid():
            num = form.cleaned_data["personas"]
    else:
        form = buscarHab()
    habitaciones = Habitacion.objects.all()
    return render(request, 'reserva.html', {'habitaciones':habitaciones, 'form':form})

def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def pago(request):
    return render(request, 'pago.html')

