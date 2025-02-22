from models.tournoi import Tournoi
from models.tour import Tour
from controllers.save_file import save_data_file_tournement
from controllers.joueur_controller import select_joueur_tournoi, get_all_players_id_dict
from colorama import Fore, Back, Style, init
from datetime import datetime as dt
from questionary import select, Style as QuestionaryStyle
from typing import List
from pathlib import Path
import json
from questionary import checkbox


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
    tournois_selectione = select_tournoi_finit()
    print(" tournois_selectione : ", tournois_selectione)
    tournois_selectione.voir_classement()


def load_and_reconstruct_tournaments_termine():
    data = Path("data/tournament.json").read_text(encoding="utf-8")
    tournaments_list = json.loads(data)

    players_dict = get_all_players_id_dict()

    reconstructed_tournaments = []

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

    return reconstructed_tournaments


def select_tournoi_finit() -> List[Tournoi]:
    liste_tournois = load_and_reconstruct_tournaments_termine()

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
