# Bitacora de IA

* **Asistente utilizado:** Google Gemini

# Prompt 1: Guía de estructuración y desarrollo paso a paso desde cero
* **Rol:** Actúa como un tutor de programación Back-End claro y paciente, especializado en Python, Django y MySQL.
* **Tarea:** Guíame paso a paso desde cero para construir una aplicación web de gestión para una clínica veterinaria, explicándome cómo conectar MySQL, definir los modelos relacionales (`Especie` y `Paciente`) y estructurar el CRUD con Vistas Basadas en Clases, `select_related` y `LoginRequiredMixin`.
* **Contexto:** Parto sin experiencia previa sólida en Django y necesito desarrollar este proyecto cumpliendo una arquitectura estricta de dos modelos (relación 1:N) conectados a una base de datos local en MySQL Workbench.
* **Formato:** Divide el desarrollo en etapas secuenciales con los comandos de terminal y el código de cada archivo explicado de forma sencilla para poder seguirlo, entenderlo e implementarlo paso a paso.

---

# Prompt 2: Depuración de errores reales en migraciones y rutas de plantillas
* **Rol:** Eres un desarrollador experto en Django y bases de datos MySQL en entorno Windows.
* **Tarea:** Ayúdame a identificar y resolver dos errores que me aparecieron al ejecutar el proyecto: primero un fallo de compatibilidad al correr `makemigrations` (`NotSupportedError: MySQL 8.4 or later is required (found 8.0.46)`) y luego un error `TemplateDoesNotExist: base.html` al cargar el catálogo principal.
* **Contexto:** Estoy trabajando en VS Code con Python 3.14 y MySQL Server 8.0.46. Ya creé los modelos y los archivos HTML dentro de `templates/clinica/`, pero el servidor no logra encontrar `base.html` ni me permitía ejecutar las migraciones inicialmente.
* **Formato:** Entrega la solución directa para ambos errores, indicando el comando exacto de `pip` para ajustar la versión de Django y la ruta correcta donde debo ubicar `base.html` en mi proyecto.

---

# Prompt 3: Diseño Front-End con Bootstrap 5 y control de botones por sesión
* **Rol:** Actúa como desarrollador Front-End especializado en integración de Bootstrap 5 con plantillas DTL de Django.
* **Tarea:** Ayúdame a diseñar las pantallas de listado (`paciente_list.html`), detalle y plantilla base (`base.html`), asegurando que los botones de registrar, editar y eliminar solo se muestren cuando exista una sesión iniciada.
* **Contexto:** Necesito que el catálogo de pacientes se despliegue en tarjetas responsivas de 3 columnas, que cargue un archivo `custom.css` desde la carpeta `static/` y que incluya alertas descartables al crear, editar o eliminar un registro.
* **Formato:** Proporciona el código HTML limpio listo para integrar en mis carpetas `templates/` y `static/`, utilizando las etiquetas nativas de Django (`{% load static %}` y `{% if user.is_authenticated %}`).