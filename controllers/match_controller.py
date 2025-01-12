from models.match import Match
from models.joueur import Joueur
from questionary import select, checkbox
from colorama import Fore, Back, Style
from models.tour import Tour
from typing import List


def start_match(premier_tour: Tour):

    if not isinstance(premier_tour, Tour):
        print("Error, argument is not a Tour Class")
        return

    liste_matchs: List[Match] = premier_tour.liste_match
    print(Back.CYAN + "--- Liste des matchs ---")

    for match_a_jouer in liste_matchs:

        print("match play :", match_a_jouer)
        select_gagnat = [
            f"{match_a_jouer.joueur1.nom}",
            f"{match_a_jouer.joueur2.nom}",
            f"Egalité : {match_a_jouer.joueur1.nom} et {match_a_jouer.joueur2.nom}",
        ]

        resulta_match = select(
            message="Qui a gagné le match ?",
            choices=select_gagnat,
        ).ask()

        if resulta_match == match_a_jouer.joueur1.nom:
            match_a_jouer.definir_resultat("joueur1")
        elif resulta_match == match_a_jouer.joueur2.nom:
            match_a_jouer.definir_resultat("joueur2")
        else:
            match_a_jouer.definir_resultat("egalite")

        # match_a_jouer.match_suivant()
        print(Back.GREEN + " --- Match suivant... --- ")

    print(Back.CYAN + "--- Tous les matchs ont été joués --- ")
    premier_tour.nom_tour += 1

    return


def match_suivante(liste_match: list):

    tours_suivante: Tour()

    pass


def validate_joueurs(joueurs_selectionnes):
    if len(joueurs_selectionnes) % 2 != 0:
        print(Back.YELLOW + "Nombre impair de joueurs, ajout d'un joueur 'bye'")
        joueurs_selectionnes.append("bye")  # Jugador ficticio
    return joueurs_selectionnes
