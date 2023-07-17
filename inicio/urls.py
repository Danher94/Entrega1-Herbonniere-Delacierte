from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/about/', views.about, name='about'),
    path('poemas/', views.listar_poemas, name='poemas'),
    path('poemas/crear/', views.crear_poema, name='crear_poema'),
    path('poemas/<int:pk>', views.DetallePoema.as_view(), name='detalle_poema'),
    path('poemas/<int:pk>/modificar', views.ModificarPoema.as_view(), name='modificar_poema'),
    path('poemas/<int:pk>/eliminar', views.EliminarPoema.as_view(), name='eliminar_poema')
]
