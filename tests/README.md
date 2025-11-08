# tests/

## Description
Ce dossier contient les tests automatisés de l'application. Les tests vérifient que chaque fonction fait bien ce qu'elle doit faire et permettent de détecter les bogues.

## Contenu
test_operators.py
- Tests pour les opérations mathématiques (add, subtract, multiply, divide)
- 16 tests qui vérifient que les calculs donnent les bons résultats

test_app.py
- Tests pour la fonction calculate() de app.py
- 16 tests qui vérifient le parsing des expressions et la gestion d'erreurs

## Lancer les tests
Installer pytest:
python -m pip install pytest

Lancer tous les tests:
pytest tests/

Avec plus de détails:
pytest tests/ -v

Un fichier spécifique:
- pytest tests/test_operators.py
- pytest tests/test_app.py

## Interpréter les résultats
- PASSED = Le test a réussi, la fonction fonctionne correctement
- FAILED = Le test a échoué, il y a un bogue à corriger
Chaque test qui échoue indique un problème dans le code qu'il faut corriger.

## Structure d'un test
Chaque test vérifie un comportement précis:
Si l'assertion est fausse, pytest affiche une erreur et on sait qu'il y a un bogue.

## Dépendances
- pytest (framework de tests)
- Les modules app.py et operators.py qu'on teste

