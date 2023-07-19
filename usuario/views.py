from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from usuario.form import CreacionUsuario, EdicionPerfil
from django.contrib.auth.forms import UserChangeForm

# Create your views here.

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            
            user = authenticate(username=usuario,password=contrasenia)
            
            django_login(request, user)
            return redirect('inicio:inicio')
            
        else:
            return render(request, 'usuario/login.html', {'formulario': formulario})
    
    formulario = AuthenticationForm()
    return render(request, 'usuario/login.html', {'formulario': formulario})

def registrarse(request):
    
    if request.method == 'POST':
        formulario = CreacionUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuario:login')
        else:
            return render(request, 'usuario/registro.html', {'formulario': formulario})

    formulario = CreacionUsuario()
    return render(request, 'usuario/registro.html', {'formulario': formulario})


class Perfil(PasswordChangeView):
    template_name = 'usuario/perfil.html'
    success_url = reverse_lazy('usuario:perfil')


@login_required
def edicion(request):
    
    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio:inicio')
    else:
        formulario = EdicionPerfil(instance=request.user)
    return render(request, 'usuario/edicion.html', {'formulario': formulario})


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = 'Contraseña anterior'
        self.fields['new_password1'].label = 'Nueva contraseña'
        self.fields['new_password2'].label = 'Repetir nueva contraseña'
        for field_name in self.fields:
            self.fields[field_name].help_text = ''

class EdicionPass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuario/edicion_pass.html'
    success_url = reverse_lazy('usuario:edicion') 
    form_class = CustomPasswordChangeForm