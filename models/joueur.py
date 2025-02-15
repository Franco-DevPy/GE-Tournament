import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


class Joueur:

    def __init__(
        self,
        nom,
        prenom,
        date_naissance,
        id_national,
        match_gagne=0,
        match_perdu=0,
        matches_nulls=0,
        score_tournoi=0,
        joueurs_rencontres=None,
    ) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.id_national = id_national
        self.match_gagne = match_gagne
        self.match_perdu = match_perdu
        self.matches_nulls = matches_nulls
        self.score_tournoi = score_tournoi
        self.jouers_rencontres = joueurs_rencontres or {}

    def __str__(self):
        return (
            f"{Back.BLACK + Fore.WHITE} - ♛ -{self.nom} {self.prenom}- ♚ -  {Style.RESET_ALL}\n"
            f"{Fore.GREEN}Id national :{Style.RESET_ALL} {self.id_national}\n"
            f"{Fore.GREEN}Match gagné :{Style.RESET_ALL} {self.match_gagne}\n"
            f"{Fore.GREEN}Match perdu :{Style.RESET_ALL} {self.match_perdu}\n"
            f"{Fore.GREEN}Match nul :{Style.RESET_ALL} {self.matches_nulls}\n"
        )

    def __repr__(self):
        return f"Joueur({self.nom}, {self.prenom}, ID: {self.id_national}), Score Total: {self.score_tournoi}, "

    # RECUPERAR EL ID PARA LUEGO JUNTARLO CON TODA LA DATA DEL JUGADORs
    def get_joueur_by_id(self, id_national):
        pass

    def gagner_match(self):
        self.match_gagne += 1
        self.score_tournoi += 1

    def egalite_match(self):
        self.match_gagne += 0
        self.score_tournoi += 0.5

    def save_joueur_match(self, joueur_id):
        self.matches_joues.append(joueur_id)

    def reset_joueur_match(self):
        self.matches_joues = []
        self.score_tournoi = 0

    def perdre_match(self):
        self.match_perdu += 1
        self.score_tournoi += 0

    def voir_score(self):
        print("Score du joueur : ", self.score_tournoi)
        pass

    def ajouter_joueur_rencontre(self, joueur_id, tour):
        if joueur_id not in self.jouers_rencontres:
            self.jouers_rencontres[joueur_id] = []
        self.jouers_rencontres[joueur_id].append(tour)

    def to_dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "id_national": self.id_national,
            "match_gagne": self.match_gagne,
            "match_perdu": self.match_perdu,
            "score_tournoi": self.score_tournoi,
        }

    def to_dict_for_tournois(self):
        return {
            "id_national": self.id_national,
            "score_tournoi": self.score_tournoi,
        }

    def to_dict_for_list(self):
        return {
            "id_national": self.id_national,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nom=data["nom"],
            prenom=data["prenom"],
            date_naissance=data.get("date_naissance", ""),
            id_national=data["id_national"],
            match_gagne=data.get("match_gagne", 0),
            match_perdu=data.get("match_perdu", 0),
            score_tournoi=data.get("score_tournoi", 0),
        )

    @classmethod
    def from_dict_for_tournois(cls, data):
        return cls(
            id_national=data["id_national"],
            score_tournoi=data.get("score_tournoi", 0),
        )


joueurs_list = [
    Joueur("toto", "tutu", "18/12/03", "AU12345"),
    Joueur("toto", "tutu", "18/12/03", "AU12346"),
    Joueur("toto", "tutu", "18/12/03", "AU12347"),
]
id = "AU12346"


def search_joueur_in_list(joueurs, id):
    for joueur in joueurs:
        if joueur.id_national == id:
            return joueur


joueurs_dict = {
    "AU12345": Joueur("toto", "tutu", "18/12/03", "AU12345"),
    "AU12346": Joueur("toto", "tutu", "18/12/03", "AU12346"),
    "AU12347": Joueur("toto", "tutu", "18/12/03", "AU12347"),
}


def searche_joueur_dict(joueurs, id):
    return joueurs[id]


json_list = JSON.parse()

joueur_dict = {}

for json_joueur in json_list:
    joueur = Joueur.from_dict(json_joueur)
    joueur_dict[joueur.id_national] = joueur
