import colorama
from colorama import Fore, Back, Style
from questionary import select, Style as QuestionaryStyle
from controllers.joueur_controller import (
    ajouter_joueur,
    voir_liste_joueur,
    get_liste_joueur,
    load_data_file_players,
)
from controllers.tournoi_controller import (
    create_tournoi,
    charger_tournois_en_cours,
    charger_tournois_termines,
)
from controllers.match_controller import start_match
import time
import os
import platform
from controllers.save_file import save_data_file_tournement
from models.tour import Tour
from models.tournoi import Tournoi


colorama.init(autoreset=True)
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
        "Gestion des Tournois",
        "Exit",
    ]

    respuesta = select(
        message="--Menu Principal--",
        choices=select_menu,
        style=custom_style,
    ).ask()

    if respuesta == "Creér un Tournois":

        new_tournoi = create_tournoi()

        premier_tour = new_tournoi.liste_tour[0]

        menu_start_tournois(premier_tour)

        print(len(new_tournoi.liste_tour) < new_tournoi.nombre_tour)
        while len(new_tournoi.liste_tour) < new_tournoi.nombre_tour:
            if len(new_tournoi.liste_tour) < new_tournoi.nombre_tour:
                new_tournoi.generate_tour()
            menu_match_suivant()
            tours_suivante = new_tournoi.liste_tour[-1]
            start_match(tours_suivante)
            save_data_file_tournement(new_tournoi)
            if len(new_tournoi.liste_tour) < new_tournoi.nombre_tour:
                menu_tour_suivant()
            pass

        print(
            Back.BLACK
            + """
     ___ ___ _  _   ___  _   _   _____ ___  _   _ ___ _  _  ___ ___
    | __|_ _| \| | |   \| | | | |_   _/ _ \| | | | _ \ \| |/ _ \_ _|
    | _| | || .` | | |) | |_| |   | || (_) | |_| |   / .` | (_) | |
    |_| |___|_|\_| |___/ \___/    |_| \___/ \___/|_|_\_|\_|\___/___|
                """
            + Style.RESET_ALL
            + "\n"
        )
        new_tournoi.date_fin = new_tournoi.get_time()
        save_data_file_tournement(new_tournoi)
        menu_fin_tournois(new_tournoi)

    if respuesta == "Gestion du Joueur":
        print("Gestion du joueur....")
        menu_joueur()
        return

    if respuesta == "Gestion des Tournois":
        menu_charger_tournois()
        print("Dernier tournois....")
        return

    if respuesta == "Exit":
        return exit_app()


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
        while continuer:
            print(Back.BLUE + "-----Ajouter un Joueur-----")
            ajouter_joueur()
            reponse = select(
                message="Choisisez une option : ",
                choices=select_back,
                style=custom_style,
            ).ask()

            if reponse == "Revenir au Menu":
                break

        return resetApp()

    if respuesta == "Voir Liste de Joueur":
        try:
            print("Chargement de la liste des joueurs...")
            time.sleep(1)

            liste_class_j = get_liste_joueur()

            if not liste_class_j:
                print(Back.RED + Fore.BLACK + "LISTE DES JOUEUR VIDE")
                menu_back()

            voir_liste_joueur(liste_class_j)
            respuesta2 = select(
                message="Choisisez une option : ",
                choices=select_sub_menu,
                style=custom_style,
            ).ask()

            if respuesta2 == "Revenir au Menu":
                resetApp()
        except Exception:
            print("Erreur de chargement de la liste des joueurs...")
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


def menu_fin_tournois(tournois: Tournoi):
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


def menu_start_tournois(premier_tour: Tour):

    select_start = ["Commencer Tournois", "Revenir au Menu"]

    response = select(
        message="Choisisez une option : ",
        choices=select_start,
        style=custom_style,
    ).ask()

    if response == "Commencer Tournois":
        start_match(premier_tour)

    if response == "Revenir au Menu":
        resetApp()


def menu_charger_tournois():
    select_tournois = [
        "Charger Tournois en Cours",
        "Charger Tournois Terminés",
        "Revenir au Menu",
    ]

    response = select(
        message="Choisisez une option : ",
        choices=select_tournois,
        style=custom_style,
    ).ask()

    if response == "Charger Tournois en Cours":
        charger_tournois_en_cours()
        menu_back()

    if response == "Charger Tournois Terminés":
        charger_tournois_termines()
        menu_back()

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
    time.sleep(1)
    print(
        Fore.CYAN
        + r"""        
-----------------------------------------------------------------       
                                                     _:_
                                                    '-.-'
                                           ()      __.'.__
                                        .-:--:-.  |_______|
                                 ()      \____/    \=====/
                                 /\      {====}     )___(
                      (\=,      //\\      )__(     /_____\
      __    |'-'-'|  //  .\    (    )    /____\     |   |
     /  \   |_____| (( \_  \    )__(      |  |      |   |
     \__/    |===|   ))  `\_)  /____\     |  |      |   |
    /____\   |   |  (/     \    |  |      |  |      |   |
     |  |    |   |   | _.-'|    |  |      |  |      |   |
     |__|    )___(    )___(    /____\    /____\    /_____\
    (====)  (=====)  (=====)  (======)  (======)  (=======)
    }===={  }====={  }====={  }======{  }======{  }======={
   (______)(_______)(_______)(________)(________)(_________)   
-----------------------------------------------------------------
            _     ___ ___ ___ _  _ _____ ___ _____ _ 
           /_\   | _ )_ _| __| \| |_   _/ _ \_   _| |
          / _ \  | _ \| || _|| .` | | || (_) || | |_|
         /_/ \_\ |___/___|___|_|\_| |_| \___/ |_| (_)                                            
----------------------------------------------------------------- 
"""
    )
    exit()
    return
