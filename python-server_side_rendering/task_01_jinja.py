#!/usr/bin/env python3
"""
Application Flask basique avec templating Jinja
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Route de la page d'accueil"""
    return render_template('index.html')


@app.route('/about')
def about():
    """Route de la page À propos"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Route de la page Contact"""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)