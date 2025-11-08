## static/

## Description
Ce dossier contient les fichiers statiques de l'application. Ces fichiers définissent l'apparence et le style visuel de la calculatrice.

## Contenu
**style.css**
- Feuille de style principale de la calculatrice
- Définit les couleurs, la mise en page et le style des boutons
- Inclut les effets de survol et les animations

## Fonctionnement
Flask sert automatiquement les fichiers de ce dossier. Pour les référencer dans le HTML, on utilise :
html<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

## Dépendances
Aucune dépendance externe. Le CSS utilisé est standard et compatible avec tous les navigateurs modernes.
