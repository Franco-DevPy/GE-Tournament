# from colorama import Back, Fore, Style
# from questionary import select, Style as QuestionaryStyle


# custom_style = QuestionaryStyle(
#     [
#         ("qmark", "fg:#E91E63 bold"),  # Color del símbolo de pregunta
#         ("question", "bold"),  # Estilo del mensaje de pregunta
#         ("pointer", "fg:#1815d1 bold"),  # Color del puntero en las opciones
#         ("highlighted", "fg:#03A9F4"),  # Color de la opción resaltada
#         ("selected", "fg:#0D47A1"),  # Color de la opción seleccionada
#         ("answer", "fg:#2196f3 bold"),  # Color de la respuesta
#         ("text", "bold"),  # Estilo del texto (por defecto)
#         ("separator", "fg:#CC5454"),  # Estilo del separador
#         ("instruction", "#0D47A1"),  # Estilo de las instrucciones (si las hay)
#         ("disabled", "fg:#858585 italic"),  # Estilo de opciones deshabilitadas
#     ]
# )


# def print_welcome_message():
#     print(
#         Back.CYAN
#         + Fore.BLACK
#         + """  ♟ ♜ ♞ ♝ ♛ ÉCHECSMANAGER ♚ ♝ ♞ ♜ ♟   """
#         + Style.RESET_ALL
#     )


# def print_end_tournament_message():
#     print(
#         Back.BLACK
#         + """
#      ___ ___ _  _   ___  _   _   _____ ___  _   _ ___ _  _  ___ ___
#     | __|_ _| \| | |   \| | | | |_   _/ _ \| | | | _ \ \| |/ _ \_ _|
#     | _| | || .` | | |) | |_| |   | || (_) | |_| |   / .` | (_) | |
#     |_| |___|_|\_| |___/ \___/    |_| \___/ \___/|_|_\_|\_|\___/___|
#                 """
#         + Style.RESET_ALL
#         + "\n"
#     )


# def handle_create_tournament():
#     new_tournoi = create_tournoi()
#     premier_tour = new_tournoi.liste_tour[0]
#     menu_start_tournois(premier_tour)

#     while len(new_tournoi.liste_tour) < new_tournoi.nombre_tour:
#         if len(new_tournoi.liste_tour) < new_tournoi.nombre_tour:
#             new_tournoi.generate_tour()
#         menu_match_suivant()
#         tours_suivante = new_tournoi.liste_tour[-1]
#         start_match(tours_suivante)
#         save_data_file_tournement(new_tournoi)
#         if len(new_tournoi.liste_tour) < new_tournoi.nombre_tour:
#             menu_tour_suivant()

#     print_end_tournament_message()
#     new_tournoi.date_fin = new_tournoi.get_time()
#     save_data_file_tournement(new_tournoi)
#     menu_fin_tournois(new_tournoi)


# def start_app():
#     load_data_file_players()
#     print_welcome_message()

#     select_menu = [
#         "Creér un Tournoi",
#         "Gestion du Joueur",
#         "Gestion des Tournois",
#         "Exit",
#     ]

#     respuesta = select(
#         message="--Menu Principal--",
#         choices=select_menu,
#         style=custom_style,
#     ).ask()

#     if respuesta == "Creér un Tournoi":
#         handle_create_tournament()
#     elif respuesta == "Gestion du Joueur":
#         handle_player_management()
#     elif respuesta == "Gestion des Tournois":
#         handle_tournament_management()
#     elif respuesta == "Exit":
#         handle_exit()
