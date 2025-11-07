"""
app.py - Application Flask de la calculatrice web

Ce fichier contient le serveur principal qui fait tourner la calculatrice.
Il gère l'affichage de la page web et calcule les résultats.

Contenu:
- Route / : affiche la calculatrice et traite les calculs
- Fonction calculate() : évalue les expressions
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Dictionnaire pour lier chaque symbole à sa fonction
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Calcule une expression avec deux nombres et un opérateur.
    
    Args:
        expr (str): L'expression entrée (ex: "10 + 5")
    
    Returns:
        float: Le résultat du calcul
    
    Raises:
        ValueError: Si l'expression est vide, mal écrite ou invalide
    """
    
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # On enlève les espaces pour simplifier l'analyse
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # On cherche où est l'opérateur dans la chaîne
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # L'opérateur doit être entre deux nombres (pas au début/fin)
    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    # On sépare en deux parties: avant et après l'opérateur
    left = s[:op_pos]
    right = s[op_pos+1:]

    # On convertit les textes en nombres
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # On appelle la bonne fonction selon l'opérateur trouvé
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Page principale de la calculatrice.
    
    GET: Affiche juste la page vide
    POST: Récupère l'expression, calcule et affiche le résultat
    """
    
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Lance le serveur en mode debug (utile pour voir les erreurs)
    app.run(debug=True)
