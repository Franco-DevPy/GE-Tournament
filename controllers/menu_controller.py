from colorama import Back, Style
from questionary import select, Style as QuestionaryStyle
import os
import platform
import time

custom_style = QuestionaryStyle(
    [
        ("qmark", "fg:#E91E63 bold"),
        ("question", "bold"),
        ("pointer", "fg:#1815d1 bold"),
        ("highlighted", "fg:#03A9F4"),
        ("selected", "fg:#0D47A1"),
        ("answer", "fg:#2196f3 bold"),
        ("text", "bold"),
        ("separator", "fg:#CC5454"),
        ("instruction", "#0D47A1"),
        ("disabled", "fg:#858585 italic"),
    ]
)


def menu_match_suivant():
    select_start = ["Jouer Tour", "Revenir au Menu"]
    response = select(
        message="Choisisez une option : ",
        choices=select_start,
        style=custom_style,
    ).ask()
    if response == "Jouer Tour":
        pass
    if response == "Revenir au Menu":
        resetApp()


def menu_tour_suivant():
    select_start = ["Tour Suivante", "Revenir au Menu"]
    response = select(
        message="Choisisez une option : ",
        choices=select_start,
        style=custom_style,
    ).ask()
    if response == "Tour Suivante":
        pass
    if response == "Revenir au Menu":
        resetApp()


def menu_fin_tournois(tournois):
    select_sub_menu = [
        "Voir le classement",
        "Revenir au Menu",
    ]
    response = select(
        message="Choisisez une option : ",
        choices=select_sub_menu,
        style=custom_style,
    ).ask()
    if response == "Voir le classement":
        tournois.voir_classement()
        menu_back()
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


def resetApp():
    clear_console()
    print("Loading...")
    time.sleep(0.5)
    clear_console()
    start_app()


def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
