# Python - Server-Side Rendering

## Description

Ce projet couvre le rendu côté serveur (SSR) avec Python. L'objectif est de générer du HTML dynamiquement sur le serveur à partir de données, plutôt que de laisser le navigateur le faire côté client.

## C'est quoi le Server-Side Rendering ?

Quand tu visites une page web, il y a deux façons de générer le HTML :

- **Client-Side Rendering (CSR)** : le serveur envoie une page HTML vide, et JavaScript dans le navigateur construit le contenu dynamiquement.
- **Server-Side Rendering (SSR)** : le serveur génère lui-même le HTML complet avec les données dedans, et envoie une page déjà prête au navigateur.

Le SSR est plus rapide à afficher pour l'utilisateur et meilleur pour le référencement (SEO).

## Technologies utilisées

- **Python 3**
- **Flask** — micro-framework web Python pour créer des routes et gérer les requêtes HTTP
- **Jinja2** — moteur de templates intégré à Flask pour générer du HTML dynamique

## Concepts clés

### Routes Flask

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Bonjour le monde !'
```

Une route, c'est une URL (`/`, `/about`, `/users`) associée à une fonction Python qui retourne une réponse HTTP.

### Templates Jinja2

Au lieu de retourner du texte brut, on retourne un fichier HTML avec des variables dedans :

```python
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', nom='Madian')
```

Dans le fichier `templates/index.html` :

```html
<h1>Bonjour {{ nom }} !</h1>
```

`{{ nom }}` sera remplacé par `"Madian"` côté serveur avant d'envoyer la page au navigateur.

### Syntaxe Jinja2 essentielle

```html
<!-- Afficher une variable -->
{{ ma_variable }}

<!-- Condition -->
{% if age >= 18 %}
  <p>Majeur</p>
{% else %}
  <p>Mineur</p>
{% endif %}

<!-- Boucle -->
{% for item in liste %}
  <p>{{ item }}</p>
{% endfor %}
```

### Passer des données au template

```python
@app.route('/utilisateurs')
def utilisateurs():
    users = ['Alice', 'Bob', 'Charlie']
    return render_template('users.html', users=users)
```

Les données (liste, dictionnaire, objet) sont passées en paramètres de `render_template` et accessibles directement dans le template avec Jinja2.

### Lire des données depuis un fichier JSON

```python
import json

with open('data.json') as f:
    data = json.load(f)

return render_template('index.html', data=data)
```

### Lire des données depuis un fichier CSV

```python
import csv

with open('data.csv') as f:
    reader = csv.DictReader(f)
    data = list(reader)

return render_template('index.html', data=data)
```

## Structure du projet

```
projet/
├── app.py               ← fichier principal Flask
├── templates/           ← fichiers HTML avec Jinja2
│   ├── index.html
│   └── users.html
├── static/              ← fichiers CSS, JS, images
│   └── style.css
└── data.json            ← données statiques (si utilisées)
```

## Lancer l'application

```bash
pip install flask
python app.py
```

Puis ouvrir `http://localhost:5000` dans le navigateur.

## Requirements

- Python 3.x
- Flask
- Pas de framework CSS obligatoire
- Les templates doivent être dans le dossier `templates/`

## Auteur

Madian Limadi