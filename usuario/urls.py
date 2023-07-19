from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView

app_name = 'usuario'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    path('registro/', views.registrarse, name='registrarse'),
    # path('perfil/', views.Perfil, name='perfil'),
    path('perfil/', views.Perfil.as_view(), name='perfil'),
    path('perfil/editar/', views.edicion, name='edicion'),
    path('perfil/editar/editar_pass/', views.EdicionPass.as_view(), name='edicion_pass')
]
