import json
import os
from controllers.joueur_controller import *
from view.MenuSelect import *


save_json = {
    "nom_jouer": "Juan",
    "partie_gagne": 2,
    "match_gagne": 5,
    "dernier_rival": "Thoma",
}


# print("data antes de json : ",save_json)

# DUMPS  indent=4 la plus utilisé
# data_json = json.dumps(save_json, indent=4)


# with open("sampleWithDumps.json", "w") as file:
#     file.write(data_json)


## con DUMP no usamos .write, usamos el FP=burrfer que necesitamos, es decir archivo que escribimo

# def save_json_file(data : dict ):
#         if not isinstance(data, dict):
#             print("Erreur, L'argument est pas un dictionaire de data ")
#             return

#         os.makedirs("data", exist_ok=True)
#         with open("data/SampleDump.json", "w") as file:
#             json.dump(data, file, indent=4)
#             print('Fichier Json Savegarde')
#             return


# save_json_file(save_json)


def main():

    start_app()
    # ajouter_joueur()


if __name__ == "__main__":
    main()
