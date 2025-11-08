"""
Tests du rendu HTML de la page d'accueil.
"""

import pytest
from app import app

@pytest.fixture
def client():
    """Crée un client de test Flask."""
    with app.test_client() as client:
        yield client


def test_calculator_title(client):
    """Vérifie que le titre de la calculatrice est présent."""
    response = client.get("/")
    html = response.data.decode("utf-8")
    
    assert "<title>Flask Calculator</title>" in html, "Titre de la page manquant"
    assert "<h1>Flask Calculator</h1>" in html, "En-tête H1 manquant"


def test_number_buttons_text(client):
    """
    Vérifie que tous les boutons numériques affichent le bon texte.
    """
    response = client.get("/")
    html = response.data.decode("utf-8")
    
    expected_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    errors = []
    for num in expected_numbers:
        if f">{num}</button>" not in html:
            errors.append(f"Le bouton {num} devrait afficher '{num}' comme texte")
    
    assert not errors, "Bugs trouvés:\n" + "\n".join(errors)


def test_number_buttons_onclick(client):
    """
    Vérifie que tous les boutons numériques ont la bonne valeur dans onclick.
    """
    response = client.get("/")
    html = response.data.decode("utf-8")
    
    expected_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    errors = []
    for num in expected_numbers:
        if f"appendToDisplay('{num}')" not in html:
            errors.append(f"Le bouton {num} devrait appeler appendToDisplay('{num}')")
    
    assert not errors, "Bugs trouvés:\n" + "\n".join(errors)

def test_operator_buttons(client):
    """
    Vérifie que tous les boutons d'opérateurs sont présents.
    """
    response = client.get("/")
    html = response.data.decode("utf-8")
    
    operators = ['+', '-', '*', '/']
    
    errors = []
    for op in operators:
        if f"appendToDisplay('{op}')" not in html:
            errors.append(f"Le bouton opérateur {op} devrait être présent")
    
    assert not errors, "Bugs trouvés:\n" + "\n".join(errors)


def test_operator_buttons_text(client):
    """
    Vérifie que tous les boutons d'opérateurs affichent leur symbole.
    BUG ATTENDU: Certains opérateurs peuvent ne pas avoir de texte visible.
    """
    response = client.get("/")
    html = response.data.decode("utf-8")
    
    operators = ['+', '-', '*', '/']
    
    errors = []
    for op in operators:
        pattern = f"appendToDisplay('{op}')\">{op}</button>"
        if pattern not in html:
            errors.append(f"Le bouton opérateur {op} devrait afficher le symbole '{op}'")
    
    assert not errors, "Bugs trouvés:\n" + "\n".join(errors)
        

def test_clear_button(client):
    """Vérifie que le bouton Clear est présent et fonctionnel."""
    response = client.get("/")
    html = response.data.decode("utf-8")
    
    assert "clearDisplay()" in html, "Fonction clearDisplay manquante"
    assert ">C</button>" in html, "Bouton Clear (C) manquant"


def test_calculate_button(client):
    """Vérifie que le bouton de calcul (=) est présent."""
    response = client.get("/")
    html = response.data.decode("utf-8")
    
    assert 'type="submit"' in html, "Bouton submit manquant"
    assert ">=</button>" in html, "Bouton égal (=) manquant"

def test_all_buttons_count(client):
    """Vérifie qu'il y a le bon nombre de boutons (10 chiffres + 4 opérateurs + 1 clear + 1 égal = 16)."""
    response = client.get("/")
    html = response.data.decode("utf-8")
    
    button_count = html.count("<button")
    expected_count = 16
    
    assert button_count == expected_count, \
        f"Devrait avoir {expected_count} boutons, mais {button_count} trouvés"