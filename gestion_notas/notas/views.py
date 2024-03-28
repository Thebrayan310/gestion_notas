from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'notas/lista_tareas.html', {'tareas': tareas})

def agregar_tarea(request):
    if request.method == 'POST':
        equipo = request.POST.get('equipo')
        fecha_mantenimiento = request.POST.get('fecha_mantenimiento')
        procedimiento = request.POST.get('procedimiento')
        Tarea.objects.create(equipo=equipo, fecha_mantenimiento=fecha_mantenimiento, procedimiento=procedimiento)
    return redirect('lista_tareas')

def modificar_tarea(request, id):
    tarea = get_object_or_404(Tarea, pk=id)
    if request.method == 'POST':
        equipo = request.POST.get('equipo')
        fecha_mantenimiento = request.POST.get('fecha_mantenimiento')
        procedimiento = request.POST.get('procedimiento')
        tarea.equipo = equipo
        tarea.fecha_mantenimiento = fecha_mantenimiento
        tarea.procedimiento = procedimiento
        tarea.save()
        return redirect('lista_tareas')
    return render(request, 'notas/modificar_tarea.html', {'tarea': tarea})

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, pk=id)
    tarea.delete()
    return redirect('lista_tareas')


    




    
