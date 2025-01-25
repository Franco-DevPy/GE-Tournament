from colorama import Back, Fore, Style, init
import random
from models.match import Match


# necesito llamar la clase jugador para moder manipular los jugadores?
# from models.joueur import Joueur


class Tour:

    def __init__(self, nom_tour, tournoi=None):
        self.number_tour = nom_tour
        self.liste_joueur = tournoi.liste_joueur
        self.liste_match = []
        self.tournoi = tournoi
        if nom_tour == 1:
            self.generate_matches_first_tour()
        else:
            self.generate_matches()

    def generate_matches_first_tour(self) -> list:
        print(
            Back.BLUE
            + " -- Génération du TOUR Nro 1 (generate_matches_first_tour)   --\n"
        )
        # print("jugadores seleccionados : ", joueurs_selectionnes)
        random.shuffle(self.liste_joueur)
        new_liste_match = []
        self.number_tour += 1
        nombre_match = 1

        nouveau_tour = self

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

        self.liste_match.extend(new_liste_match)

        return self.liste_match

    def generate_matches(self) -> list:
        print(
            Back.BLUE
            + f" -- Génération du Tour (generate_matches) {self.number_tour} --"
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
                f"{Back.BLUE + Fore.BLACK}♜  {joueur1.nom} VS {joueur2.nom} ♜ {Style.RESET_ALL}"
            )
            nombre_match += 1

        self.liste_match.extend(new_liste_match)
        return self.liste_match

    def to_dict(self):
        return {
            "nom_tour": self.number_tour,
            "liste_joueur": [joueur.to_dict() for joueur in self.liste_joueur],
            "liste_match": [match.to_dict() for match in self.liste_match],
        }
