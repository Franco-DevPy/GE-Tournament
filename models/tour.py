from colorama import Back, Fore, Style, init
import random
from typing import List
from models.match import Match
from models.joueur import Joueur


# necesito llamar la clase jugador para moder manipular los jugadores?
# from models.joueur import Joueur


class Tour:

    def __init__(self, number_tour, tournoi=None):
        self.number_tour = number_tour
        self.liste_joueur: List[Joueur] = tournoi.liste_joueur
        self.liste_match: List[Match] = []
        self.tournoi = tournoi
        if number_tour == 1:
            self.generate_matches_first_tour()
        else:
            self.generate_matches_hazard()

    def generate_matches_first_tour(self) -> list:

        random.shuffle(self.liste_joueur)
        new_liste_match = []
        nombre_match = 1

        for paire_joueur in range(0, len(self.liste_joueur), 2):

            joueur1 = self.liste_joueur[paire_joueur]
            joueur2 = self.liste_joueur[paire_joueur + 1]

            new_match = Match(
                nombre_match=nombre_match,
                joueur1=joueur1,
                joueur2=joueur2,
                score_jouer1=0,
                score_jouer2=0,
            )

            if joueur2.id_national not in joueur1.jouers_rencontres:
                joueur1.jouers_rencontres[joueur2.id_national] = []
            if joueur1.id_national not in joueur2.jouers_rencontres:
                joueur2.jouers_rencontres[joueur1.id_national] = []

            joueur1.jouers_rencontres[joueur2.id_national].append(self.number_tour)
            joueur2.jouers_rencontres[joueur1.id_national].append(self.number_tour)

            new_liste_match.append(new_match)
            print(
                f"{Back.BLUE + Fore.BLACK}♜  {joueur1.nom + ' - ID :' + joueur1.id_national} ♜  {Style.RESET_ALL}  VS  {Back.BLUE + Fore.BLACK}♜  {joueur2.nom + ' - ID :' + joueur2.id_national} ♜ {Style.RESET_ALL} \n "
            )
            nombre_match += 1

        self.liste_match.extend(new_liste_match)

        return self.liste_match

    def generate_matches(self) -> list:
        print(
            Back.BLUE + f" -- Génération  Tour (generate_matches) {self.number_tour} --"
        )
        new_liste_match = []
        # nombre_match = 1

        # Aquí se emparejan los jugadores según los resultados de los matchs previos
        for paire_joueur in range(0, len(self.liste_joueur), 2):
            joueur1 = self.liste_joueur[paire_joueur]
            joueur2 = self.liste_joueur[paire_joueur + 1]

            new_match = Match(
                nombre_match=nombre_match,
                joueur1=joueur1,
                joueur2=joueur2,
                score_jouer1=0,
                score_jouer2=0,
            )

            new_liste_match.append(new_match)
            print(
                f"{Back.BLUE + Fore.BLACK}♜  {joueur1.nom + ' - ID :' + joueur1.id_national} ♜  {Style.RESET_ALL}  VS  {Back.BLUE + Fore.BLACK}♜  {joueur2.nom + ' - ID :' + joueur2.id_national} ♜ {Style.RESET_ALL} \n "
            )
            nombre_match += 1

        self.liste_match.extend(new_liste_match)
        return self.liste_match

    def generate_matches_hazard(self) -> list:
        print(
            Back.BLUE
            + f" -- Génération HAZARD Tour (generate_matches) {self.number_tour} --"
        )
        new_liste_match = []
        nombre_match = 1

        # ORDENAR JUGADORES POR PUNTOS (Mayor a menor)
        self.liste_joueur.sort(key=lambda x: x.match_gagne, reverse=True)

        # Crear una copia de la lista de jugadores para evitar modificaciones directas durante la iteración
        copy_liste_joueur: List[Joueur] = self.liste_joueur[:]

        # Crear una lista de jugadores ya emparejados para evitar duplicados
        jugadores_emparejados = []

        while copy_liste_joueur:
            joueur1 = copy_liste_joueur.pop(
                0
            )  # Sacamos al primer jugador con más puntos

            # Verificamos si el jugador ya está emparejado
            if joueur1.id_national in jugadores_emparejados:
                continue

            # Buscar un oponente válido con las condiciones de "mejor oponente"
            adversaire = self.trouver_adversaire(joueur1, copy_liste_joueur)

            if adversaire is None:
                print(f"No se encontró oponente adecuado para {joueur1.nom}")
                continue  # Si no encontramos oponente, seguimos con el siguiente jugador

            # Marcar a los jugadores como emparejados
            jugadores_emparejados.append(joueur1.id_national)
            jugadores_emparejados.append(adversaire.id_national)

            # Crear un nuevo match
            new_match = Match(
                nombre_match=nombre_match,
                joueur1=joueur1,
                joueur2=adversaire,
                score_jouer1=0,
                score_jouer2=0,
            )

            # Añadimos los jugadores a los registros de encuentros
            if adversaire.id_national not in joueur1.jouers_rencontres:
                joueur1.jouers_rencontres[adversaire.id_national] = []
            if joueur1.id_national not in adversaire.jouers_rencontres:
                adversaire.jouers_rencontres[joueur1.id_national] = []

            joueur1.jouers_rencontres[adversaire.id_national].append(self.number_tour)
            adversaire.jouers_rencontres[joueur1.id_national].append(self.number_tour)

            # Añadimos el nuevo match a la lista de partidos
            new_liste_match.append(new_match)

            # Mostramos el enfrentamiento generado
            print(
                f"{Back.BLUE + Fore.BLACK}♜  {joueur1.nom} vs {adversaire.nom} ♜ {Style.RESET_ALL}"
            )
            nombre_match += 1

        self.liste_match.extend(
            new_liste_match
        )  # Añadimos los nuevos partidos a la lista de partidos
        return self.liste_match

    def trouver_adversaire(
        self, joueur1: Joueur, lista_jugadores: List[Joueur]
    ) -> Joueur:
        adversaire = None
        min_fois_jouer = float("inf")  # Inicializamos con un valor muy alto

        for joueur2 in lista_jugadores:
            if joueur1.id_national == joueur2.id_national:
                continue  # Evita que un jugador se enfrente a sí mismo

            if not self.deja_recontre(joueur1, joueur2):
                return joueur2  # Si encontramos a un jugador con el que nunca jugó, lo elegimos de inmediato

            fois_jouer_deja = self.combien_fois_joue(joueur1, joueur2)

            if fois_jouer_deja < min_fois_jouer:
                adversaire = joueur2
                min_fois_jouer = fois_jouer_deja  # Guardamos la menor cantidad de enfrentamientos encontrados

        return adversaire  # Devuelve el mejor oponente que encontramos

    def deja_recontre(self, joueur1: Joueur, joueur2: Joueur) -> bool:

        # Recorremos todos los partidos jugados
        for match in self.liste_match:
            # Si el partido fue entre jugador1 y jugador2 (sin importar el orden), devolvemos True
            if (
                match.joueur1.id_national == joueur1.id_national
                and match.joueur2.id_national == joueur2.id_national
            ) or (
                match.joueur1.id_national == joueur2.id_national
                and match.joueur2.id_national == joueur1.id_national
            ):
                return True

        return False

    def combien_fois_joue(self, joueur1: Joueur, joueur2: Joueur) -> int:
        quantite = 0

        for match in self.liste_match:
            if (
                match.joueur1.id_national == joueur1.id_national
                and match.joueur2.id_national == joueur2.id_national
            ) or (
                match.joueur1.id_national == joueur2.id_national
                and match.joueur2.id_national == joueur1.id_national
            ):
                quantite += 1

        return quantite

    def to_dict(self):
        return {
            "nom_tour": self.number_tour,
            # "liste_joueur": [joueur.to_dict() for joueur in self.liste_joueur],
            "liste_match": [match.to_dict() for match in self.liste_match],
        }

    # def generate_matches_hazard(self) -> list:
    #     print(
    #         Back.BLUE
    #         + f" -- Génération HAZARD Tour (generate_matches) {self.number_tour} --"
    #     )
    #     new_liste_match = []
    #     nombre_match = 1

    #     self.liste_joueur.sort(key=lambda x: x.match_gagne, reverse=True)

    #     copy_liste_joueur: List[Joueur] = self.liste_joueur[:]

    #     while copy_liste_joueur:
    #         joueur1 = copy_liste_joueur.pop(0)
    #         for i, joueur2 in enumerate(copy_liste_joueur):
    #             if joueur2.id_national not in joueur1.jouers_rencontres:
    #                 copy_liste_joueur.pop(i)

    #                 new_match = Match(
    #                     nombre_match=nombre_match,
    #                     joueur1=joueur1,
    #                     joueur2=joueur2,
    #                     score_jouer1=0,
    #                     score_jouer2=0,
    #                 )

    #                 if joueur2.id_national not in joueur1.jouers_rencontres:
    #                     joueur1.jouers_rencontres[joueur2.id_national] = []
    #                 if joueur1.id_national not in joueur2.jouers_rencontres:
    #                     joueur2.jouers_rencontres[joueur1.id_national] = []

    #                 joueur1.jouers_rencontres[joueur2.id_national].append(
    #                     self.number_tour
    #                 )
    #                 joueur2.jouers_rencontres[joueur1.id_national].append(
    #                     self.number_tour
    #                 )

    #                 new_liste_match.append(new_match)
    #                 print(
    #                     f"{Back.BLUE + Fore.BLACK}♜  {joueur1.nom} vs {joueur2.nom} ♜ {Style.RESET_ALL}"
    #                 )
    #                 nombre_match += 1
    #                 break

    #     self.liste_match.extend(new_liste_match)
    #     return self.liste_match
