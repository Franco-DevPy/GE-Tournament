from colorama import Back, Fore, Style
import random
from typing import List
from models.match import Match
from models.joueur import Joueur


class Tour:

    def __init__(
        self, number_tour, liste_match=None, tournoi=None, generate_matches=True
    ):
        self.number_tour = number_tour
        self.liste_match = liste_match if liste_match is not None else []
        self.liste_joueur = tournoi.liste_joueur if tournoi else []
        self.tournoi = tournoi
        if generate_matches:
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
                f"{Back.BLUE + Fore.BLACK}♜  {joueur1.nom} - ID : {joueur1.id_national} ♜ "
                f"{Style.RESET_ALL}  VS  "
                f"{Back.BLUE + Fore.BLACK}♜  {joueur2.nom} - ID : {joueur2.id_national} ♜ "
                f"{Style.RESET_ALL} \n"
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

        jugadores_emparejados = []

        while copy_liste_joueur:
            joueur1 = copy_liste_joueur.pop(0)

            if joueur1.id_national in jugadores_emparejados:
                continue

            adversaire = self.trouver_adversaire(joueur1, copy_liste_joueur)

            if adversaire is None:
                print(f"No se encontró oponente adecuado para {joueur1.nom}")
                continue

            jugadores_emparejados.append(joueur1.id_national)
            jugadores_emparejados.append(adversaire.id_national)

            new_match = Match(
                nombre_match=nombre_match,
                joueur1=joueur1,
                joueur2=adversaire,
                score_jouer1=0,
                score_jouer2=0,
            )

            if adversaire.id_national not in joueur1.jouers_rencontres:
                joueur1.jouers_rencontres[adversaire.id_national] = []
            if joueur1.id_national not in adversaire.jouers_rencontres:
                adversaire.jouers_rencontres[joueur1.id_national] = []

            joueur1.jouers_rencontres[adversaire.id_national].append(self.number_tour)
            adversaire.jouers_rencontres[joueur1.id_national].append(self.number_tour)

            new_liste_match.append(new_match)

            print(
                f"{Back.BLUE + Fore.BLACK}♜  {joueur1.nom} vs {adversaire.nom} ♜ {Style.RESET_ALL}"
            )
            nombre_match += 1

        self.liste_match.extend(new_liste_match)
        return self.liste_match

    def trouver_adversaire(
        self, joueur1: Joueur, lista_jugadores: List[Joueur]
    ) -> Joueur:
        adversaire = None
        min_fois_jouer = float("inf")

        for joueur2 in lista_jugadores:
            if joueur1.id_national == joueur2.id_national:
                continue

            if not self.deja_recontre(joueur1, joueur2):
                return joueur2

            fois_jouer_deja = self.combien_fois_joue(joueur1, joueur2)

            if fois_jouer_deja < min_fois_jouer:
                adversaire = joueur2
                min_fois_jouer = fois_jouer_deja

        return adversaire

    def deja_recontre(self, joueur1: Joueur, joueur2: Joueur) -> bool:

        for match in self.liste_match:
            if (
                match.joueur1.id_national == joueur1.id_national
                and match.joueur2.id_national == joueur2.id_national
            ) or (
                match.joueur1.id_national == joueur2.id_national
                and match.joueur2.id_national == joueur1.id_national
            ):
                return True

        return False

    def combien_fois_joue(self, joueur1: Joueur, joueur2: Joueur) -> int:
        quantite = 0

        for match in self.liste_match:
            if (
                match.joueur1.id_national == joueur1.id_national
                and match.joueur2.id_national == joueur2.id_national
            ) or (
                match.joueur1.id_national == joueur2.id_national
                and match.joueur2.id_national == joueur1.id_national
            ):
                quantite += 1

        return quantite

    def to_dict(self):
        return {
            "nom_tour": self.number_tour,
            "liste_match": [match.to_dict() for match in self.liste_match],
        }

    @classmethod
    def from_dict(
        cls, data: dict, players_dict: dict[str, Joueur], generate_matches=True
    ):
        return cls(
            number_tour=data.get("nom_tour"),
            liste_match=[
                Match.from_dict(match_data, players_dict)
                for match_data in data.get("liste_match", [])
            ],
            generate_matches=generate_matches,
        )
