from models.match import Match
from models.joueur import Joueur
from questionary import select, checkbox
from colorama import Fore, Back, Style


def start_match(matchs: list):

    if not isinstance(matchs, list):
        print("Error, argument is not a match list")
        return

    print("Match started...")

    print(matchs)

    while len(matchs) > 0:

        match_play = matchs.pop(0)

        print("match play :", match_play)
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
            # match_play.joueur1.score_jouer1 += 1
            # PORUIQE NO RECONOCE  LOS ATRIBUTOS DE LA CLASE JUGADOR
            # print(f"Score actuel : {match_play.joueur1.score_jouer1}")
            match_play.joueur1.gagner_match()
        # PORQUE NO SUGIERE LOS METDOS DE LA CLASE JUGADOR
        if response == match_play.joueur2.nom:
            match_play.joueur2.gagner_match()
        if (
            response
            == f"Egalité : {match_play.joueur1.nom} et {match_play.joueur2.nom}"
        ):

            match_play.joueur1.egalite_match()
            match_play.joueur2.egalite_match()
        print(Back.GREEN + " --- Match suivant... --- ")

    print(Back.CYAN + "--- Tous les matchs ont été joués --- ")
    return
