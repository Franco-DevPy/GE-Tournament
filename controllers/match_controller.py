from models.match import Match
from models.joueur import Joueur
from questionary import select, checkbox
from colorama import Fore, Back, Style


def start_match(matchs: list):

    if not isinstance(matchs, list):
        print("Error, argument is not a match list")
        return

    print("Match started...")

    while len(matchs) > 0:

        match_play = matchs.pop(0)
        select_gaganant = [
            f"{match_play.joueur1.nom}",
            f"{match_play.joueur2.nom}",
            f"Egalité : {match_play.joueur1.nom} et {match_play.joueur2.nom}",
        ]

        response = select(
            message="Qui a gagné le match ?",
            choices=select_gaganant,
        ).ask()

        if response == match_play.joueur1.nom:
            print(f"{Back.BLUE} Le joueur {match_play.joueur1.nom} a gagné le match ")
        if response == match_play.joueur2.nom:
            print(f"Le joueur {match_play.joueur2.nom} a gagné le match")
        if (
            response
            == f"Egalité : {match_play.joueur1.nom} et {match_play.joueur2.nom}"
        ):
            print(f"Le match est nul")
        print(Back.GREEN + " --- Match suivant... --- ")

    print("Tous les matchs ont été joués")
    return
