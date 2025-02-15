from models.tournoi import Tournoi
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
    try:
        tournois_selectione = select_tournoi_finit()
        tournois_selectione.voir_classement()
    except Exception as e:
        print(f"Error en charger_tournois_termines: {e}")


def load_and_reconstruct_tournaments() -> List[Tournoi]:
    try:
        # Cargar datos de torneos desde el archivo JSON

        data = Path("data/tournament.json").read_text(encoding="utf-8")
        tournaments_list = json.loads(data)

        # Obtener el diccionario de jugadores
        players_dict = get_all_players_id_dict()

        # Lista para almacenar los torneos reconstruidos
        reconstructed_tournaments = []

        for tournament_data in tournaments_list:
            # Crear una instancia de Tournoi desde el diccionario
            tournament = Tournoi.from_dict(tournament_data)

            # Reconstruir la lista de jugadores del torneo
            tournament.liste_joueur = [
                players_dict[joueur_id] for joueur_id in tournament.liste_joueur_ids
            ]

            # Añadir el torneo reconstruido a la lista
            reconstructed_tournaments.append(tournament)

        return reconstructed_tournaments

    except Exception as e:
        print(f"Error en load_and_reconstruct_tournaments: {e}")
        return []


# def charger_tournois_termines():
#     print(Back.BLUE + "-----Liste des tournois terminés-----")
#     liste_tournois =
#     print("Liste des tournois terminés : ")
#     print(liste_tournois)
#     print("\n")
#     print("Liste des tournois terminés ITERADO : ")
#     nt = 0
#     for tournoi in liste_tournois:
#         print(f"Tournoi : {nt} ")
#         print(tournoi)
#         nt += 1

#     pass


def select_tournoi_finit() -> List[Tournoi]:

    liste_tournois = load_and_reconstruct_tournaments()

    print("liste_tournois : ", liste_tournois)
    print("antess de la boucle")
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
