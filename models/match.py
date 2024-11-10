class Match:
    
    nombre_match = 1
    
    def __init__(self,nombre_match, joueur1 , joueur2, score_jouer1, score_jouer2):
        self.nombre_match = nombre_match
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score_jouer1 = score_jouer1
        self.score_jouer2 = score_jouer2
    
    
    def create_match(self):
        print(f"Le Joueur {self.joueur1} VS {self.joueur2}")
        
        
    def delete_match(self):
        print(f"Le match {self.nombre_match} a été eliminé")
        
        
    def gagner_match(self):
        pass
    
    def perdre_match(self):
        pass
    
    
