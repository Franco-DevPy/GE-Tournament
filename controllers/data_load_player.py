from pathlib import Path
from models.joueur import Joueur
import json


def load_data_file_players():
    try:
        data = Path("data/players.json").read_text(encoding="utf-8")
        players_list = json.loads(data, object_hook=Joueur.from_dict)
        return players_list
    except Exception as e:
        print(f"Error en load_data_file_players: {e}")
        return []
