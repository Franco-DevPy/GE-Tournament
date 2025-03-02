Gestionnaire de Tournois d'Échecs

Description

Le Gestionnaire de Tournois d'Échecs est une application Python permettant de créer, gérer et suivre des tournois d'échecs de manière autonome. Elle fonctionne en mode console et utilise un système de sauvegarde basé sur JSON pour enregistrer et charger les données des tournois et des joueurs. L'application permet :

- L'ajout de joueurs avec leur identifiant national et leurs statistiques.
- La création de nouveaux tournois avec un nombre défini de tours.
- La gestion des matchs et l'attribution des points.
- La sauvegarde et le chargement des tournois en cours pour pouvoir les reprendre ultérieurement.

Installation

Prérequis

Python 3.8+ doit être installé sur votre système.

pip doit être installé pour gérer les dépendances.

Installation avec un environnement virtuel

Il est recommandé d'utiliser un environnement virtuel pour installer les dépendances du projet.

Windows

# Création de l'environnement virtuel

python -m venv venv

# Activation de l'environnement virtuel

venv\Scripts\activate

# Installation des dépendances

pip install -r requirements.txt

Linux & macOS

# Création de l'environnement virtuel

python3 -m venv venv

# Activation de l'environnement virtuel

source venv/bin/activate

# Installation des dépendances

pip install -r requirements.txt

Exécution de l'application

Après l'installation, vous pouvez lancer l'application en exécutant la commande suivante :

python main.py

Cela ouvrira l'interface console de l'application où vous pourrez créer un tournoi, ajouter des joueurs et gérer les matchs.
