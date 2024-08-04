from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea
from .forms import TareaForm

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'home/lista_tareas.html', {'tareas': tareas})

def detalle_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    return render(request, 'home/detalle_tarea.html', {'tarea': tarea})

def nueva_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.save()
            return redirect('detalle_tarea', pk=tarea.pk)
    else:
        form = TareaForm()
    return render(request, 'home/editar_tarea.html', {'form': form})

def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.save()
            return redirect('detalle_tarea', pk=tarea.pk)
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'home/editar_tarea.html', {'form': form})

def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.delete()
    return redirect('lista_tareas')
