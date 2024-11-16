from colorama import Fore, Back, Style as init
from questionary import select, Style as QuestionaryStyle
from controllers.joueur_controller import *
import time
import os
import platform
from controllers.save_file import *


init(autoreset=True)

custom_style = QuestionaryStyle(
    [
        ("qmark", "fg:#E91E63 bold"),  # Color del símbolo de pregunta
        ("question", "bold"),  # Estilo del mensaje de pregunta
        ("pointer", "fg:#1815d1 bold"),  # Color del puntero en las opciones
        ("highlighted", "fg:#03A9F4"),  # Color de la opción resaltada
        ("selected", "fg:#0D47A1"),  # Color de la opción seleccionada
        ("answer", "fg:#2196f3 bold"),  # Color de la respuesta
        ("text", "bold"),  # Estilo del texto (por defecto)
        ("separator", "fg:#CC5454"),  # Estilo del separador
        ("instruction", "#0D47A1"),  # Estilo de las instrucciones (si las hay)
        ("disabled", "fg:#858585 italic"),  # Estilo de opciones deshabilitadas
    ]
)


def start_app():

    load_data_file_players()

    print(
        Back.CYAN
        + Fore.BLACK
        + """  ♟ ♜ ♞ ♝ ♛ ÉCHECSMANAGER ♚ ♝ ♞ ♜ ♟   """
        + Style.RESET_ALL
    )
    select_menu = [
        "Creér un Tournois",
        "Gestion du Joueur",
        "Charger Dernier Tournois",
        "Exit",
    ]

    respuesta = select(
        message="--Menu Principal--",
        choices=select_menu,
        style=custom_style,
    ).ask()

    if respuesta == "Creér un Tournois":
        print("Nouve Tournois Crée...")
        time.sleep(2)
        resetApp()

    if respuesta == "Gestion du Joueur":
        print("Gestion du joueur....")
        menu_joueur()

    if respuesta == "Charger Dernier Tournois":
        print("Dernier tournois....")

    if respuesta == "Exit":
        clear_console()
        print("Exit...")
        time.sleep(1)
        exit_app()


def menu_joueur():
    print(Back.BLUE + "-----Gérer les Joueurs-----")

    select_menu = [
        "Ajouter un Joueur",
        "Voir Liste de Joueur",
        "Revenir au Menu",
    ]

    select_sub_menu = [
        "Revenir au Menu",
    ]

    select_back = ["Ajouter un Joueur", "Revenir au Menu"]

    respuesta = select(
        message="Choisisez une option : ",
        choices=select_menu,
        style=custom_style,
    ).ask()

    if respuesta == "Ajouter un Joueur":
        continuer = True
        while continuer == True:
            print(Back.BLUE + "-----Ajouter un Joueur-----")
            ajouter_joueur()
            reponse = select(
                message="Choisisez une option : ",
                choices=select_back,
                style=custom_style,
            ).ask()

            if reponse == "Revenir au Menu":
                break

        resetApp()

    if respuesta == "Voir Liste de Joueur":
        try:
            print("Cargando lista...")
            time.sleep(2)

            liste = get_liste_joueur()

            if not liste:
                print(Back.RED + Fore.BLACK + "LISTE DES JOUEUR VIDE")
                menu_back()

            voir_liste_joueur(liste)
            time.sleep(5)
            respuesta2 = select(
                message="Choisisez une option : ",
                choices=select_sub_menu,
                style=custom_style,
            ).ask()

            if respuesta2 == "Revenir au Menu":
                resetApp()

        except:
            print("Error al cargar...")
            time.sleep(5)
            respuesta2 = select(
                message="Choisisez une option : ",
                choices=select_sub_menu,
                style=custom_style,
            ).ask()

            if respuesta2 == "Revenir au Menu":
                resetApp()

    if respuesta == "Revenir au Menu":
        resetApp()


def menu_back():

    select_sub_menu = [
        "Revenir au Menu",
    ]

    response = select(
        message="Choisisez une option : ",
        choices=select_sub_menu,
        style=custom_style,
    ).ask()

    if response == "Revenir au Menu":
        resetApp()


def menu_back():

    select_sub_menu = [
        "Revenir au Menu",
    ]

    response = select(
        message="Choisisez une option : ",
        choices=select_sub_menu,
        style=custom_style,
    ).ask()

    if response == "Revenir au Menu":
        resetApp()


def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def resetApp():
    clear_console()
    print("Loading...")
    time.sleep(0.5)
    clear_console()
    start_app()


def exit_app():
    clear_console()
    exit()
