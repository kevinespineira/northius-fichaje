import argparse
import os
import random
import schedule
import time
from playwright.sync_api import sync_playwright
from datetime import datetime, timedelta


def create_random_time(current_time):
    # Convertir la cadena de texto a un objeto datetime
    time_obj = datetime.strptime(current_time, "%H:%M")

    # Generar un número aleatorio entre 0 y 15
    random_minutes = random.randint(0, 15)

    # Elegir aleatoriamente entre sumar o restar el número de minutos generados
    operation = random.choice([-1, 1])

    # Calcular el nuevo tiempo sumando o restando los minutos aleatorios
    new_time = time_obj + timedelta(minutes=random_minutes * operation)

    # Convertir el nuevo tiempo a formato de cadena de texto
    new_time_str = new_time.strftime("%H:%M")

    return new_time_str


global HORA_ENTRADA 
HORA_ENTRADA = create_random_time("08:00")
global HORA_SALIDA 
HORA_SALIDA = create_random_time("18:00")
global HORA_SALIDA_VIERNES 
HORA_SALIDA_VIERNES= create_random_time("15:00")


def login_and_click_button(url, username, password):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # Navegar a la página de inicio de sesión
        page.goto(url)

        # Rellenar el formulario de inicio de sesión
        page.fill('input[name="username"]', username)
        page.fill('input[name="password"]', password)

        # Hacer clic en el botón de inicio de sesión
        page.click('button[type="submit"]')

        # Esperar a que se cargue la siguiente página
        page.wait_for_load_state("networkidle")

        # Realizar otras acciones después de iniciar sesión
        page.click('button[id="btn-check"]')

        # Cerrar el navegador
        browser.close()


def run_script():
    # Obtener la hora actual
    current_time = time.strftime("%H:%M")
    global HORA_ENTRADA
    global HORA_SALIDA
    global HORA_SALIDA_VIERNES 

    # Verificar si es de lunes a viernes y es la hora deseada
    if (time.strftime("%A") in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] and current_time == HORA_ENTRADA):
        login_and_click_button(args.url, args.username, args.password)
        HORA_ENTRADA = create_random_time("08:00")

    # Verificar si es de lunes a jueves y es la hora deseada
    if (time.strftime("%A") in ["Monday", "Tuesday", "Wednesday", "Thursday"] and current_time == HORA_SALIDA): 
        HORA_SALIDA = create_random_time("18:00")
        login_and_click_button(args.url, args.username, args.password)

    # Verificar si es viernes y es la hora deseada
    if time.strftime("%A") == "Friday" and current_time == HORA_SALIDA_VIERNES:
        HORA_SALIDA_VIERNES = create_random_time("15:00")
        login_and_click_button(args.url, args.username, args.password)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Realiza el inicio de sesión en una página web y pulsa un botón."
    )
    parser.add_argument(
        "--url", default=os.getenv("URL"), help="URL de la página de inicio de sesión"
    )
    parser.add_argument(
        "--username",
        default=os.getenv("USERNAME"),
        help="Nombre de usuario para iniciar sesión",
    )
    parser.add_argument(
        "--password",
        default=os.getenv("PASSWORD"),
        help="Contraseña para iniciar sesión",
    )

    args = parser.parse_args()
    current_time = time.strftime("%H:%M")
    # Comprueba cada 60 segundos si se cumple alguna condicion
    schedule.every(60).seconds.do(run_script)

    # Ejecutar el script en bucle
    while True:
        schedule.run_pending()
        time.sleep(1)
