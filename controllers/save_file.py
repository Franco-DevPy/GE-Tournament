import json
from pathlib import Path
import os
from colorama import Fore, Back


# save_json = {
#     "nom_joueur": "Juan",
#     "partie_gagne": 2,
#     " match_gagne": 5,
#     "dernier_rival": "Thoma",
# }

# players = [
#     {
#         "id": 1,
#         "nom_joueur": "Juan",
#         "partie_gagne": 2,
#         "match_gagne": 5,
#         "dernier_rival": "Thoma",
#     },
#     {
#         "id": 2,
#         "nom_joueur": "Thoma",
#         "partie_gagne": 2,
#         "match_gagne": 5,
#         "dernier_rival": "Juan",
#     },
#     {
#         "id": 3,
#         "nom_joueur": "Thoma",
#         "partie_gagne": 2,
#         "match_gagne": 5,
#         "dernier_rival": "Juan",
#     },
# ]

# PATH AND JSON FOR SAVE FILE
# data = json.dumps(players)

# Path("players.json").write_text(data)

# # PATH AND JSON FOR LOAD FILE

# data = Path("players.json").read_text(encoding="utf-8")

# Players_load = json.loads(data)

# print(Players_load)

# # PATH AND JSON FOR EDIT FILE
# Players_load[2]["nom_joueur"] = "Franco"

# Path("players.json").write_text(json.dumps(Players_load))

# print(Players_load)


def save_data_file_players(players: list):
    if not isinstance(players, list):
        print("Error, argument is not a players list ")
        return
    players.sort(key=lambda jugador: jugador["nom"])
    data = json.dumps(players)
    print(data)
    Path("data/players.json").write_text(data)
    print(Back.CYAN + "Les joueurs ont été sauvegardés avec succès")


# como probar funciones ? cuando hay varias en la app
def load_data_file_players():
    try:
        data = Path("data/players.json").read_text(encoding="utf-8")
        players_dict = json.loads(data)
        try:
            # returna un dict
            return players_dict
        except:
            print(Back.RED + "player load ERROR")
    except:
        print("error en load data file")
        return


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
