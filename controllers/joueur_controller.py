from models.joueur import Joueur
from colorama import Fore, Back, Style, init
import re
import datetime
import time
from controllers.save_file import *


regex_id = r"^[A-Z]{2}\d{5}$"
# regex_date =

init(autoreset=True)

liste_joueur = []


def ajouter_joueur():
    nom = input("Entrez le nom du joueur : ")
    prenom = input("Entrez le prenom du joueur : ")
    while True:
        date_naissance = input("Entrez la date de naissance: JJ/MM/AAAA :  ")
        try:
            date_format = datetime.datetime.strptime(date_naissance, "%d/%m/%Y").date()
            break

        except ValueError:
            print(Fore.RED + "Format Date naissance invalide")

    while True:
        nombre_id = input("Entrez l'identifiant national : ")
        if re.match(regex_id, nombre_id):
            print(Fore.GREEN + "L'identifiant national est valide")
            break
        else:
            print(Fore.RED + "L'identifiant national est invalide")

    new_joueur = Joueur(nom, prenom, date_format, nombre_id)
    liste_joueur.append(new_joueur)

    liste_dict = [joueur.to_dict() for joueur in liste_joueur]

    save_data_file_players(liste_dict)
    print(Back.GREEN + "  New Player Created :  ")
    print(new_joueur)


def get_liste_joueur():
    player_dict = load_data_file_players()
    # print("la lista de joueur est : ", player_dict)
    return player_dict


def voir_liste_joueur(all_joueur: list):
    print(Back.CYAN + Fore.BLACK + "LISTE DES JOUEURS : ")
    print(type(all_joueur))
