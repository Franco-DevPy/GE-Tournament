from models.match import Match
from models.joueur import Joueur
from questionary import select, checkbox
from colorama import Fore, Back, Style
from models.tour import Tour


def start_match(premier_tour: Tour):

    if not isinstance(premier_tour, Tour):
        print("Error, argument is not a Tour Class")
        return

    print("Match started...")

    liste_matchs = premier_tour.liste_match
    print(Back.CYAN + "--- Liste des matchs ---")
    print(liste_matchs)

    for match_a_jouer in liste_matchs:

        print("match play :", match_a_jouer)
        resulta_match = [
            f"{match_a_jouer.joueur1.nom}",
            f"{match_a_jouer.joueur2.nom}",
            f"Egalité : {match_a_jouer.joueur1.nom} et {match_a_jouer.joueur2.nom}",
        ]

        match_a_jouer.definir_resultat(resulta_match)

        # response = select(
        #     message="Qui a gagné le match ?",
        #     choices=select_gaganant,
        # ).ask()

        # if response == match_a_jouer.joueur1.nom:

        #     match_a_jouer.joueur1.gagner_match()

        # if response == match_a_jouer.joueur2.nom:
        #     match_a_jouer.joueur2.gagner_match()
        # if (
        #     response
        #     == f"Egalité : {match_a_jouer.joueur1.nom} et {match_a_jouer.joueur2.nom}"
        # ):

        #     match_a_jouer.joueur1.egalite_match()
        #     match_a_jouer.joueur2.egalite_match()
        print(Back.GREEN + " --- Match suivant... --- ")

    print(Back.CYAN + "--- Tous les matchs ont été joués --- ")
    return


def match_suivante(liste_match: list):

    tours_suivante: Tour()

    pass


def validate_joueurs(joueurs_selectionnes):
    if len(joueurs_selectionnes) % 2 != 0:
        print(Back.YELLOW + "Nombre impair de joueurs, ajout d'un joueur 'bye'")
        joueurs_selectionnes.append("bye")  # Jugador ficticio
    return joueurs_selectionnes
