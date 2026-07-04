#!/usr/bin/env python3
"""
Flask application to display data from JSON and CSV files
"""

from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)


def read_json_file(file_path):
    """Reads a JSON file and returns a list of products"""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_file(file_path):
    """Reads a CSV file and returns a list of products"""
    products = []
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
        return products
    except (FileNotFoundError, csv.Error, ValueError, KeyError):
        return []


@app.route('/products')
def display_products():
    """Display products from JSON or CSV with optional ID filter"""
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Check if source is provided
    if source is None:
        return render_template('product_display.html', 
                             error="Source parameter is required", 
                             products=None)
    
    # Check if source is valid
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                             error="Wrong source", 
                             products=None)
    
    # Read data based on source
    if source == 'json':
        file_path = os.path.join(os.path.dirname(__file__), 'products.json')
        products = read_json_file(file_path)
    else:  # source == 'csv'
        file_path = os.path.join(os.path.dirname(__file__), 'products.csv')
        products = read_csv_file(file_path)
    
    # Check if products were loaded
    if not products:
        return render_template('product_display.html', 
                             error="No products found", 
                             products=None)
    
    # Filter by ID if provided
    if product_id is not None:
        try:
            product_id = int(product_id)
            filtered = [p for p in products if p['id'] == product_id]
            if not filtered:
                return render_template('product_display.html', 
                                     error="Product not found", 
                                     products=None)
            products = filtered
        except ValueError:
            return render_template('product_display.html', 
                                 error="Invalid ID format", 
                                 products=None)
    
    return render_template('product_display.html', 
                         error=None, 
                         products=products)


@app.route('/')
def home():
    """Home page"""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
EOF