from models.tournoi import Tournoi
from controllers.joueur_controller import select_joueur_tournoi
from colorama import Fore, Back, Style, init
import datetime
from questionary import select, Style as QuestionaryStyle

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


def create_tournoi():
    print(Back.BLUE + "-----Creation du Tournoi-----")

    select_joueur_tournoi()
    # reponse_dernier_tournoi = get_dernier_tournois()
    nom_tournoi = input("Entrez le nom du Tournoi : ")
    lieu_tournoi = input("Entrez le lieu du Tournoi : ")
    # date_debout = datetime()
    # date_fin = datetime()
    description_tournoi = input("Entrez une description du Tournoi")
    nombre_tour_actuel = 0
    nombre_tour = 0

    Tournoi(
        nom_tournoi,
        lieu_tournoi,
        description_tournoi,
    )

    print(Back.GREEN + "Le Tournois a été crée")


# problema, estoy avazando pero creo que hay cosas que me limitan y pido a chatgpt, este me da opciones y entre eso me da codigo de como deberia hacerlo, como puedo gestionar esto
