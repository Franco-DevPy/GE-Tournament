from models.joueur import Joueur
from colorama import Fore, Back, Style, init
import re
import datetime
import time
from controllers.save_file import *
from questionary import checkbox, select, Style as QuestionaryStyle


regex_id = r"^[A-Z]{2}\d{5}$"
# regex_date =


custom_style = QuestionaryStyle(
    [
        ("qmark", "fg:#E91E63 bold"),  # Color del símbolo de pregunta
        ("question", "bold"),  # Estilo del mensaje de pregunta
        ("pointer", "fg:#1815d1 bold"),  # Color del puntero en las opciones
        ("highlighted", "fg:#03A9F4"),  # Color de la opción resaltada
        ("selected", "fg:#0D47A1"),  # Color de la opción seleccionada
        ("answer", "fg:#2196f3 bold"),  # Color de la respuesta
        ("text", "bold"),  # Estilo del texto (por defecto)
        ("separator", "fg:#CC5454"),  # Estilo del separador
        ("instruction", "#0D47A1"),  # Estilo de las instrucciones (si las hay)
        ("disabled", "fg:#858585 italic"),  # Estilo de opciones deshabilitadas
    ]
)

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

    save_data_file_players(reponse_liste)
    print(Back.GREEN + "  New Player Created :  ")
    print(new_joueur)


def get_liste_joueur():
    joueurs = load_data_file_players()
    joueurs.sort(key=lambda joueur: joueur.nom)
    return joueurs


# ACA PUEDO HACER UNA TYPO DE EL LA CLASSE O UN ENUM PARA QUE ASEGUREMOS Y DETECTE "la classe jugador"
# def voir_liste_joueur(all_joueur):
#     print(Back.CYAN + Fore.BLACK + "LISTE DES JOUEURS :" + Style.RESET_ALL)
#     for joueur in all_joueur:
#         print(Fore.GREEN + "Nom:" + Fore.WHITE + joueur["nom"])
#         print(Fore.GREEN + "Prénom:" + Fore.WHITE + joueur["prenom"])
#         print(Fore.GREEN + "ID National:" + Fore.WHITE + joueur["id_national"])
#         print(
#             Fore.GREEN
#             + "Matchs Gagnés:"
#             + Fore.WHITE
#             + str(joueur.get("match_gagne", 0))
#         )
#         print(
#             Fore.GREEN
#             + "Matchs Perdus:"
#             + Fore.WHITE
#             + str(joueur.get("match_perdu", 0))
#         )
#         print(
#             Fore.GREEN
#             + "Matchs Totals:"
#             + Fore.WHITE
#             + str(joueur.get("match_total", 0))
#             + "\n"
#         )


def voir_liste_joueur(all_joueur):
    print(Back.CYAN + Fore.BLACK + "LISTE DES JOUEURS :" + Style.RESET_ALL)
    for joueur in all_joueur:
        print(joueur, "\n")


def select_joueur_tournoi():

    liste_select_joueur = get_liste_joueur()

    choices = []
    ##ENTEDER ESTO
    for joueur in liste_select_joueur:
        choices.append(
            {
                "name": f"{joueur.nom} {joueur.prenom} ({joueur.id_national})",
                "value": joueur,  # El diccionario completo del jugador
            }
        )

    ## MUY DIFICIL Y FRUSTRANTE ESTA PARTE NO ENTIENDO NADA LO QUE HACE Y LO HICE GPT
    rpse_choix_joueur = checkbox(
        "Selectioner Joueur pour le Tournois",
        choices=choices,
        style=custom_style,
    ).ask()

    return rpse_choix_joueur
