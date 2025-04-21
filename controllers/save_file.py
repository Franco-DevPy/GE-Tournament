import json
from pathlib import Path
from colorama import Fore, Back, Style
from models.tournoi import Tournoi


# PLAYERS DATA
def save_data_file_players(players: list):
    if not isinstance(players, list):
        print(Back.RED + " Error, argument is not a players list  ")
        return
    players.sort(key=lambda jugador: jugador["nom"])
    data = json.dumps(players)
    Path("data/players.json").write_text(data)
    print(Back.CYAN + Fore.BLACK + " - LES JOUEURS ONT ÉTÉ SAUVEGARDÉS AVEC SUCCÈS - ")


# TOURNEMENT DATA
def save_data_file_tournement(new_tournoi: Tournoi):
    file_path = Path("data/tournament.json")

    if file_path.exists():
        try:
            liste_tournois = json.loads(file_path.read_text())
        except json.JSONDecodeError:
            liste_tournois = []
    else:
        liste_tournois = []

    save_tournois = new_tournoi.to_dict()

    tournoi_existant = next(
        (t for t in liste_tournois if t["nom_tournoi"] == save_tournois["nom_tournoi"]),
        None,
    )

    if tournoi_existant:
        liste_tournois = [
            save_tournois if t["nom_tournoi"] == save_tournois["nom_tournoi"] else t
            for t in liste_tournois
        ]
    else:
        liste_tournois.append(save_tournois)

    file_path.write_text(json.dumps(liste_tournois, indent=4))

    print(Back.GREEN + "Tournoi sauvegardé avec succès !" + Style.RESET_ALL)
