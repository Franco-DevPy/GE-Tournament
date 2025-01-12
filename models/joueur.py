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
        match_total=0,
        matches_joues=[],
    ) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.id_national = id_national
        self.match_gagne = match_gagne
        self.match_perdu = match_perdu
        self.match_total = match_total

    def __str__(self):
        return (
            f"{Back.BLACK + Fore.WHITE} - ♛ -{self.nom} {self.prenom}- ♚ -  {Style.RESET_ALL}\n"
            f"{Fore.GREEN}Id national :{Style.RESET_ALL} {self.id_national}\n"
            f"{Fore.GREEN}Match gagné :{Style.RESET_ALL} {self.match_gagne}\n"
            f"{Fore.GREEN}Match perdu :{Style.RESET_ALL} {self.match_perdu}\n"
            f"{Fore.GREEN}Total match joué :{Style.RESET_ALL} {self.match_total}"
        )

    def __repr__(self):
        return f"Joueur({self.nom}, {self.prenom}, ID: {self.id_national})"

    def gagner_match(self):
        self.match_gagne += 1
        self.match_total += 1
        print(
            f"{Back.GREEN}-- Le joueur {self.nom} a gagné le match --{Style.RESET_ALL}"
        )

    def egalite_match(self):
        self.match_gagne += 1
        self.match_total += 1
        print(f"{Back.BLUE}-- Le match est nul -- {Style.RESET_ALL}")

    def save_joueur_match(self, joueur_id):
        self.matches_joues.append(joueur_id)
        print(f"{Back.GREEN} Le match a été sauvegardé{Style.RESET_ALL}")

    def reset_joueur_match(self):
        self.matches_joues = []
        print(f"{Back.GREEN} Les matchs ont été réinitialisés{Style.RESET_ALL}")

    def perdre_match(self):
        self.match_perdu += 1
        self.match_total += 1
        print(
            f"{Back.BLUE}--  Le joueur {self.nom} a perdu le match -- {Style.RESET_ALL}"
        )

    def to_dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "id_national": self.id_national,
            "match_gagne": self.match_gagne,
            "match_perdu": self.match_perdu,
            "match_total": self.match_total,
        }

    # ENTENDER ESTO
    @classmethod
    def from_dict(cls, data):
        return cls(
            nom=data["nom"],
            prenom=data["prenom"],
            date_naissance=data.get("date_naissance", ""),
            id_national=data["id_national"],
            match_gagne=data.get("match_gagne", 0),
            match_perdu=data.get("match_perdu", 0),
            match_total=data.get("match_total", 0),
        )
