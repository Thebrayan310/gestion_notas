from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('eliminar/<int:id>/', views.eliminar_tarea, name='eliminar'),
    path('agregar/', views.agregar_tarea, name='agregar'),
    path('modificar/<int:id>/', views.modificar_tarea, name='modificar'),
]

