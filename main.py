import argparse
import os
import random
import schedule
import time
import logging
from playwright.sync_api import sync_playwright
from datetime import datetime, timedelta

# Configura el registro para almacenar los mensajes en un archivo
logging.basicConfig(filename='output.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class TimeManager:
    def __init__(self, entry_time="08:00", exit_time="18:00", friday_exit_time="15:00"):
        # Crea un tiempo aleatorio para la entrada, salida y salida de los viernes
        self.entry_time = self.create_random_time(entry_time)
        self.exit_time = self.create_random_time(exit_time)
        self.friday_exit_time = self.create_random_time(friday_exit_time)

    def create_random_time(self, current_time):
        # Convierte la hora actual a un objeto datetime y luego añade o resta minutos
        time_obj = datetime.strptime(current_time, "%H:%M")
        random_minutes = random.randint(0,15)
        new_time = time_obj + timedelta(minutes=random_minutes * random.choice([-1,1]))
        return new_time.strftime("%H:%M")

class Bot:
    def __init__(self, time_manager, url, username, password):
        self.time_manager = time_manager
        self.url = url
        self.username = username
        self.password = password

    def login_and_click_button(self):
        # Inicia el navegador, navega al sitio web, llena los campos y hace click en el botón
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            context = browser.new_context()
            page = context.new_page()
            page.goto(self.url)
            page.fill('input[name="username"]', self.username)
            page.fill('input[name="password"]', self.password)
            page.click('button[type="submit"]')
            page.wait_for_load_state("networkidle")
            page.click('button[id="btn-check"]')
            browser.close()

    def run_script(self):
        # Revisa la hora actual y si es el tiempo de entrada o salida, realiza el login
        current_time = time.strftime("%H:%M")
        if (time.strftime("%A") in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            and current_time == self.time_manager.entry_time):
            self.login_and_click_button()
            logging.info(f"Se ha fichado la Entrada {self.time_manager.entry_time}")
            self.time_manager.entry_time = self.time_manager.create_random_time("08:00")

        if (time.strftime("%A") in ["Monday", "Tuesday", "Wednesday", "Thursday"]
            and current_time == self.time_manager.exit_time):
            self.login_and_click_button()
            logging.info(f"Se ha fichado la Salida a las {self.time_manager.exit_time}")
            self.time_manager.exit_time = self.time_manager.create_random_time("18:00")

        # Verificar si es viernes y es la hora deseada
        if (time.strftime("%A") == "Friday" and current_time == self.time_manager.friday_exit_time):        
            self.login_and_click_button()
            logging.info(f"Se ha fichado la Salida del Viernes a las {self.time_manager.friday_exit_time}")
            self.time_manager.exit_time = self.time_manager.create_random_time("15:00")

if __name__ == "__main__":
    logging.info(f"Se ejecuta la App")
    parser = argparse.ArgumentParser(description="Realiza el inicio de sesión en una página web y pulsa un botón.")
    parser.add_argument("--url", default=os.getenv("URL"), help="URL de la página de inicio de sesión")
    parser.add_argument("--username", default=os.getenv("USERNAME"), help="Nombre de usuario para iniciar sesión")
    parser.add_argument("--password", default=os.getenv("PASSWORD"), help="Contraseña para iniciar sesión")
    args = parser.parse_args()

    time_manager = TimeManager()  # Crea una instancia de TimeManager
    bot = Bot(time_manager, args.url, args.username, args.password)  # Crea una instancia del Bot

    # Programa el bot para comprobar cada 60 segundos si se cumple alguna condición
    schedule.every(60).seconds.do(bot.run_script)

    # Ejecuta el script en bucle
    while True:
        schedule.run_pending()
        time.sleep(1)