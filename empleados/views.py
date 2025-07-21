from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth import logout

@login_required
def index(request):
    return render(request, 'empleados/index.html')

@login_required
def ver_todos(request):
    empleados = Empleado.objects.all()
    paginator = Paginator(empleados, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'empleados/ver_todos.html', {'page_obj': page_obj})

@login_required
def gestionar(request):
    return render(request, 'empleados/gestionar.html')

@login_required
def crear_empleado(request):
    if request.method == 'POST':
        data = request.POST
        empleado = Empleado(
            id_empleado=data['id_empleado'],
            num_oficial=data['num_oficial'],
            num_provicional=data['num_provicional'],
            nombre=data.get('nombre', ''),
            apellido_paterno=data.get('apellido_paterno', ''),
            apellido_materno=data.get('apellido_materno', ''),
            sexo=data.get('sexo', ''),
            estado=data['estado'],
            fecha_alta=timezone.now().date(),
            usuario_ultima_modificacion=request.user.username,
            fecha_contratacion=data.get('fecha_contratacion') or None,
            fecha_baja=data.get('fecha_baja') or None,
            departamento=data.get('departamento', ''),
            puesto=data.get('puesto', ''),
            centro_costo=data.get('centro_costo', ''),
            sucursal=data.get('sucursal', ''),
            plan=data.get('plan', ''),
            telefono_trabajo=data.get('telefono_trabajo', ''),
            telefono_celular=data.get('telefono_celular', ''),
            telefono_otro=data.get('telefono_otro', ''),
            email=data.get('email', ''),
            horario_comedor=data.get('horario_comedor', ''),
            turno=data.get('turno', ''),
            foto=request.FILES.get('foto', None),
            jefe_inmediato=data.get('jefe_inmediato', '')
        )
        try:
            empleado.save()
            messages.success(request, 'Empleado creado exitosamente.')
        except Exception as e:
            messages.error(request, f'Error al crear el empleado: {str(e)}')
        return redirect('empleados:gestionar')
    return render(request, 'empleados/gestionar.html')

@login_required
def editar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        data = request.POST
        for field in data:
            if field not in ['id_empleado', 'nombre_completo', 'fecha_alta', 'usuario_ultima_modificacion', 'foto'] and hasattr(empleado, field):
                setattr(empleado, field, data[field] or None)
        if request.FILES.get('foto'):
            empleado.foto = request.FILES['foto']
        empleado.fecha_alta = empleado.fecha_alta or timezone.now().date()
        empleado.usuario_ultima_modificacion = request.user.username
        try:
            empleado.save()
            messages.success(request, 'Empleado actualizado exitosamente.')
        except Exception as e:
            messages.error(request, f'Error al actualizar el empleado: {str(e)}')
        return redirect('empleados:gestionar')
    return render(request, 'empleados/gestionar.html', {'empleado': empleado})

@login_required
def eliminar_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id_empleado=id_empleado)
    if request.method == 'POST':
        try:
            empleado.delete()
            messages.success(request, 'Empleado eliminado exitosamente.')
        except Exception as e:
            messages.error(request, f'Error al eliminar el empleado: {str(e)}')
        return redirect('empleados:gestionar')
    return render(request, 'empleados/confirmar_eliminar.html', {'empleado': empleado})

@login_required
def buscar_empleado(request):
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET['q'].strip()
        try:
            query_num = int(query)
            empleado = Empleado.objects.filter(
                Q(id_empleado=query_num) | Q(num_oficial=query_num)
            ).first()
            if empleado:
                return render(request, 'empleados/gestionar.html', {'empleado': empleado})
            else:
                messages.error(request, 'No se encontró el empleado.')
        except ValueError:
            messages.error(request, 'Por favor, ingrese un ID o número oficial válido (solo números).')
    return redirect('empleados:gestionar')

@login_required
def navegar_empleado(request, accion, id_empleado):
    empleados = Empleado.objects.all().order_by('id_empleado')
    current = get_object_or_404(Empleado, id_empleado=id_empleado)
    if accion == 'siguiente':
        next_empleado = empleados.filter(id_empleado__gt=id_empleado).first()
        if next_empleado:
            return render(request, 'empleados/gestionar.html', {'empleado': next_empleado})
    elif accion == 'anterior':
        prev_empleado = empleados.filter(id_empleado__lt=id_empleado).last()
        if prev_empleado:
            return render(request, 'empleados/gestionar.html', {'empleado': prev_empleado})
    elif accion == 'ultimo':
        last_empleado = empleados.last()
        if last_empleado:
            return render(request, 'empleados/gestionar.html', {'empleado': last_empleado})
    return render(request, 'empleados/gestionar.html', {'empleado': current})

def logout_view(request):
    logout(request)
    return redirect('empleados:index')