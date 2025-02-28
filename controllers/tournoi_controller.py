from models.tournoi import Tournoi
from models.tour import Tour
from controllers.save_file import save_data_file_tournement
from controllers.joueur_controller import select_joueur_tournoi, get_all_players_id_dict
from colorama import Back, Style, init
from questionary import select, Style as QuestionaryStyle
from typing import List
from pathlib import Path
import json
import platform
import os
import time
from controllers.match_controller import start_match

# from save_file import save_data_file_tournement


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


def create_tournoi() -> Tournoi:
    print(Back.BLUE + "-----Creation du Tournoi-----")

    # reponse_dernier_tournoi = get_dernier_tournois()
    nom_tournoi = input("Entrez le NOM du Tournoi : ")
    lieu_tournoi = input("Entrez le LIEU du Tournoi : ")
    # date_debut = dt.now().strftime("%Y-%m-%d %H:%M")

    description_tournoi = input("Entrez une description du Tournoi : ")
    joueurs_selectionnes = select_joueur_tournoi()

    new_tournoi = Tournoi(
        nom_tournoi=nom_tournoi,
        location=lieu_tournoi,
        description=description_tournoi,
        liste_joueur=joueurs_selectionnes,
    )

    # GENERATE FIRST TOUR
    new_tournoi.generate_tour()

    save_data_file_tournement(new_tournoi)

    return new_tournoi


def charger_tournois_termines():
    tournois_selectione = select_tournoi_finit(finit=True)
    print(" tournois_selectione : ", tournois_selectione)
    tournois_selectione.voir_classement()


def charger_tournois_en_cours():
    tournois_selectione = select_tournoi_finit(finit=False)
    print(" tournois_selectione : ", tournois_selectione)
    print("ici")
    continuer_tour(tournois_selectione)


def select_tournoi_finit(finit: bool) -> List[Tournoi]:

    if finit == True:
        liste_tournois = load_and_reconstruct_tournaments(finit=True)
    else:
        liste_tournois = load_and_reconstruct_tournaments(finit=False)

    choices = []

    for tournoi in liste_tournois:
        choices.append(
            {
                "name": f"{tournoi.nom_tournoi} - {tournoi.location} - ({tournoi.date_debut})",
                "value": tournoi,
            }
        )

    rpse_choix_joueur = select(
        "Selectioner Tournois ",
        choices=choices,
        style=custom_style,
    ).ask()

    if rpse_choix_joueur is None:
        print(Back.RED + " -- ⚠ VOUS DEVEZ SELECTIONNER AU MOINS UN TOURNOI. ⚠ -- ")

    else:
        return rpse_choix_joueur


def load_and_reconstruct_tournaments(finit: bool):
    data = Path("data/tournament.json").read_text(encoding="utf-8")
    tournaments_list = json.loads(data)

    players_dict = get_all_players_id_dict()

    reconstructed_tournaments = []
    if finit == True:
        for tournament_data in tournaments_list:
            if tournament_data.get("date_fin") is not None:
                tournament = Tournoi(
                    nom_tournoi=tournament_data.get("nom_tournoi", ""),
                    location=tournament_data.get("location", ""),
                    date_debut=tournament_data.get("date_debut"),
                    date_fin=tournament_data.get("date_fin"),
                    description=tournament_data.get("description", ""),
                    nombre_tour=tournament_data.get("nombre_tour", 4),
                    liste_joueur=[],
                    liste_tour=[
                        Tour.from_dict(tour_data, players_dict, generate_matches=False)
                        for tour_data in tournament_data.get("liste_tour", [])
                    ],
                )

                tournament.liste_joueur = [
                    players_dict[joueur_data["id_national"]]
                    for joueur_data in tournament_data.get("liste_joueur", [])
                ]

                reconstructed_tournaments.append(tournament)
    if finit == False:
        for tournament_data in tournaments_list:
            if tournament_data.get("date_fin") is None:
                tournament = Tournoi(
                    nom_tournoi=tournament_data.get("nom_tournoi", ""),
                    location=tournament_data.get("location", ""),
                    date_debut=tournament_data.get("date_debut"),
                    date_fin=tournament_data.get("date_fin"),
                    description=tournament_data.get("description", ""),
                    nombre_tour=tournament_data.get("nombre_tour", 4),
                    liste_joueur=[],
                    liste_tour=[
                        Tour.from_dict(tour_data, players_dict, generate_matches=False)
                        for tour_data in tournament_data.get("liste_tour", [])
                    ],
                )

                tournament.liste_joueur = [
                    players_dict[joueur_data["id_national"]]
                    for joueur_data in tournament_data.get("liste_joueur", [])
                ]

                reconstructed_tournaments.append(tournament)

    return reconstructed_tournaments


def continuer_tour(tournoi_selectione):
    while len(tournoi_selectione.liste_tour) < tournoi_selectione.nombre_tour:
        if len(tournoi_selectione.liste_tour) < tournoi_selectione.nombre_tour:
            tournoi_selectione.generate_tour()
        menu_match_suivant()
        tours_suivante = tournoi_selectione.liste_tour[-1]
        start_match(tours_suivante)
        save_data_file_tournement(tournoi_selectione)
        if len(tournoi_selectione.liste_tour) < tournoi_selectione.nombre_tour:
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
    tournoi_selectione.date_fin = tournoi_selectione.get_time()
    save_data_file_tournement(tournoi_selectione)
    exit()
    return


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


def resetApp():
    clear_console()
    print("Loading...")
    time.sleep(0.5)
    clear_console()
    exit()


def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
