#!/usr/bin/python3
"""
Flask application extending product data display to include SQLite
"""
import csv
import json
import sqlite3
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
    products_list = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products_list.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except (FileNotFoundError, KeyError, ValueError):
        pass
    return products_list


def read_sql(product_id=None):
    """Reads data from products.db and filters by id if provided"""
    products_list = []
    try:
        conn = sqlite3.connect('products.db')
        # Permet d'accéder aux colonnes par leur nom comme un dictionnaire
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if product_id is not None:
            cursor.execute(
                'SELECT id, name, category, price FROM Products WHERE id = ?',
                (product_id,)
            )
        else:
            cursor.execute('SELECT id, name, category, price FROM Products')

        rows = cursor.fetchall()
        for row in rows:
            products_list.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
    except sqlite3.Error:
        pass
    return products_list


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Cas limite 1 : Source invalide (on accepte maintenant 'sql')
    if source not in ['json', 'csv', 'sql']:
        return render_template(
            'product_display.html',
            error="Wrong source"
        )

    # Conversion de l'ID si présent
    target_id = None
    if product_id is not None:
        try:
            target_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html',
                error="Product not found"
            )

    # Récupération des données selon la source choisie
    if source == 'json':
        products_list = read_json()
        if target_id is not None:
            products_list = [p for p in products_list if p['id'] == target_id]
    elif source == 'csv':
        products_list = read_csv()
        if target_id is not None:
            products_list = [p for p in products_list if p['id'] == target_id]
    elif source == 'sql':
        products_list = read_sql(target_id)

    # Cas limite 2 : L'ID est fourni mais aucun produit ne correspond
    if product_id is not None and not products_list:
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
