from models.joueur import Joueur
from colorama import Fore, Back, Style, init
import re
import datetime
import time


regex_id = r'^[A-Z]{2}\d{5}$'
# regex_date = 

init(autoreset=True)

liste_joueur = []


def ajouter_joueur():
    nom = input("Entrez le nom du joueur : ")
    prenom = input("Entrez le prenom du joueur : ")
    while True:
        date_naissance = input("Entrez la date de naissance: JJ/MM/AAAA :  ")
        try: 
            date_format = datetime.datetime.strptime( date_naissance, "%d/%m/%Y").date()
            break
        
        except ValueError:
            print(Fore.RED + "Format Date naissance invalide")
            
    
    while True: 
       nombre_id = input("Entrez l'identifiant national : " )
       if re.match(regex_id, nombre_id):
           print (Fore.GREEN + "L'identifiant national est valide")
           break
       else:
           print(Fore.RED + "L'identifiant national est invalide")
    
    new_joueur =  Joueur( nom , prenom, date_format, nombre_id)
    liste_joueur.append(new_joueur)   
    print(Back.GREEN + "  New Player Created :  ")
    print(new_joueur)
    




liste_all_joueur = [
    "lala" , "lolo" , "lele" , "lili"
    
]

def get_liste_joueur():
    print("la lista de joueur est : ",liste_joueur)
    return liste_joueur



def voir_liste_joueur():
    print(Back.CYAN + "LISTE DE JOUEURler : ")
    for joeur in liste_joueur:
        print(joeur)
    
    


