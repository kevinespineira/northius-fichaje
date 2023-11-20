import argparse
import os
from playwright.sync_api import sync_playwright

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
        page.wait_for_load_state('networkidle')

        # Realizar otras acciones después de iniciar sesión
        page.click('button[id="btn-check"]')
        
        # Cerrar el navegador
        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Realiza el inicio de sesión en una página web y pulsa un botón.')
    parser.add_argument('--url', default=os.getenv('URL'), help='URL de la página de inicio de sesión')
    parser.add_argument('--username', default=os.getenv('USERNAME'), help='Nombre de usuario para iniciar sesión')
    parser.add_argument('--password', default=os.getenv('PASSWORD'), help='Contraseña para iniciar sesión')

    args = parser.parse_args()

    login_and_click_button(args.url, args.username, args.password)