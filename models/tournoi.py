import random
from colorama import Fore, Back, init, Style
from models.match import Match
from models.joueur import Joueur
from models.tour import Tour
from typing import List
from controllers.data_load_player import load_data_file_players

init(autoreset=True)


class Tournoi:

    def __init__(
        self,
        nom_tournoi="",
        location="",
        date_debut=0,
        date_fin=None,
        description="",
        # numero minimo de tour
        nombre_tour=4,
        liste_joueur: List[Joueur] = [],
        liste_tour: List[Tour] = [],
        finit=False,
    ) -> None:
        self.nom_tournoi = nom_tournoi
        self.location = location
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tour = nombre_tour
        self.liste_joueur = liste_joueur
        self.liste_tour = liste_tour
        self.description = description
        self.finit = finit

    def __str__(self):
        return (
            f"Le Tournois {self.nom_tournoi}\n"
            f"Adrresse : {self.location}\n"
            f"Date debout {self.date_debut}\n"
            f"Description {self.description}\n"
            f"Liste de Tour {self.nombre_tour}\n"
            f"Joueurs qui participent : {[joueur.nom for joueur in self.liste_joueur]}"  # Mostrar solo los nombres de los jugadores
        )

    def voir_histoiral_match(self):
        print(Back.CYAN + Fore.BLACK + "HISTORIAL DES MATCHS :" + Style.RESET_ALL)
        for match in self.historial_match:
            print(Back.BLUE + match, "\n")

    def generate_tour(self):

        numero_tour = len(self.liste_tour) + 1

        ## ACA DEBEMOS GENERAR TOUR Y NUMERO DE TOUR, DEFINIRLOS, PARA QUE EL WHILE FUNCIONE nombre_tour_actuel < new_tournoi.nombre_tour:

        # print(
        #     Fore.GREEN
        #     + f" -- Création du Tour #{numero_tour} pour le tournoi {self.nom_tournoi} --"
        # )

        nouveau_tour = Tour(tournoi=self, number_tour=numero_tour)

        self.liste_tour.append(nouveau_tour)

    def voir_classement(self):

        print(" -- Classement -- ")

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
            "finit": self.finit,
        }

    @classmethod
    def from_dict(cls, data):
        # Cargar los datos completos de los jugadores
        joueurs_complets = load_data_file_players()
        joueurs_dict = {joueur.id_national: joueur for joueur in joueurs_complets}

        print("joueurs_dict", joueurs_dict)

        # Imprimir el contenido de 'data' para depuración
        print(Back.BLUE + "data", data)
        # Verificar si 'liste_joueur' existe en los datos
        if "liste_joueur" not in data:
            raise KeyError(
                "La clé 'liste_joueur' est manquante dans les données du tournoi."
            )
        # Buscar los jugadores completos usando su id_national

        liste_joueur = [
            joueurs_dict[joueur["id_national"]] for joueur in data["liste_joueur"]
        ]

        return cls(
            nom_tournoi=data["nom_tournoi"],
            location=data["location"],
            date_debut=data["date_debut"],
            date_fin=data["date_fin"],
            description=data["description"],
            nombre_tour=data["nombre_tour"],
            liste_joueur=liste_joueur,
            liste_tour=[Tour.from_dict(tour) for tour in data["liste_tour"]],
            finit=data["finit"],
        )

    # def from_dict(cls, data):
    #     return cls(
    #         nom_tournoi=data["nom_tournoi"],
    #         location=data["location"],
    #         date_debut=data["date_debut"],
    #         date_fin=data["date_fin"],
    #         description=data["description"],
    #         nombre_tour=data["nombre_tour"],
    #         # liste_joueur=[Joueur.from_dict(joueur) for joueur in data["liste_joueur"]],
    #         liste_tour=[Tour.from_dict(tour) for tour in data["liste_tour"]],
    #         finit=data["finit"],
    #     )

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
