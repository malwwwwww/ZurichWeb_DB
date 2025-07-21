from django.urls import path
from . import views

app_name = 'activos'

urlpatterns = [
    path('EQUIPOS/buscar/', views.buscar_equipo, name='buscar_equipo'),
    path('MONITORES/buscar/', views.buscar_monitor, name='buscar_monitor'),
    path('NO_BREAKS/buscar/', views.buscar_no_break, name='buscar_no_break'),
    path('EQUIPOS/', views.ver_equipos, name='ver_equipos'),
    path('EQUIPOS/gestionar/', views.gestionar_equipo, name='gestionar_equipo'),
    path('EQUIPOS/gestionar/<str:id_equipo>/', views.gestionar_equipo, name='gestionar_equipo_edit'),
    path('EQUIPOS/<str:id_equipo>/', views.ver_equipo, name='ver_equipo'),
    path('EQUIPOS/eliminar/<str:id_equipo>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('MONITORES/', views.ver_monitores, name='ver_monitores'),
    path('MONITORES/gestionar/', views.gestionar_monitor, name='gestionar_monitor'),
    path('MONITORES/gestionar/<str:id_monitor>/', views.gestionar_monitor, name='gestionar_monitor_edit'),
    path('MONITORES/<str:id_monitor>/', views.ver_monitor, name='ver_monitor'),
    path('MONITORES/eliminar/<str:id_monitor>/', views.eliminar_monitor, name='eliminar_monitor'),
    path('NO_BREAKS/', views.ver_no_breaks, name='ver_no_breaks'),
    path('NO_BREAKS/gestionar/', views.gestionar_no_break, name='gestionar_no_break'),
    path('NO_BREAKS/gestionar/<str:id_no_break>/', views.gestionar_no_break, name='gestionar_no_break_edit'),
    path('NO_BREAKS/<str:id_break>/', views.ver_no_break, name='ver_no_break'),
    path('NO_BREAKS/eliminar/<str:id_break>/', views.eliminar_no_break, name='eliminar_no_break'),
    path('EQUIPOS/<str:id>/<str:file_type>/', views.get_file, name='get_file'),
]