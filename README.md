# Autofichaje en Northius

Este script de Python utiliza Playwright para iniciar sesión en una página web y pulsar un botón. Puede ser ejecutado desde la línea de comandos o utilizando variables de entorno.

## Requisitos

- Python 3.6 o superior
- Playwright (`pip install playwright` o `py -m pip install playwright` en Windows)
- Ejecutar `playwright install` para descargar los navegadores necesarios (`py -m playwright install` en Windows)

## Uso

### En Linux

Puede ejecutar el script desde la línea de comandos proporcionando los argumentos necesarios:

```bash
python main.py --url <URL> --username <USERNAME> --password <PASSWORD>
```

También puede utilizar variables de entorno para proporcionar los argumentos:

```bash
export URL=<URL>
export USERNAME=<USERNAME>
export PASSWORD=<PASSWORD>
python main.py
```

### En Windows

Puede ejecutar el script desde la línea de comandos proporcionando los argumentos necesarios:

```bash
py main.py --url <URL> --username <USERNAME> --password <PASSWORD>
```

También puede utilizar variables de entorno para proporcionar los argumentos:

```bash
set URL=<URL>
set USERNAME=<USERNAME>
set PASSWORD=<PASSWORD>
py main.py
```

Si se proporcionan argumentos de la línea de comandos, estos sobrescribirán las variables de entorno.

## Configuración de tareas automatizadas

### En Linux

Puede programar el script para ejecutarse regularmente utilizando crontab. Para editar la tabla de cron, utilice el comando `crontab -e` y añada una línea como la siguiente:

```bash
0 * * * * python /ruta/absoluta/a/main.py --url <URL> --username <USERNAME> --password <PASSWORD>
```

Esto ejecutará el script al principio de cada hora. Modifique los números al principio de la línea para cambiar la programación.

### En Windows

Puede programar el script para ejecutarse regularmente utilizando el Programador de Tareas de Windows. Cree una tarea nueva y configure la acción para iniciar un programa con los siguientes detalles:

- Programa: `C:\ruta\absoluta\a\python.exe`
- Argumentos: `C:\ruta\absoluta\a\main.py --url <URL> --username <USERNAME> --password <PASSWORD>`

Puede ajustar las condiciones y la configuración de la tarea según sus necesidades.

## Argumentos

- `--url`: URL de la página de inicio de sesión (requerido)
- `--username`: Nombre de usuario para iniciar sesión (requerido)
- `--password`: Contraseña para iniciar sesión (requerido)

## Variables de entorno

- `URL`: URL de la página de inicio de sesión
- `USERNAME`: Nombre de usuario para iniciar sesión
- `PASSWORD`: Contraseña para iniciar sesión

## Funcionamiento

1. Lanza un nuevo navegador utilizando Playwright.
2. Navega a la URL proporcionada.
3. Rellena el formulario de inicio de sesión con el nombre de usuario y la contraseña proporcionados.
4. Hace clic en el botón de inicio de sesión.
5. Espera a que se cargue la siguiente página.
6. Hace clic en un botón con el ID "btn-check".
7. Cierra el navegador.