from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import EQUIPOS, MONITORES, NO_BREAKS
from django.contrib import messages
from django.http import FileResponse, Http404
from django.core.files.storage import FileSystemStorage

def ver_equipos(request):
    equipos = EQUIPOS.objects.all().order_by('ID_EQUIPO')
    paginator = Paginator(equipos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'activos/ver_activos.html', {'activos': page_obj.object_list, 'tipo': 'EQUIPOS', 'page_obj': page_obj, 'first_id': equipos.first().ID_EQUIPO if equipos.exists() else None})

def ver_equipo(request, id_equipo):
    equipo = get_object_or_404(EQUIPOS, ID_EQUIPO=id_equipo)
    equipos = EQUIPOS.objects.all().order_by('ID_EQUIPO')
    paginator = Paginator(equipos, 1)  # Una página por equipo
    page_number = 1
    if equipos.exists():
        id_list = list(equipos.values_list('ID_EQUIPO', flat=True))
        if id_equipo in id_list:
            index = id_list.index(id_equipo)
            page_number = (index // paginator.per_page) + 1
            prev_index = index - 1 if index > 0 else None
            next_index = index + 1 if index < len(id_list) - 1 else None
            prev_id = id_list[0] if prev_index is None else id_list[prev_index]
            next_id = id_list[-1] if next_index is None else id_list[next_index]
    else:
        id_list = []
        prev_id = None
        next_id = None
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        q = request.POST.get('q', '')
        equipo = get_object_or_404(EQUIPOS, ID_EQUIPO=q)
        return redirect('activos:ver_equipo', id_equipo=equipo.ID_EQUIPO)
    return render(request, 'activos/ver_equipo.html', {'equipo': equipo, 'page_obj': page_obj, 'id_list': id_list, 'prev_id': prev_id, 'next_id': next_id})

def gestionar_equipo(request, id_equipo=None):
    if request.method == 'POST':
        if id_equipo:
            equipo = get_object_or_404(EQUIPOS, ID_EQUIPO=id_equipo)
            equipo.ESTADO = request.POST.get('ESTADO')
            equipo.RAZON_SOCIAL = request.POST.get('RAZON_SOCIAL')
            equipo.UBICACION = request.POST.get('UBICACION')
            equipo.TIPO_EQUIPO = request.POST.get('TIPO_EQUIPO')
            equipo.SITUACION = request.POST.get('SITUACION')
            equipo.PROVEEDOR = request.POST.get('PROVEEDOR')
            equipo.MARCA = request.POST.get('MARCA')
            equipo.MODELO = request.POST.get('MODELO')
            equipo.SERIE = request.POST.get('SERIE')
            equipo.LINEA_TEL = request.POST.get('LINEA_TEL')
            equipo.IMEI = request.POST.get('IMEI')
            equipo.COMPANIA = request.POST.get('COMPANIA')
            equipo.PROCESADOR = request.POST.get('PROCESADOR')
            equipo.RAM_1 = request.POST.get('RAM_1')
            equipo.RAM_2 = request.POST.get('RAM_2')
            equipo.DISCO_1 = request.POST.get('DISCO_1')
            equipo.DISCO_2 = request.POST.get('DISCO_2')
            equipo.SISTEMA_OPERATIVO = request.POST.get('SISTEMA_OPERATIVO')
            equipo.OBSERVATIONS = request.POST.get('OBSERVATIONS')
            equipo.MAC_WIFI1 = request.POST.get('MAC_WIFI1')
            equipo.MAC_WIFI2 = request.POST.get('MAC_WIFI2')
            equipo.MAC_ETHERNET1 = request.POST.get('MAC_ETHERNET1')
            equipo.MAC_ETHERNET2 = request.POST.get('MAC_ETHERNET2')
            equipo.DEPARTAMENTO_ASIGNADO = request.POST.get('DEPARTAMENTO_ASIGNADO')
            equipo.FECHA_ALTA = request.POST.get('FECHA_ALTA')
            equipo.ANTIVIRUS = request.POST.get('ANTIVIRUS')
            if 'FOTO' in request.FILES:
                equipo.FOTO = request.FILES['FOTO']
            if 'DOCUMENTOS' in request.FILES:
                equipo.DOCUMENTOS = request.FILES['DOCUMENTOS']
            equipo.save()
            messages.success(request, 'Equipo actualizado exitosamente.')
        else:
            equipo = EQUIPOS(
                ID_EQUIPO=request.POST.get('ID_EQUIPO'),
                ESTADO=request.POST.get('ESTADO'),
                RAZON_SOCIAL=request.POST.get('RAZON_SOCIAL'),
                UBICACION=request.POST.get('UBICACION'),
                TIPO_EQUIPO=request.POST.get('TIPO_EQUIPO'),
                SITUACION=request.POST.get('SITUACION'),
                PROVEEDOR=request.POST.get('PROVEEDOR'),
                MARCA=request.POST.get('MARCA'),
                MODELO=request.POST.get('MODELO'),
                SERIE=request.POST.get('SERIE'),
                LINEA_TEL=request.POST.get('LINEA_TEL'),
                IMEI=request.POST.get('IMEI'),
                COMPANIA=request.POST.get('COMPANIA'),
                PROCESADOR=request.POST.get('PROCESADOR'),
                RAM_1=request.POST.get('RAM_1'),
                RAM_2=request.POST.get('RAM_2'),
                DISCO_1=request.POST.get('DISCO_1'),
                DISCO_2=request.POST.get('DISCO_2'),
                SISTEMA_OPERATIVO=request.POST.get('SISTEMA_OPERATIVO'),
                OBSERVATIONS=request.POST.get('OBSERVATIONS'),
                MAC_WIFI1=request.POST.get('MAC_WIFI1'),
                MAC_WIFI2=request.POST.get('MAC_WIFI2'),
                MAC_ETHERNET1=request.POST.get('MAC_ETHERNET1'),
                MAC_ETHERNET2=request.POST.get('MAC_ETHERNET2'),
                DEPARTAMENTO_ASIGNADO=request.POST.get('DEPARTAMENTO_ASIGNADO'),
                FECHA_ALTA=request.POST.get('FECHA_ALTA'),
                ANTIVIRUS=request.POST.get('ANTIVIRUS')
            )
            if 'FOTO' in request.FILES:
                equipo.FOTO = request.FILES['FOTO']
            if 'DOCUMENTOS' in request.FILES:
                equipo.DOCUMENTOS = request.FILES['DOCUMENTOS']
            equipo.save()
            messages.success(request, 'Equipo creado exitosamente.')
        return redirect('activos:ver_equipos')
    else:
        equipo = get_object_or_404(EQUIPOS, ID_EQUIPO=id_equipo) if id_equipo else None
        return render(request, 'activos/gestionar_equipo.html', {'equipo': equipo, 'tipo': 'EQUIPOS'})

def eliminar_equipo(request, id_equipo):
    equipo = get_object_or_404(EQUIPOS, ID_EQUIPO=id_equipo)
    if request.method == 'POST':
        equipo.delete()
        messages.success(request, 'Equipo eliminado exitosamente.')
        return redirect('activos:ver_equipos')
    return render(request, 'activos/confirmar_eliminar.html', {'equipo': equipo, 'tipo': 'EQUIPOS'})

def ver_monitores(request):
    monitores = MONITORES.objects.all().order_by('ID_MONITOR')
    paginator = Paginator(monitores, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'activos/ver_activos.html', {'activos': page_obj.object_list, 'tipo': 'MONITORES', 'page_obj': page_obj, 'first_id': monitores.first().ID_MONITOR if monitores.exists() else None})

def ver_monitor(request, id_monitor):
    monitor = get_object_or_404(MONITORES, ID_MONITOR=id_monitor)
    monitores = MONITORES.objects.all().order_by('ID_MONITOR')
    paginator = Paginator(monitores, 1)  # Una página por monitor
    page_number = 1
    if monitores.exists():
        id_list = list(monitores.values_list('ID_MONITOR', flat=True))
        if id_monitor in id_list:
            index = id_list.index(id_monitor)
            page_number = (index // paginator.per_page) + 1
            prev_index = index - 1 if index > 0 else None
            next_index = index + 1 if index < len(id_list) - 1 else None
            prev_id = id_list[0] if prev_index is None else id_list[prev_index]
            next_id = id_list[-1] if next_index is None else id_list[next_index]
    else:
        id_list = []
        prev_id = None
        next_id = None
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        q = request.POST.get('q', '')
        monitor = get_object_or_404(MONITORES, ID_MONITOR=q)
        return redirect('activos:ver_monitor', id_monitor=monitor.ID_MONITOR)
    return render(request, 'activos/ver_monitor.html', {'monitor': monitor, 'page_obj': page_obj, 'id_list': id_list, 'prev_id': prev_id, 'next_id': next_id})

def gestionar_monitor(request, id_monitor=None):
    if request.method == 'POST':
        if id_monitor:
            monitor = get_object_or_404(MONITORES, ID_MONITOR=id_monitor)
            monitor.ESTADO = request.POST.get('ESTADO')
            monitor.RAZON_SOCIAL = request.POST.get('RAZON_SOCIAL')
            monitor.MARCA = request.POST.get('MARCA')
            monitor.MODELO = request.POST.get('MODELO')
            monitor.NUM_SERIE = request.POST.get('NUM_SERIE')
            monitor.OBSERVATIONS = request.POST.get('OBSERVATIONS')
            if 'DOCUMENTOS' in request.FILES:
                monitor.DOCUMENTOS = request.FILES['DOCUMENTOS']
            monitor.save()
            messages.success(request, 'Monitor actualizado exitosamente.')
        else:
            monitor = MONITORES(
                ID_MONITOR=request.POST.get('ID_MONITOR'),
                ESTADO=request.POST.get('ESTADO'),
                RAZON_SOCIAL=request.POST.get('RAZON_SOCIAL'),
                MARCA=request.POST.get('MARCA'),
                MODELO=request.POST.get('MODELO'),
                NUM_SERIE=request.POST.get('NUM_SERIE'),
                OBSERVATIONS=request.POST.get('OBSERVATIONS')
            )
            if 'DOCUMENTOS' in request.FILES:
                monitor.DOCUMENTOS = request.FILES['DOCUMENTOS']
            monitor.save()
            messages.success(request, 'Monitor creado exitosamente.')
        return redirect('activos:ver_monitores')
    else:
        monitor = get_object_or_404(MONITORES, ID_MONITOR=id_monitor) if id_monitor else None
        return render(request, 'activos/gestionar_monitor.html', {'monitor': monitor, 'tipo': 'MONITORES'})

def eliminar_monitor(request, id_monitor):
    monitor = get_object_or_404(MONITORES, ID_MONITOR=id_monitor)
    if request.method == 'POST':
        monitor.delete()
        messages.success(request, 'Monitor eliminado exitosamente.')
        return redirect('activos:ver_monitores')
    return render(request, 'activos/confirmar_eliminar.html', {'monitor': monitor, 'tipo': 'MONITORES'})

def ver_no_breaks(request):
    no_breaks = NO_BREAKS.objects.all().order_by('ID_BREAK')
    paginator = Paginator(no_breaks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'activos/ver_activos.html', {'activos': page_obj.object_list, 'tipo': 'NO_BREAKS', 'page_obj': page_obj, 'first_id': no_breaks.first().ID_BREAK if no_breaks.exists() else None})

def ver_no_break(request, id_break):
    no_break = get_object_or_404(NO_BREAKS, ID_BREAK=id_break)
    no_breaks = NO_BREAKS.objects.all().order_by('ID_BREAK')
    paginator = Paginator(no_breaks, 1)  # Una página por no_break
    page_number = 1
    if no_breaks.exists():
        id_list = list(no_breaks.values_list('ID_BREAK', flat=True))
        if id_break in id_list:
            index = id_list.index(id_break)
            page_number = (index // paginator.per_page) + 1
            prev_index = index - 1 if index > 0 else None
            next_index = index + 1 if index < len(id_list) - 1 else None
            prev_id = id_list[0] if prev_index is None else id_list[prev_index]
            next_id = id_list[-1] if next_index is None else id_list[next_index]
    else:
        id_list = []
        prev_id = None
        next_id = None
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        q = request.POST.get('q', '')
        no_break = get_object_or_404(NO_BREAKS, ID_BREAK=q)
        return redirect('activos:ver_no_break', id_break=no_break.ID_BREAK)
    return render(request, 'activos/ver_no_break.html', {'no_break': no_break, 'page_obj': page_obj, 'id_list': id_list, 'prev_id': prev_id, 'next_id': next_id})

def gestionar_no_break(request, id_no_break=None):
    if request.method == 'POST':
        if id_no_break:
            no_break = get_object_or_404(NO_BREAKS, ID_BREAK=id_no_break)
            no_break.ESTADO = request.POST.get('ESTADO')
            no_break.RAZON_SOCIAL = request.POST.get('RAZON_SOCIAL')
            no_break.MARCA = request.POST.get('MARCA')
            no_break.MODELO = request.POST.get('MODELO')
            no_break.NUM_SERIE = request.POST.get('NUM_SERIE')
            no_break.OBSERVATIONS = request.POST.get('OBSERVATIONS')
            if 'DOCUMENTOS' in request.FILES:
                no_break.DOCUMENTOS = request.FILES['DOCUMENTOS']
            no_break.save()
            messages.success(request, 'No Break actualizado exitosamente.')
        else:
            no_break = NO_BREAKS(
                ID_BREAK=request.POST.get('ID_BREAK'),
                ESTADO=request.POST.get('ESTADO'),
                RAZON_SOCIAL=request.POST.get('RAZON_SOCIAL'),
                MARCA=request.POST.get('MARCA'),
                MODELO=request.POST.get('MODELO'),
                NUM_SERIE=request.POST.get('NUM_SERIE'),
                OBSERVATIONS=request.POST.get('OBSERVATIONS')
            )
            if 'DOCUMENTOS' in request.FILES:
                no_break.DOCUMENTOS = request.FILES['DOCUMENTOS']
            no_break.save()
            messages.success(request, 'No Break creado exitosamente.')
        return redirect('activos:ver_no_breaks')
    else:
        no_break = get_object_or_404(NO_BREAKS, ID_BREAK=id_no_break) if id_no_break else None
        return render(request, 'activos/gestionar_no_break.html', {'no_break': no_break, 'tipo': 'NO_BREAKS'})

def eliminar_no_break(request, id_break):
    no_break = get_object_or_404(NO_BREAKS, ID_BREAK=id_break)
    if request.method == 'POST':
        no_break.delete()
        messages.success(request, 'No Break eliminado exitosamente.')
        return redirect('activos:ver_no_breaks')
    return render(request, 'activos/confirmar_eliminar.html', {'no_break': no_break, 'tipo': 'NO_BREAKS'})

def buscar_equipo(request):
    q = request.GET.get('q', '').strip()
    if q:
        equipos = EQUIPOS.objects.filter(ID_EQUIPO__iexact=q)
        if equipos.exists():
            if equipos.count() == 1:
                return redirect('activos:ver_equipo', id_equipo=equipos[0].ID_EQUIPO)
            else:
                return render(request, 'activos/ver_activos.html', {'activos': equipos, 'tipo': 'EQUIPOS', 'page_obj': None, 'first_id': equipos.first().ID_EQUIPO if equipos.exists() else None})
        else:
            equipos = EQUIPOS.objects.filter(ID_EQUIPO__icontains=q).order_by('ID_EQUIPO')
            if equipos.exists():
                paginator = Paginator(equipos, 10)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request, 'activos/ver_activos.html', {'activos': page_obj.object_list, 'tipo': 'EQUIPOS', 'page_obj': page_obj, 'first_id': equipos.first().ID_EQUIPO if equipos.exists() else None})
    return render(request, 'activos/ver_activos.html', {'activos': [], 'tipo': 'EQUIPOS', 'page_obj': None, 'first_id': None})

def buscar_monitor(request):
    q = request.GET.get('q', '').strip()
    if q:
        monitores = MONITORES.objects.filter(ID_MONITOR__iexact=q)
        if monitores.exists():
            if monitores.count() == 1:
                return redirect('activos:ver_monitor', id_monitor=monitores[0].ID_MONITOR)
            else:
                return render(request, 'activos/ver_activos.html', {'activos': monitores, 'tipo': 'MONITORES', 'page_obj': None, 'first_id': monitores.first().ID_MONITOR if monitores.exists() else None})
        else:
            monitores = MONITORES.objects.filter(ID_MONITOR__icontains=q).order_by('ID_MONITOR')
            if monitores.exists():
                paginator = Paginator(monitores, 10)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request, 'activos/ver_activos.html', {'activos': page_obj.object_list, 'tipo': 'MONITORES', 'page_obj': page_obj, 'first_id': monitores.first().ID_MONITOR if monitores.exists() else None})
    return render(request, 'activos/ver_activos.html', {'activos': [], 'tipo': 'MONITORES', 'page_obj': None, 'first_id': None})

def buscar_no_break(request):
    q = request.GET.get('q', '').strip()
    if q:
        no_breaks = NO_BREAKS.objects.filter(ID_BREAK__iexact=q)
        if no_breaks.exists():
            if no_breaks.count() == 1:
                return redirect('activos:ver_no_break', id_break=no_breaks[0].ID_BREAK)
            else:
                return render(request, 'activos/ver_activos.html', {'activos': no_breaks, 'tipo': 'NO_BREAKS', 'page_obj': None, 'first_id': no_breaks.first().ID_BREAK if no_breaks.exists() else None})
        else:
            no_breaks = NO_BREAKS.objects.filter(ID_BREAK__icontains=q).order_by('ID_BREAK')
            if no_breaks.exists():
                paginator = Paginator(no_breaks, 10)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request, 'activos/ver_activos.html', {'activos': page_obj.object_list, 'tipo': 'NO_BREAKS', 'page_obj': page_obj, 'first_id': no_breaks.first().ID_BREAK if no_breaks.exists() else None})
    return render(request, 'activos/ver_activos.html', {'activos': [], 'tipo': 'NO_BREAKS', 'page_obj': None, 'first_id': None})

def get_file(request, id, file_type):
    if file_type == 'foto':
        equipo = get_object_or_404(EQUIPOS, ID_EQUIPO=id)
        file_field = equipo.FOTO
    elif file_type == 'documento':
        equipo = get_object_or_404(EQUIPOS, ID_EQUIPO=id)
        file_field = equipo.DOCUMENTOS
    else:
        raise Http404("Tipo de archivo no válido")

    if file_field and hasattr(file_field, 'file'):
        return FileResponse(file_field.file, as_attachment=True, filename=file_field.name)
    else:
        raise Http404("Archivo no encontrado")