import flet as ft
import time


# Simulamos la terminal
async def main_ui(page: ft.Page):
    page.window.width = 900
    page.window.height = 800
    page.padding = 0
    page.margin = 0

    # Contenedor para mostrar el "output" (equivalente a la terminal)
    terminal_output = ft.Column(scroll=ft.ScrollMode.AUTO)

    # Función para agregar mensajes a la terminal
    def print_to_terminal(message):
        terminal_output.controls.append(ft.Text(message, color=ft.colors.WHITE))
        terminal_output.update()

    # Función para manejar el menú principal
    def start_app():
        print_to_terminal("-----Bienvenue à Tournois D'échecs-----")
        select_menu = [
            "Créer un Tournoi",
            "Gestion du Joueur",
            "Charger Dernier Tournoi",
            "Exit",
        ]

        menu_buttons.controls.clear()
        for option in select_menu:
            menu_buttons.controls.append(
                ft.ElevatedButton(
                    option, on_click=lambda e, opt=option: handle_main_menu(opt)
                )
            )
        menu_buttons.update()

    # Función para manejar las opciones del menú principal
    def handle_main_menu(option):
        if option == "Créer un Tournoi":
            print_to_terminal("Nouveau Tournoi Créé...")
        elif option == "Gestion du Joueur":
            print_to_terminal("Gestion du joueur...")
            menu_joueur()
        elif option == "Charger Dernier Tournoi":
            print_to_terminal("Dernier tournoi chargé...")
        elif option == "Exit":
            print_to_terminal("Exit...")
            time.sleep(1)
            exit_app()

    # Función para el submenú de gestión de jugadores
    def menu_joueur():
        print_to_terminal("Gestion des Joueurs")
        select_menu = [
            "Ajouter un Joueur",
            "Voir Liste de Joueurs",
            "Revenir au Menu",
        ]

        menu_buttons.controls.clear()
        for option in select_menu:
            menu_buttons.controls.append(
                ft.ElevatedButton(
                    option, on_click=lambda e, opt=option: handle_joueur_menu(opt)
                )
            )
        menu_buttons.update()

    # Función para manejar las opciones del submenú de jugadores
    def handle_joueur_menu(option):
        if option == "Ajouter un Joueur":
            print_to_terminal("Ajouter un Joueur...")
            # Aquí puedes llamar a la lógica de "ajouter_joueur()"
        elif option == "Voir Liste de Joueurs":
            print_to_terminal("Liste des Joueurs...")
            # Aquí puedes llamar a la lógica de "voir_liste_joueur()"
        elif option == "Revenir au Menu":
            reset_app()

    # Función para limpiar la "consola"
    def clear_console():
        terminal_output.controls.clear()
        terminal_output.update()

    # Función para reiniciar la app
    def reset_app():
        clear_console()
        start_app()

    # Función para salir de la app
    def exit_app():
        page.window_close()

    # Contenedor para los botones del menú
    menu_buttons = ft.Column()

    # Estructura principal de la interfaz
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Terminal (Simulación):", size=20, color=ft.colors.WHITE),
                    ft.Container(
                        content=terminal_output,
                        bgcolor=ft.colors.BLACK,
                        width=800,
                        height=400,
                        padding=10,
                        border_radius=10,
                        border=ft.border.all(1, ft.colors.WHITE),
                    ),
                    menu_buttons,
                ],
                spacing=20,
            ),
            alignment=ft.alignment.center,
        )
    )

    # Inicia la app
    start_app()


ft.app(target=main_ui)


"""


import flet as ft

async def main_ui(page: ft.Page):
    # Configuramos la ventana
    page.window.width = 900
    page.window.height = 800
    page.window.resizable = False
    page.padding = 0
    page.margin = 0

    # Lista para almacenar los mensajes de salida (prints)
    terminal_output = ft.Column(scroll=ft.ScrollMode.AUTO)

    # Función para manejar el envío de comandos
    def handle_command(e):
        # Obtén el texto ingresado por el usuario
        command = input_field.value
        if command.strip():  # Solo procesa si hay texto
            # Muestra el comando en la terminal
            terminal_output.controls.append(ft.Text(f"> {command}", color=ft.colors.GREEN))
            # Simula una respuesta o lógica
            terminal_output.controls.append(ft.Text(f"Resultado: Procesado '{command}'", color=ft.colors.WHITE))
            # Desplaza hacia abajo para mostrar la última línea
            terminal_output.update()
        input_field.value = ""  # Limpia el campo de texto
        input_field.update()

    # Campo para capturar entrada del usuario
    input_field = ft.TextField(
        label="Escribe un comando:",
        on_submit=handle_command,  # Procesa cuando se presiona Enter
        expand=True,  # Ocupa todo el ancho disponible
    )

    # Contenedor que simula la terminal
    centro = ft.Container(
        content=ft.Column(
            [
                ft.Text("Terminal (Simulación):", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                terminal_output,  # Aquí se mostrarán los "prints"
                input_field,  # Campo de entrada
            ],
            spacing=10,
        ),
        width=700,
        height=400,
        bgcolor=ft.colors.BLACK,
        alignment=ft.alignment.top_center,
        border=ft.border.all(color=ft.colors.WHITE),
        padding=10,
    )

    # Contenedor inferior
    inferior = ft.Container(
        width=700,
        height=100,
        bgcolor=ft.colors.WHITE,
        alignment=ft.alignment.center,
        border=ft.border.all(),
    )

    # Imagen que ocupa el ancho completo de la ventana
    imagen = ft.Image(
        src="https://img.freepik.com/photos-premium/image-panoramique-jeu-echecs_20693-354.jpg",
        fit=ft.ImageFit.COVER,
        width=page.window.width,
        height=200,
    )

    # Organizar los elementos
    col = ft.Column(
        spacing=20,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            imagen,  # La imagen ocupa el ancho completo
            centro,  # La terminal simulada
            inferior,  # Sección inferior
        ],
    )

    contenedor = ft.Container(
        content=col,
        width=900,
        height=800,
        bgcolor=ft.colors.BLACK,
        alignment=ft.alignment.top_center,
    )

    # Agregar el contenedor principal a la página
    page.add(contenedor)

ft.app(target=main_ui)





"""
