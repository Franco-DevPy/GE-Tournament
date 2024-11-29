class Tournoi:

    def __init__(
        self,
        nom_tournoi,
        location,
        date_debout,
        date_fin,
        description,
        nombre_tour_actuel=0,
        nombre_tour=4,
    ) -> None:
        self.nom_tournoi = nom_tournoi
        self.location = location
        self.date_debout = date_debout
        self.date_fin = date_fin
        self.nombre_tour = nombre_tour
        self.nombre_tour_actuel = nombre_tour_actuel
        self.liste_tour = []
        self.liste_joeur = []
        self.description = description

        # TODO: Gérer le cas où le nombre de joueurs n’est pas pair

    def __str__(self):
        return (
            f"Le Tournois {self.nom_tournoi}\n"
            f"Adrresse : {self.location}\n"
            f"Date debout {self.date_debout}\n"
            f"Date de fin {self.date_fin}\n"
            f"Description {self.description}\n"
            f"Joueur qui participent {self.liste_joueur}"
        )
