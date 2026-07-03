#!/usr/bin/python3
"""
Flask application reading and filtering product data from JSON and CSV files
"""
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json():
    """Reads data from products.json"""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv():
    """Reads data from products.csv"""
    products = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # On convertit l'ID en int et le prix en float pour la cohérence
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except (FileNotFoundError, KeyError, ValueError):
        pass
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Cas limite 1 : Source invalide
    if source not in ['json', 'csv']:
        return render_template(
            'product_display.html',
            error="Wrong source"
        )

    # Chargement des données selon la source
    if source == 'json':
        products_list = read_json()
    else:
        products_list = read_csv()

    # Cas limite 2 : Filtrage par ID si fourni
    if product_id is not None:
        try:
            product_id = int(product_id)
            # Recherche du produit spécifique
            filtered_products = [
                p for p in products_list if p['id'] == product_id
            ]
            if not filtered_products:
                return render_template(
                    'product_display.html',
                    error="Product not found"
                )
            products_list = filtered_products
        except ValueError:
            # Si l'ID passé n'est pas un entier valide
            return render_template(
                'product_display.html',
                error="Product not found"
            )

    return render_template(
        'product_display.html',
        products=products_list
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
