from models.tournoi import Tournoi
from controllers.save_file import save_data_file_tournement
from controllers.joueur_controller import select_joueur_tournoi
from colorama import Fore, Back, Style, init
from datetime import datetime as dt
from questionary import select, Style as QuestionaryStyle
from models.tour import Tour

# from save_file import save_data_file_tournement


init(autoreset=True)

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


def create_tournoi() -> Tournoi:
    print(Back.BLUE + "-----Creation du Tournoi-----")

    # reponse_dernier_tournoi = get_dernier_tournois()
    nom_tournoi = input("Entrez le NOM du Tournoi : ")
    lieu_tournoi = input("Entrez le LIEU du Tournoi : ")
    date_debut = dt.now().strftime("%Y-%m-%d %H:%M")

    description_tournoi = input("Entrez une description du Tournoi : ")
    nombre_tour_actuel = 0
    nombre_tour = 0
    joueurs_selectionnes = select_joueur_tournoi()

    new_tournoi = Tournoi(
        nom_tournoi=nom_tournoi,
        location=lieu_tournoi,
        description=description_tournoi,
        date_debut=date_debut,
        liste_joueur=joueurs_selectionnes,
    )

    print(Back.GREEN + "--- Le Tournois a été crée avec succes ---")

    new_tournoi.generate_tour()

    print(Back.BLUE + "--- La generation de tour a été finalisé ---")
    save_tournois = new_tournoi.to_dict()

    save_data_file_tournement(save_tournois)

    return new_tournoi
