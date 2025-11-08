"""
Tests pour les opérations mathématiques du module operators.py

Ce fichier teste les quatre opérations de base: addition, soustraction,
multiplication et division.
"""

from operators import add, subtract, multiply, divide


def test_add():
    """Test de l'addition de deux nombres positifs."""
    result = add(5, 3)
    assert result == 8, f"Expected 8 but got {result}"


def test_add_negative():
    """Test de l'addition avec des nombres négatifs."""
    result = add(-5, 3)
    assert result == -2, f"Expected -2 but got {result}"


def test_add_zero():
    """Test de l'addition avec zéro."""
    result = add(5, 0)
    assert result == 5, f"Expected 5 but got {result}"


def test_subtract():
    """Test de la soustraction de deux nombres positifs."""
    result = subtract(10, 3)
    assert result == 7, f"Expected 7 but got {result}"


def test_subtract_negative():
    """Test de la soustraction avec des nombres négatifs."""
    result = subtract(-5, 3)
    assert result == -8, f"Expected -8 but got {result}"


def test_subtract_zero():
    """Test de la soustraction avec zéro."""
    result = subtract(5, 0)
    assert result == 5, f"Expected 5 but got {result}"


def test_multiply():
    """Test de la multiplication de deux nombres positifs."""
    result = multiply(5, 3)
    assert result == 15, f"Expected 15 but got {result}"


def test_multiply_negative():
    """Test de la multiplication avec un nombre négatif."""
    result = multiply(-5, 3)
    assert result == -15, f"Expected -15 but got {result}"


def test_multiply_zero():
    """Test de la multiplication par zéro."""
    result = multiply(5, 0)
    assert result == 0, f"Expected 0 but got {result}"


def test_multiply_one():
    """Test de la multiplication par un."""
    result = multiply(5, 1)
    assert result == 5, f"Expected 5 but got {result}"


def test_divide():
    """Test de la division de deux nombres positifs."""
    result = divide(10, 2)
    assert result == 5.0, f"Expected 5.0 but got {result}"


def test_divide_with_decimal():
    """Test de la division qui donne un résultat décimal."""
    result = divide(10, 3)
    assert abs(result - 3.333) < 0.01, f"Expected ~3.333 but got {result}"


def test_divide_negative():
    """Test de la division avec un nombre négatif."""
    result = divide(-10, 2)
    assert result == -5.0, f"Expected -5.0 but got {result}"


def test_divide_by_one():
    """Test de la division par un."""
    result = divide(5, 1)
    assert result == 5.0, f"Expected 5.0 but got {result}"