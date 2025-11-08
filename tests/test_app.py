"""
Tests pour la fonction calculate() du module app.py
Ce fichier teste le parsing et l'évaluation des expressions mathématiques (validations et erreurs).
"""

import pytest
from app import calculate


def test_calculate_addition():
    """Test du calcul d'une addition simple."""
    result = calculate("5 + 3")
    assert result == 8, f"Expected 8 but got {result}"


def test_calculate_subtraction():
    """Test du calcul d'une soustraction simple."""
    result = calculate("10 - 3")
    assert result == 7, f"Expected 7 but got {result}"


def test_calculate_multiplication():
    """Test du calcul d'une multiplication simple."""
    result = calculate("5 * 3")
    assert result == 15, f"Expected 15 but got {result}"


def test_calculate_division():
    """Test du calcul d'une division simple."""
    result = calculate("10 / 2")
    assert result == 5.0, f"Expected 5.0 but got {result}"


def test_calculate_no_spaces():
    """Test du calcul sans espaces dans l'expression."""
    result = calculate("5+3")
    assert result == 8, f"Expected 8 but got {result}"


def test_calculate_with_decimals():
    """Test du calcul avec des nombres décimaux."""
    result = calculate("5.5 + 2.5")
    assert result == 8.0, f"Expected 8.0 but got {result}"


def test_calculate_empty_expression():
    """Test avec une expression vide - doit lever une erreur."""
    with pytest.raises(ValueError, match="empty expression"):
        calculate("")


def test_calculate_none():
    """Test avec None - doit lever une erreur."""
    with pytest.raises(ValueError, match="empty expression"):
        calculate(None)


def test_calculate_no_operator():
    """Test avec une expression sans opérateur - doit lever une erreur."""
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("123")


def test_calculate_multiple_operators():
    """Test avec plusieurs opérateurs - doit lever une erreur."""
    with pytest.raises(ValueError, match="only one operator is allowed"):
        calculate("5 + 3 + 2")


def test_calculate_operator_at_start():
    """Test avec l'opérateur au début - doit lever une erreur."""
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("+ 5")


def test_calculate_operator_at_end():
    """Test avec l'opérateur à la fin - doit lever une erreur."""
    with pytest.raises(ValueError, match="invalid expression format"):
        calculate("5 +")


def test_calculate_invalid_operand():
    """Test avec un opérande invalide - doit lever une erreur."""
    with pytest.raises(ValueError, match="operands must be numbers"):
        calculate("abc + 3")