from colorama import Fore, Back, init, Style
from models.joueur import Joueur
from models.tour import Tour
from typing import List
import datetime

init(autoreset=True)


class Tournoi:

    def __init__(
        self,
        nom_tournoi="",
        location="",
        date_debut=None,
        date_fin=None,
        description="",
        # numero minimo de tour
        nombre_tour=4,
        liste_joueur: List[Joueur] = [],
        liste_tour: List[Tour] = [],
    ) -> None:
        self.nom_tournoi = nom_tournoi
        self.location = location
        self.date_debut = date_debut if date_debut else self.get_time()
        self.date_fin = date_fin
        self.nombre_tour = nombre_tour
        self.liste_joueur = liste_joueur
        self.liste_tour = liste_tour
        self.description = description

    def __str__(self):
        return (
            "\n"
            "\n"
            f"{Fore.CYAN} ---  Le Tournois {self.nom_tournoi}\n"
            f"{Fore.CYAN} ---  Adrresse : {self.location}\n"
            f"{Fore.CYAN} ---  Date debout {self.date_debut}\n"
            f"{Fore.CYAN} ---  Description {self.description}\n"
            f"{Fore.CYAN} ---  Liste de Tour {self.nombre_tour}\n"
        )

    def voir_histoiral_match(self):
        print(Back.CYAN + Fore.BLACK + "HISTORIAL DES MATCHS :" + Style.RESET_ALL)
        for match in self.historial_match:
            print(Back.BLUE + match, "\n")

    def generate_tour(self):

        numero_tour = len(self.liste_tour) + 1

        nouveau_tour = Tour(tournoi=self, number_tour=numero_tour)

        self.liste_tour.append(nouveau_tour)

    def voir_classement(self):
        print(Fore.CYAN + " --- Classement : --- ")
        print("\n")

        order_joueur = sorted(
            self.liste_joueur, key=lambda joueur: joueur.score_tournoi, reverse=True
        )

        for joueur in order_joueur:
            print(
                f"{Back.BLACK + Fore.WHITE} -♛ -{joueur.nom} {joueur.prenom} : {joueur.id_national} ♚- {Style.RESET_ALL}\n"
                f"{Fore.GREEN} Score Total-Tournoi :{Style.RESET_ALL} {joueur.score_tournoi}\n"
            )

    def get_all_tours(self):
        """Recuper tous les tours"""
        return self.liste_tour

    def get_time(self):
        return datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    def to_dict(self):
        return {
            "nom_tournoi": self.nom_tournoi,
            "location": self.location,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "description": self.description,
            "nombre_tour": self.nombre_tour,
            "liste_joueur": [joueur.to_dict_for_list() for joueur in self.liste_joueur],
            "liste_tour": [tour.to_dict() for tour in self.liste_tour],
        }

    @classmethod
    def from_dict(cls, data: dict):
        # Asegúrate de que todos los campos necesarios están presentes
        return cls(
            nom_tournoi=data.get("nom_tournoi", ""),
            location=data.get("location", ""),
            date_debut=data.get("date_debut"),
            date_fin=data.get("date_fin"),
            description=data.get("description", ""),
            nombre_tour=data.get("nombre_tour", 4),
            liste_joueur=[
                Joueur.to_dict_for_tournois(joueur_data)
                for joueur_data in data.get("liste_joueur", [])
            ],
            liste_tour=[
                Tour.from_dict(tour_data) for tour_data in data.get("liste_tour", [])
            ],
        )

    # def init_joueurs_tournoi(self) -> list:
    #     raise NotImplementedError
    #     return []

    # def init_tours(self, liste_joueur: list) -> list:

    #     joueurs_copy = liste_joueur[:]
    #     random.shuffle(joueurs_copy)
    #     print("Tour Generé : ", "\n")

    #     liste_paire = []
    #     nombre_match = 0
    #     liste_match = []

    #     while len(joueurs_copy) >= 2:
    #         joueur1 = joueurs_copy.pop(0)
    #         joueur2 = joueurs_copy.pop(0)
    #         nombre_match += 1

    #         new_match = Match(
    #             nombre_match=nombre_match,
    #             joueur1=joueur1,
    #             joueur2=joueur2,
    #             score_jouer1=0,
    #             score_jouer2=0,
    #         )

    #         print(
    #             f"{Back.BLUE + Fore.BLACK}♜  {joueur1.nom + ' - ID :' + joueur1.id_national} ♜  {Style.RESET_ALL}  VS  {Back.BLUE + Fore.BLACK}♜  {joueur2.nom + ' - ID :' + joueur2.id_national} ♜ {Style.RESET_ALL} \n "
    #         )

    #         paire_joueur = [joueur1, joueur2]
    #         liste_paire.append(paire_joueur)
    #         liste_match.append(new_match)

    #         joueur1.save_joueur_match(joueur2.id_national)
    #         joueur2.save_joueur_match(joueur1.id_national)

    #     self.nombre_tour = len(liste_paire)
    #     self.liste_joueur = liste_joueur
    #     self.liste_match = liste_match

    #     # for match in list_match:
    #     #     print("Liste de match creados :", match)

    #     # print("liste paire", liste_paire)
    #     return liste_match

    # def save_historial_match(self, match):
    #     self.historial_match.append(match)

    # def load_historial_match(self, match):
