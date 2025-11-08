# templates/

## Description
Ce dossier contient le fichier HTML de l'interface utilisateur. Flask utilise Jinja2 pour rendre ces templates dynamiques.

## Contenu
**index.html**
- Page principale de la calculatrice
- Contient le formulaire et les boutons de la calculatrice
- Affiche les résultats envoyés par le serveur
- Inclut le JavaScript pour gérer les clics sur les boutons

## Fonctionnement
Flask rend les templates avec `render_template()` :
return render_template('index.html', result=result)


Les variables Python sont accessibles dans le HTML avec la syntaxe Jinja2 :
<input type="text" value="{{ result }}">


## Dépendances
- Flask (système de templates Jinja2)
- `static/style.css` (style visuel)
