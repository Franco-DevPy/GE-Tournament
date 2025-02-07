from colorama import Back, Fore, Style, init
import random
from typing import List
from models.match import Match
from models.joueur import Joueur


# necesito llamar la clase jugador para moder manipular los jugadores?
# from models.joueur import Joueur


class Tour:

    def __init__(self, number_tour, tournoi=None):
        self.number_tour = number_tour
        self.liste_joueur: List[Joueur] = tournoi.liste_joueur
        self.liste_match: List[Match] = []
        self.tournoi = tournoi
        if number_tour == 1:
            self.generate_matches_first_tour()
        else:
            self.generate_matches_hazard()

    def generate_matches_first_tour(self) -> list:

        random.shuffle(self.liste_joueur)
        new_liste_match = []
        nombre_match = 1

        for paire_joueur in range(0, len(self.liste_joueur), 2):

            joueur1 = self.liste_joueur[paire_joueur]
            joueur2 = self.liste_joueur[paire_joueur + 1]

            new_match = Match(
                nombre_match=nombre_match,
                joueur1=joueur1,
                joueur2=joueur2,
                score_jouer1=0,
                score_jouer2=0,
            )

            if joueur2.id_national not in joueur1.jouers_rencontres:
                joueur1.jouers_rencontres[joueur2.id_national] = []
            if joueur1.id_national not in joueur2.jouers_rencontres:
                joueur2.jouers_rencontres[joueur1.id_national] = []

            joueur1.jouers_rencontres[joueur2.id_national].append(self.number_tour)
            joueur2.jouers_rencontres[joueur1.id_national].append(self.number_tour)

            new_liste_match.append(new_match)
            print(
                f"{Back.BLUE + Fore.BLACK}♜  {joueur1.nom + ' - ID :' + joueur1.id_national} ♜  {Style.RESET_ALL}  VS  {Back.BLUE + Fore.BLACK}♜  {joueur2.nom + ' - ID :' + joueur2.id_national} ♜ {Style.RESET_ALL} \n "
            )
            nombre_match += 1

        self.liste_match.extend(new_liste_match)

        return self.liste_match

    def generate_matches(self) -> list:
        print(
            Back.BLUE + f" -- Génération  Tour (generate_matches) {self.number_tour} --"
        )
        new_liste_match = []
        nombre_match = 1

        # Aquí se emparejan los jugadores según los resultados de los matchs previos
        for paire_joueur in range(0, len(self.liste_joueur), 2):
            joueur1 = self.liste_joueur[paire_joueur]
            joueur2 = self.liste_joueur[paire_joueur + 1]

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
            nombre_match += 1

        self.liste_match.extend(new_liste_match)
        return self.liste_match

    def generate_matches_hazard(self) -> list:
        print(
            Back.BLUE
            + f" -- Génération HAZARD Tour (generate_matches) {self.number_tour} --"
        )
        new_liste_match = []
        nombre_match = 1

        self.liste_joueur.sort(key=lambda x: x.match_gagne, reverse=True)

        copy_liste_joueur: List[Joueur] = self.liste_joueur[:]

        while copy_liste_joueur:
            joueur1 = copy_liste_joueur.pop(0)
            for i, joueur2 in enumerate(copy_liste_joueur):
                if joueur2.id_national not in joueur1.jouers_rencontres:
                    copy_liste_joueur.pop(i)

                    new_match = Match(
                        nombre_match=nombre_match,
                        joueur1=joueur1,
                        joueur2=joueur2,
                        score_jouer1=0,
                        score_jouer2=0,
                    )

                    if joueur2.id_national not in joueur1.jouers_rencontres:
                        joueur1.jouers_rencontres[joueur2.id_national] = []
                    if joueur1.id_national not in joueur2.jouers_rencontres:
                        joueur2.jouers_rencontres[joueur1.id_national] = []

                    joueur1.jouers_rencontres[joueur2.id_national].append(
                        self.number_tour
                    )
                    joueur2.jouers_rencontres[joueur1.id_national].append(
                        self.number_tour
                    )

                    new_liste_match.append(new_match)
                    print(
                        f"{Back.BLUE + Fore.BLACK}♜  {joueur1.nom} vs {joueur2.nom} ♜ {Style.RESET_ALL}"
                    )
                    nombre_match += 1
                    break

        self.liste_match.extend(new_liste_match)
        return self.liste_match

    def to_dict(self):
        return {
            "nom_tour": self.number_tour,
            "liste_joueur": [joueur.to_dict() for joueur in self.liste_joueur],
            "liste_match": [match.to_dict() for match in self.liste_match],
        }
