import random
from colorama import Fore, Back, init, Style
from models.match import Match

init(autoreset=True)


class Tournoi:

    def __init__(
        self,
        nom_tournoi="",
        location="",
        date_debut=0,
        date_fin=None,
        description="",
        nombre_tour_actuel=0,
        nombre_tour=0,
        liste_joueur=[],
        liste_paires=[],
    ) -> None:
        self.nom_tournoi = nom_tournoi
        self.location = location
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tour = nombre_tour
        self.nombre_tour_actuel = nombre_tour_actuel
        self.liste_joueur = liste_joueur
        self.liste_paires = liste_paires
        self.description = description

    def __str__(self):
        return (
            f"Le Tournois {self.nom_tournoi}\n"
            f"Adrresse : {self.location}\n"
            f"Date debout {self.date_debut}\n"
            f"Description {self.description}\n"
            f"Liste de Tour {self.nombre_tour}\n"
            f"Joueurs qui participent : {[joueur.nom for joueur in self.liste_joueur]}"  # Mostrar solo los nombres de los jugadores
        )

    # def init_joueurs_tournoi(self) -> list:
    #     raise NotImplementedError
    #     return []

    def init_tours(self, liste_joueur: list) -> list:

        joueurs_copy = liste_joueur[:]
        random.shuffle(joueurs_copy)
        print("Tour Generé : ", "\n")

        liste_paire = []
        nombre_match = 0
        list_match = []

        while len(joueurs_copy) >= 2:
            joueur1 = joueurs_copy.pop(0)
            joueur2 = joueurs_copy.pop(0)
            nombre_match += 1

            new_match = Match(
                nombre_match=nombre_match,
                joueur1=joueur1,
                joueur2=joueur2,
                score_jouer1=0,
                score_jouer2=0,
            )

            print(
                f"{Back.BLUE + Fore.BLACK}♜  {joueur1.nom + 'ID :' + joueur1.id_national} ♜  {Style.RESET_ALL}  VS  {Back.BLUE + Fore.BLACK}♜  {joueur2.nom + 'ID :' + joueur2.id_national} ♜ {Style.RESET_ALL} \n "
            )

            paire_joueur = [joueur1, joueur2]
            liste_paire.append(paire_joueur)
            list_match.append(new_match)

        self.nombre_tour = len(liste_paire)
        self.liste_joueur = liste_joueur
        self.liste_paires = liste_paire

        for match in list_match:
            print("Liste de match creados :", match)

        # print("liste paire", liste_paire)
        return liste_paire
