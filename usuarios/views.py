from django.shortcuts import redirect, render
from .forms import RegistrarUsuario
from django.contrib.auth.decorators import login_required
from .models import Usuario

# Creacion de usuarios
def registro(request):
    # SI el usuario esta registrado lo redireccionamos a la pagina de inicio
    if request.user.is_authenticated:
        return redirect ('/')

    else:
        if request.method == 'POST':
            form = RegistrarUsuario(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/login/')
            
        else:
            form = RegistrarUsuario()

        contexto = {
            'form': form,
        }
    return render(request, 'vistas/registro.html', contexto)

# Vista inicio, login necesario
@login_required(login_url='/login/')
def inicio(request):
    return render(request, 'vistas/index.html')