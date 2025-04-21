from models.joueur import Joueur
from colorama import Fore, Back, Style, init
import re
import datetime

from controllers.save_file import save_data_file_players
from questionary import checkbox, Style as QuestionaryStyle
from controllers.data_load_player import load_data_file_players


regex_id = r"^[A-Z]{2}\d{5}$"


custom_style = QuestionaryStyle(
    [
        ("qmark", "fg:#E91E63 bold"),
        ("question", "bold"),
        ("pointer", "fg:#1815d1 bold"),
        ("highlighted", "fg:#03A9F4"),
        ("selected", "fg:#0D47A1"),
        ("answer", "fg:#2196f3 bold"),
        ("text", "bold"),
        ("separator", "fg:#CC5454"),
        ("instruction", "#0D47A1"),
        ("disabled", "fg:#858585 italic"),
    ]
)

init(autoreset=True)


def ajouter_joueur():

    reponse_liste = get_liste_joueur()

    reponse_liste_dict = [joueur.to_dict() for joueur in reponse_liste]

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

    reponse_liste_dict.append(new_dict_joueur)

    save_data_file_players(reponse_liste_dict)
    print(Back.GREEN + "  Nouveau Joueur Crée :  ")
    print(new_joueur)


def get_liste_joueur():
    joueurs = load_data_file_players()
    joueurs.sort(key=lambda joueur: joueur.nom)
    return joueurs


def get_all_players_id_dict():
    players = load_data_file_players()
    players.sort(key=lambda joueur: joueur.nom)
    players_dict = {}

    for player in players:
        players_dict[player.id_national] = player

    return players_dict


def voir_liste_joueur(all_joueur):
    print(Back.CYAN + Fore.BLACK + "LISTE DES JOUEURS :" + Style.RESET_ALL)
    for joueur in all_joueur:
        print(joueur, "\n")


def select_joueur_tournoi() -> list[Joueur]:

    liste_select_joueur = get_liste_joueur()

    choices = []
    for joueur in liste_select_joueur:
        choices.append(
            {
                "name": f"{joueur.nom} {joueur.prenom} ({joueur.id_national})",
                "value": joueur,
            }
        )
    while True:
        rpse_choix_joueur = checkbox(
            "Selectioner Joueur pour le Tournois",
            choices=choices,
            style=custom_style,
        ).ask()

        if rpse_choix_joueur is None or len(rpse_choix_joueur) < 2:
            print(
                Back.RED + " -- ⚠ VOUS DEVEZ SELECTIONNER AU MOINS DEUX JOUEUR. ⚠ -- "
            )

        if len(rpse_choix_joueur) % 2 != 0:
            print(Back.RED + " -- ⚠ LA QUANTITÉ DE JOUEURS DOIT ÊTRE PAIRE. ⚠ -- ")

        else:
            return rpse_choix_joueur
