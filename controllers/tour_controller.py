from controllers.match_controller import start_match
from controllers.save_file import save_data_file_tournement
from controllers.menu_controller import (
    menu_match_suivant,
    menu_tour_suivant,
    menu_fin_tournois,
)
from colorama import Back, Style


def continuer_tour(tournoi_selectione):
    while len(tournoi_selectione.liste_tour) < tournoi_selectione.nombre_tour:
        if len(tournoi_selectione.liste_tour) < tournoi_selectione.nombre_tour:
            tournoi_selectione.generate_tour()
        menu_match_suivant()
        tours_suivante = tournoi_selectione.liste_tour[-1]
        start_match(tours_suivante)
        save_data_file_tournement(tournoi_selectione)
        if len(tournoi_selectione.liste_tour) < tournoi_selectione.nombre_tour:
            menu_tour_suivant()
        pass

    print(
        Back.BLACK
        + """
        ___ ___ _  _   ___  _   _   _____ ___  _   _ ___ _  _  ___ ___   
        | __|_ _| \| | |   \| | | | |_   _/ _ \| | | | _ \ \| |/ _ \_ _| 
        | _| | || .` | | |) | |_| |   | || (_) | |_| |   / .` | (_) | |  
        |_| |___|_|\_| |___/ \___/    |_| \___/ \___/|_|_\_|\_|\___/___|
                    """
        + Style.RESET_ALL
        + "\n"
    )
    tournoi_selectione.date_fin = tournoi_selectione.get_time()
    save_data_file_tournement(tournoi_selectione)
    menu_fin_tournois(tournoi_selectione)
