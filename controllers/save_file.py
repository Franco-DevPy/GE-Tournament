import json
from pathlib import Path
import os
from colorama import Fore, Back
from models.joueur import Joueur


# PLAYERS DATA
def save_data_file_players(players: list):
    if not isinstance(players, list):
        print("Error, argument is not a players list ")
        return
    players.sort(key=lambda jugador: jugador["nom"])
    data = json.dumps(players)
    Path("data/players.json").write_text(data)
    print(Back.CYAN + Fore.BLACK + " - LES JOUEURS ONT ÉTÉ SAUVEGARDÉS AVEC SUCCÈS - ")


# como probar funciones ? cuando hay varias en la app
def load_data_file_players():
    try:
        data = Path("data/players.json").read_text(encoding="utf-8")
        players_list = json.loads(data)
        # Convertir cada diccionario en un objeto Joueur
        joueurs = [Joueur.from_dict(player_data) for player_data in players_list]
        return joueurs
    except Exception as e:
        print(f"Error en load_data_file_players: {e}")
        return []


# TOURNEMENT DATA
def save_data_file_tournement(tournois: list):
    if not isinstance(tournois, list):
        print("Error , argument is not a tournois")
        return

    data = json.dumps(tournois)
    Path("data/tournament.json").write_text(data)
    print(Back.GREEN + "Le Tournoi a été sauvegardé avec succès")


def load_data_file_tournement():
    data = Path("data/tournament.json").read_text(encoding="utf-8")
    tournament_list = json.load(data)
    print(Back.GREEN + "DERNIER TOURNOI")
    print(tournament_list)


# print("data antes de json : ",save_json)

# DUMPS  indent=4 la plus utilisé
# data_json = json.dumps(save_json, indent=4)


# with open("sampleWithDumps.json", "w") as file:
#     file.write(data_json)


## con DUMP no usamos .write, usamos el FP=burrfer que necesitamos, es decir archivo que escribimo


# def save_json_file(data: dict):
#     if not isinstance(data, dict):
#         print("Erreur, L'argument est pas un dictionaire de data ")
#         return

#     os.makedirs("data", exist_ok=True)
#     with open("data/SampleDumpSI.json", "w") as file:
#         json.dump(data, file, indent=4)
#         print("Fichier Json Savegarde")
#         return
