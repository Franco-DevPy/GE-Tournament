from colorama import Fore, Back, Style
from models.joueur import Joueur
from questionary import select, checkbox
import random
from controllers.data_load_player import load_data_file_players


class Match:

    def __init__(
        self, nombre_match, joueur1: Joueur, joueur2: Joueur, score_jouer1, score_jouer2
    ):
        self.nombre_match = nombre_match
        self.joueur1: Joueur = joueur1
        self.joueur2: Joueur = joueur2

    def __str__(self):
        return (
            # f" Match Nro : {self.nombre_match} \n "
            f"{Back.CYAN + Fore.BLACK}♜  {self.joueur1.nom + 'ID :' + self.joueur1.id_national} ♜  {Style.RESET_ALL}  VS  {Back.CYAN + Fore.BLACK}♜  {self.joueur2.nom + 'ID :' + self.joueur2.id_national} ♜ {Style.RESET_ALL} \n "
        )

    def definir_resultat(self, resultat):
        """Definir le résultat du match"""
        if resultat == "joueur1":
            self.joueur1.gagner_match()
            self.joueur2.perdre_match()
        elif resultat == "joueur2":
            self.joueur2.gagner_match()
            self.joueur1.perdre_match()
        else:  # Egalité
            self.joueur1.egalite_match()
            self.joueur2.egalite_match()

    def match_suivant(self):
        self.nombre_match += 1

    def create_match(self):
        print(f"Le Joueur {self.joueur1} VS {self.joueur2}")

    def delete_match(self):
        print(f"Le match {self.nombre_match} a été eliminé")

    def gagner_match(self):
        pass

    def perdre_match(self):
        pass

    def voir_histoiral_match(self):
        print(Back.CYAN + Fore.BLACK + "HISTORIAL DES MATCHS :" + Style.RESET_ALL)
        for match in self.historial_match:
            print(Back.BLUE + match, "\n")

    def to_dict(self):
        return {
            "nombre_match": self.nombre_match,
            "joueur1": self.joueur1.to_dict_for_tournois(),
            "joueur2": self.joueur2.to_dict_for_tournois(),
        }

    # @classmethod
    # def from_dict(cls, data: dict):
    #     return cls(
    #         nombre_match=data["nombre_match"],
    #         joueur1=Joueur.from_dict_for_tournois(data["joueur1"]),
    #         joueur2=Joueur.from_dict_for_tournois(data["joueur2"]),
    #     )
    @classmethod
    def from_dict(cls, data: dict):
        joueurs_complets = load_data_file_players()
        joueurs_dict = {joueur.id_national: joueur for joueur in joueurs_complets}

        return cls(
            nombre_match=data["nombre_match"],
            joueur1=joueurs_dict[data["joueur1"]["id_national"]],
            joueur2=joueurs_dict[data["joueur2"]["id_national"]],
            score_jouer1=data.get("score_jouer1", 0),
            score_jouer2=data.get("score_jouer2", 0),
        )
