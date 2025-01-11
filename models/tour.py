from colorama import Back, Fore, Style, init
import random
from models.match import Match


# necesito llamar la clase jugador para moder manipular los jugadores?
# from models.joueur import Joueur


class Tour:

    def __init__(self, joueurs_selectionnes, nom_tour, tournoi=None):
        self.nom_tour = nom_tour
        self.liste_joueur = joueurs_selectionnes
        self.liste_match = []
        self.tournoi = tournoi
        if nom_tour == 1:
            self.generate_matches_first_tour(joueurs_selectionnes)
        else:
            self.generate_matches(joueurs_selectionnes)

    def generate_matches_first_tour(self, joueurs_selectionnes) -> list:
        print(Back.BLUE + " -- Génération des MATCH NRO 1   --")
        # print("jugadores seleccionados : ", joueurs_selectionnes)
        random.shuffle(joueurs_selectionnes)
        new_liste_match = []
        self.nom_tour += 1
        nombre_match = 1

        for paire_joueur in range(0, len(joueurs_selectionnes), 2):

            joueur1 = joueurs_selectionnes[paire_joueur]
            joueur2 = joueurs_selectionnes[paire_joueur + 1]

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

        # print("new_liste_match : ", len(new_liste_match))

        # print(
        #     "Liste des matchs générés : ",
        #     [
        #         f"{match.joueur1.nom} vs {match.joueur2.nom}"
        #         for match in self.liste_match
        #     ],
        # )
        return self.liste_match

    def generate_matches(self, joueurs_selectionnes) -> list:
        print(Back.BLUE + "Génération des matchs pour le tour suivant")
        print(joueurs_selectionnes)

    def to_dict(self):
        return {
            "nom_tour": self.nom_tour,
            "liste_joueur": [joueur.to_dict() for joueur in self.liste_joueur],
            "liste_match": [match.to_dict() for match in self.liste_match],
        }

    #     print(" new tour : ", vars(new_tournoi))

    #     joueurs_selectionnes = new_tournoi.liste_match

    #     if not isinstance(joueurs_selectionnes, list):
    #         print(Back.RED + "  NO ES UNA LISTA DE JUGADORES  ")

    #     if len(joueurs_selectionnes) < 1:
    #         print(Back.RED + " La lista de jugadores esta vacia  ")

    #     while len(joueurs_selectionnes) > 0:
    #         random.shuffle(joueurs_selectionnes)
    #         joueur1 = joueurs_selectionnes.pop(0)
    #         joueur2 = joueurs_selectionnes.pop(0)

    #         if (joueur1.matches_joues.count(joueur2.id_national) == 0) and (
    #             joueur2.matches_joues.count(joueur1.id_national) == 0
    #         ):
    #             new_match = Match(joueur1, joueur2)
    #             joueur1.save_joueur_match(joueur2.id_national)
    #             joueur2.save_joueur_match(joueur1.id_national)
    #             self.liste_match.append(new_match)
    #         else:
    #             print(
    #                 f"{Back.RED}Les joueurs {joueur1.nom} et {joueur2.nom} ont déjà joué ensemble{Back.RESET}"
    #             )
    #             print("On recommence le tirage")
    #             joueurs_selectionnes.append(joueur1)
    #             joueurs_selectionnes.append(joueur2)

    #     return self.liste_match

    # Logique de génération des paires
    # Tour 3:
    #     - A/B
    #     - C/D
    # Résultats après tour 3:
    #     - A: 10 pts
    #     - B: 9 pts
    #     - C: 4 pts
    #     - D: 3 pts
