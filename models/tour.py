from colorama import Back
import random
from models.match import Match
from models.tournoi import *


# necesito llamar la clase jugador para moder manipular los jugadores?
# from models.joueur import Joueur


class Tour:

    def __init__(self, tournoi: Tournoi, nom_tour=1):
        self.nom = "Round " + str(nom_tour)
        # # self.date_heure_debout = date_heure_debout  # op
        # self.date_heure_fin = date_heure_fin  # op
        self.liste_match = []
        self.tournoi: Tournoi = tournoi
        if nom_tour == 1:
            self.generate_matches_first_tour(tournoi)
        else:
            self.generate_matches(tournoi)

    def generate_matches_first_tour(self, new_tournois: Tournoi) -> list:
        print("Génération des matchs pour le premier tour")
        joueurs_selectionnes = new_tournois.liste_joueur
        random.shuffle(joueurs_selectionnes)
        new_liste_match = []
        while len(joueurs_selectionnes) > 0:
            joueur1 = joueurs_selectionnes.pop(0)
            joueur2 = joueurs_selectionnes.pop(0)
            nombre_match = 1

            new_match = Match(
                nombre_match=nombre_match,
                joueur1=joueur1,
                joueur2=joueur2,
                score_jouer1=0,
                score_jouer2=0,
            )

            new_liste_match.append(new_match)
            print(
                f"{Back.BLUE + Fore.BLACK}♜  {joueur1.nom + ' - ID :' + joueur1.id_national} ♜  {Style.RESET_ALL}  VS  {Back.BLUE + Fore.BLACK}♜  {joueur2.nom + ' - ID :' + joueur2.id_national} ♜ {Style.RESET_ALL} \n "
            )

        self.liste_match.extend(new_liste_match)

        return new_match

    def generate_matches(self, new_tournois: Tournoi):

        nom_tour += 1

        joueurs_selectionnes = new_tournois.liste_joueur

        # liste_match = new_tournois.init_tours(joueurs_selectionnes)

        while len(joueurs_selectionnes) > 0:
            random.shuffle(joueurs_selectionnes)
            joueur1 = joueurs_selectionnes.pop(0)
            joueur2 = joueurs_selectionnes.pop(0)

            if (joueur1.matches_joues.count(joueur2.id_national) == 0) and (
                joueur2.matches_joues.count(joueur1.id_national) == 0
            ):
                new_match = Match(joueur1, joueur2)
                joueur1.save_joueur_match(joueur2.id_national)
                joueur2.save_joueur_match(joueur1.id_national)
                self.liste_match.append(new_match)
            else:
                print(
                    f"{Back.RED}Les joueurs {joueur1.nom} et {joueur2.nom} ont déjà joué ensemble{Back.RESET}"
                )
                print("On recommence le tirage")
                joueurs_selectionnes.append(joueur1)
                joueurs_selectionnes.append(joueur2)

        return self.liste_match

        # Logique de génération des paires
        # Tour 3:
        #     - A/B
        #     - C/D
        # Résultats après tour 3:
        #     - A: 10 pts
        #     - B: 9 pts
        #     - C: 4 pts
        #     - D: 3 pts
