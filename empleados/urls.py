from django.urls import path
from . import views

app_name = 'empleados'

urlpatterns = [
    path('', views.index, name='index'),
    path('empleados/ver_todos/', views.ver_todos, name='ver_todos'),
    path('empleados/gestionar/', views.gestionar, name='gestionar'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),
    path('empleados/editar/<int:id_empleado>/', views.editar_empleado, name='editar_empleado'),
    path('empleados/eliminar/<int:id_empleado>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('empleados/buscar/', views.buscar_empleado, name='buscar_empleado'),
    path('empleados/navegar/<str:accion>/<int:id_empleado>/', views.navegar_empleado, name='navegar_empleado'),
]