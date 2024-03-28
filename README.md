Documentación del Proyecto Gestion de Notas

Introducción


Este proyecto, llamado Gestion Notas, es una aplicación web desarrollada utilizando el framework Django. La aplicación permite a los usuarios gestionar y administrar tareas, incluyendo la capacidad de agregar, modificar y eliminar tareas.




Objetivo

El objetivo de este proyecto es crear una aplicación web que permita a los usuarios registrar, visualizar, modificar y eliminar notas de tareas relacionadas con el mantenimiento de equipos.





Características Principales

1.	Registro de tareas con información detallada.
2.	Visualización de todas las tareas registradas.
3.	Modificación y eliminación de tareas existentes.
4.	Interfaz intuitiva y fácil de usar.





Requisitos del Sistema

•	Python 3.x

•	Django 3.x

•	Navegador web compatible con HTML5 y CSS3







Instalación


Para ejecutar este proyecto localmente, sigue estos pasos:


1.	Clona este repositorio en tu máquina local utilizando el siguiente comando:

en el bash

git clone https://github.com/Thebrayan310/gestion_notas.git

2.	Navega al directorio del proyecto:

en el bash

cd gestion_notas



3.	Crea un entorno virtual para el proyecto:

en el bash

python3 -m venv venv




4.	Activa el entorno virtual:

-En Windows:

en el bash
venv\Scripts\activate

-En macOS y Linux:

en el bash
source venv/bin/activate




5.	Instala las dependencias del proyecto:

en el bash

pip install -r requirements.txt




6.	Realiza las migraciones de la base de datos:

en el bash

python manage.py migrate




7.	Inicia el servidor de desarrollo:

en el bash

python manage.py runserver



8.	Accede a la aplicación en tu navegador web en la siguiente dirección: http://127.0.0.1:8000/




Uso

•	Desde la página principal, podrás visualizar todas las tareas registradas.

•	Para agregar una nueva tarea, simplemente haz clic en el botón "Agregar Tarea" y completa el formulario.

•	Si necesitas modificar o eliminar una tarea existente, puedes hacerlo haciendo clic en los enlaces correspondientes junto a cada tarea en la lista.

•	¡Explora las diversas funcionalidades y disfruta del sistema sin necesidad de iniciar sesión!




Créditos

Desarrollador principal: Brayan Stiven Arias Henao

