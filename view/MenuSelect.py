import colorama
from colorama import Fore, Back, Style
from questionary import select, Style as QuestionaryStyle
from controllers.joueur_controller import *
from controllers.tournoi_controller import *
from controllers.match_controller import *
import time
import os
import platform
from controllers.save_file import *
from models.match import *
from models.tour import *


colorama.init(autoreset=True)
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

        new_tournoi = create_tournoi()

        premier_tour = new_tournoi.liste_tour[0]

        menu_start_tournois(premier_tour)  # llama a start_match

        while len(new_tournoi.liste_tour) < new_tournoi.nombre_tour:
            print("-------------------------------------------------")

            if len(new_tournoi.liste_tour) < new_tournoi.nombre_tour:
                new_tournoi.generate_tour()
            tours_suivante = new_tournoi.liste_tour[-1]
            menu_match_suivant()
            print("start match - tour 2")
            start_match(tours_suivante)
            save_tournois = new_tournoi.to_dict()
            save_data_file_tournement(save_tournois)
            if len(new_tournoi.liste_tour) < new_tournoi.nombre_tour:
                menu_tour_suivant()
            pass

        print(
            Back.BLACK
            + Fore.BLUE
            + """
     ___ ___ _  _   ___  _   _   _____ ___  _   _ ___ _  _  ___ ___   
    | __|_ _| \| | |   \| | | | |_   _/ _ \| | | | _ \ \| |/ _ \_ _| 
    | _| | || .` | | |) | |_| |   | || (_) | |_| |   / .` | (_) | |  
    |_| |___|_|\_| |___/ \___/    |_| \___/ \___/|_|_\_|\_|\___/___|
                """
            + Style.RESET_ALL
            + "\n"
        )
        menu_fin_tournois(new_tournoi)

    if respuesta == "Gestion du Joueur":
        print("Gestion du joueur....")
        menu_joueur()

    if respuesta == "Charger Dernier Tournois":
        menu_charger_tournois()
        print("Dernier tournois....")

    if respuesta == "Exit":
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
        # BaseExcept
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
        "Charger Tournois",
        "Voir Tournois",
        "Revenir au Menu",
    ]

    response = select(
        message="Choisisez une option : ",
        choices=select_tournois,
        style=custom_style,
    ).ask()

    if response == "Charger Tournois":
        print("Charger Tournois....")
        resetApp()

    if response == "Voir Tournois":
        print("Voir Tournois....")

        resetApp()

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
