## Nom du projet
Calculatrice Web Flask

## Numéro d'équipe
Équipe 33

## Membres de l'équipe
- Praise Mbay
- Mathilde Jean-Brown

## Objectif
Ce projet est une application web de calculatrice simple développée avec Flask. Elle permet d'effectuer les quatre opérations de base: addition, soustraction, multiplication et division.
Dans le cadre du TP3 de LOG3000, on met en pratique les bonnes pratiques de développement: gestion de versions avec Git/GitHub, documentation du code, tests automatisés et travail collaboratif avec des branches et pull requests.

## Description du projet
L'application permet à l'utilisateur d'entrer une expression simple (comme 5 + 3) et d'obtenir le résultat directement dans le navigateur. Si l'expression est invalide ou contient une erreur (division par zéro, format incorrect), un message d'erreur s'affiche.
Le projet contient:
- app.py - Serveur Flask et logique principale
- operators.py - Fonctions mathématiques (add, subtract, multiply, divide)
- templates/ - Fichiers HTML pour l'interface
- static/ - Fichier CSS pour le style

## Prérequis d'installation
Avant de commencer, il faut avoir installé :
- Python 3.8 ou version supérieure
- pip (gestionnaire de paquets Python)
- Git
- Un navigateur web moderne (Chrome, Firefox, Safari, Edge)

## Instructions d’installation et d’exécution
1. **Cloner le dépôt**
   - git clone https://github.com/TP3_LOG3000.git 
   - cd TP3_LOG3000
2. **Installer les dépendances**
   - pip install flask
   - pip install pytest
4. **Lancer l'application**
   - python app.py
   - Le serveur démarre sur http://localhost:5000
5. **Utiliser la calculatrice**
   - Ouvrir http://localhost:5000 dans le navigateur
   - Cliquer sur les chiffres pour entrer un nombre
   - Cliquer sur un opérateur (+, -, *, /)
   - Entrer le deuxième nombre
   - Cliquer sur "=" pour voir le résultat
   - Utiliser "C" pour effacer
   *Note*: Une seule opération à la fois est supportée.
   
## Tests
Les tests vérifient que les opérations mathématiques fonctionnent correctement et que les erreurs sont bien gérées.
1. **Lancer les tests**
   pytest tests/
2.  **Tests spécifiques**
   - pytest tests/test_operators.py
   - pytest tests/test_app.py

## flux de contribution
1. **Structure des branches**
   - main - Branche principale avec le code stable
   - feature/nom - Nouvelles fonctionnalités
2. **Processus**
   1. La création d'une branche, la modification d'un fichier, le commit et pousser sur la        branche:
      - git checkout -b feature/nom 
      - git add fichiers
      - git commit -m "feat: description de l'ajout"
      - git push origin feature/nom 
   2. Ouvrir une Pull Request sur GitHub
   3. Faire réviser par un autre membre
   4. Fusionner une fois approuvé
3. **Conventions de commit**
   - feat: Nouvelle fonctionnalité
   - fix: Correction de bogue
   - test: Tests
   - refactor: Refactorisation

## Technologies utilisées
- Flask (Python) - Framework web
- HTML/CSS - Interface utilisateur
- pytest - Tests automatisés
- Git/GitHub - Gestion de versions

## Auteurs
Projet réalisé dans le cadre du cours LOG3000 à Polytechnique Montréal.
