class Tour:
    
    def __init__(self, date_heure_debout, date_heure_fin, liste_match,nom_tour= 1):
        self.nom = "Round " + nom_tour
        self.date_heure_debout = date_heure_debout #op
        self.date_heure_fin = date_heure_fin #op
        self.liste_match = liste_match
    
    def generate_matches(self):
        """
        Logique de génération des paires
        Tour 3: 
            - A/B
            - C/D
        Résultats après tour 3: 
            - A: 10 pts
            - B: 9 pts
            - C: 4 pts
            - D: 3 pts 
        """
        pass
        
    