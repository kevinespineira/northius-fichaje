# Script de inicio de sesión con Playwright

Este script de Python utiliza Playwright para iniciar sesión en una página web y pulsar un botón. Puede ser ejecutado desde la línea de comandos o utilizando variables de entorno.

## Requisitos

- Python 3.6 o superior
- Playwright (`pip install playwright`)
- Ejecutar `playwright install` para descargar los navegadores necesarios

## Uso

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

Si se proporcionan argumentos de la línea de comandos, estos sobrescribirán las variables de entorno.

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
