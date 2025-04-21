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
                f"{Back.BLACK + Fore.WHITE} -♛ -{joueur.nom} {joueur.prenom} : {joueur.id_national} ♚- \n"
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
