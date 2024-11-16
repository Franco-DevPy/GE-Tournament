class Joueur:

    def __init__(self, nom, prenom, date_naissance, id_national) -> None:
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.id_national = id_national
        self.match_gagne = 0
        self.match_perdu = 0
        self.match_total = 0

    def __str__(self):
        return (
            f"{self.nom} {self.prenom}\n"
            f"Id national échec : {self.id_national}\n"
            f"Match gagné : {self.match_gagne}\n"
            f"Match perdu : {self.match_perdu}\n"
            f"Total match joué : {self.match_total}"
        )

    def __repr__(self):
        return f"Joueur({self.nom}, {self.prenom}, ID: {self.id_national})"

    def gagner_match(self):
        self.match_gagne += 1
        self.match_total += 1
        print(f"Le joueur {self.nom} a gagné le match")

    def perdre_match(self):
        self.match_perdu += 1
        self.match_total += 1
        print(f"Le joueur {self.nom} a perdu le match")

    def to_dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "id_national": self.id_national,
            "match_gagne": self.match_gagne,
            "match_perdu": self.match_perdu,
            "match_total": self.match_total,
        }
