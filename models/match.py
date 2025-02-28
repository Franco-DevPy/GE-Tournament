from colorama import Fore, Back, Style
from models.joueur import Joueur


class Match:

    def __init__(
        self, nombre_match, joueur1: Joueur, joueur2: Joueur, score_jouer1, score_jouer2
    ):
        self.nombre_match = nombre_match
        self.joueur1: Joueur = joueur1
        self.joueur2: Joueur = joueur2

    def __str__(self):
        return f"{Back.CYAN + Fore.BLACK}♜  {self.joueur1.nom + 'ID :' + self.joueur1.id_national} ♜  {Style.RESET_ALL}  VS  {Back.CYAN + Fore.BLACK}♜  {self.joueur2.nom + 'ID :' + self.joueur2.id_national} ♜ {Style.RESET_ALL} \n "

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

    @classmethod
    def from_dict(cls, data: dict, players_dict: dict[str, Joueur]):
        joueur1 = players_dict[data["joueur1"]["id_national"]]
        joueur2 = players_dict[data["joueur2"]["id_national"]]
        joueur1.score_tournoi = data["joueur1"].get("score_tournoi", 0)
        joueur2.score_tournoi = data["joueur2"].get("score_tournoi", 0)
        return cls(
            nombre_match=data.get("nombre_match"),
            joueur1=joueur1,
            joueur2=joueur2,
            score_jouer1=joueur1.score_tournoi,
            score_jouer2=joueur2.score_tournoi,
        )
