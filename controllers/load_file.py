from pathlib import Path
from colorama import Back
import json
from models.tournoi import Tournoi
from models.joueur import Joueur


# def load_data_file_players():
#     try:
#         data = Path("data/players.json").read_text(encoding="utf-8")
#         players_list = json.loads(data)
#         # Convertir cada diccionario en un objeto Joueur
#         joueurs = [Joueur.from_dict(player_data) for player_data in players_list]
#         return joueurs
#     except Exception as e:
#         print(f"Error en load_data_file_players: {e}")
#         return []


def load_tournois():
    chemin_fichier = Path("data/tournament.json")

    if not chemin_fichier.exists():
        print(Back.RED + " Aucun tournoi sauvegardé.")
        return []

    data = chemin_fichier.read_text()
    try:
        liste_tournois = json.loads(data, object_hook=Tournoi.from_dict)
        print(Back.GREEN + "Tournois chargés avec succès.")
        return liste_tournois
    except json.JSONDecodeError:
        print(Back.RED + " Erreur de chargement du fichier.")
        return []
