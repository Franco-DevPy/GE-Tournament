from models.joueur import Joueur
from colorama import Fore, Back, Style, init
import re
import datetime
import time
from controllers.save_file import *


regex_id = r"^[A-Z]{2}\d{5}$"
# regex_date =

init(autoreset=True)


def ajouter_joueur():

    reponse_liste = get_liste_joueur()

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
    new_dict_joueur = new_joueur.to_dict()

    reponse_liste.append(new_dict_joueur)

    # ERROR YA ES UN DICTIONARIO
    # liste_dict = [joueur.to_dict() for joueur in reponse_liste]
    ##total_list = liste_dict + reponse_liste

    save_data_file_players(reponse_liste)
    print(Back.GREEN + "  New Player Created :  ")
    print(new_joueur)


def get_liste_joueur():
    player_dict = load_data_file_players()
    player_dict.sort(key=lambda jugador: jugador["nom"])

    return player_dict


# ACA PUEDO HACER UNA TYPO DE EL LA CLASSE O UN ENUM PARA QUE ASEGUREMOS Y DETECTE "la classe jugador"
def voir_liste_joueur(all_joueur):
    print(Back.CYAN + Fore.BLACK + "LISTE DES JOUEURS :" + Style.RESET_ALL)
    for joueur in all_joueur:
        print(Fore.GREEN + "Nom:" + Fore.WHITE + joueur["nom"])
        print(Fore.GREEN + "Prénom:" + Fore.WHITE + joueur["prenom"])
        print(Fore.GREEN + "ID National:" + Fore.WHITE + joueur["id_national"])
        print(
            Fore.GREEN
            + "Matchs Gagnés:"
            + Fore.WHITE
            + str(joueur.get("match_gagne", 0))
        )
        print(
            Fore.GREEN
            + "Matchs Perdus:"
            + Fore.WHITE
            + str(joueur.get("match_perdu", 0))
        )
        print(
            Fore.GREEN
            + "Matchs Totals:"
            + Fore.WHITE
            + str(joueur.get("match_total", 0))
            + "\n"
        )
