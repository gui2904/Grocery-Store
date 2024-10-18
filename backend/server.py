#!/usr/bin/env python3
import products_dao
import uom_dao
import json
from sql_connection import get_sql_connection
from flask import Flask, request, jsonify

app = Flask(__name__)

# creating connection with database from the server.py
connection = get_sql_connection()

# creating endpoint with method of 'GET', GET is just for getting data
@app.route('/getProducts', methods=['GET'])
def get_products():

    # storing products query aquired from get_all_products method in products_dao file inside var and converting it to JSON
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# display uom names instead of id in the UI, when adding a new product
@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# creating endpoint with method 'POST', POST is for updating data, or deleting in this case
@app.route('/deleteProduct', methods=['POST'])
def delete_product():

    # calls delete_product function from products_dao file with specified product id then stores it in variable
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({'product_id': return_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# creating endpoint to  insert a new order.
@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })

# function to insert product
@app.route('/insertProduct', methods=['POST'])
def insert_product():
    # creating a payload with the data, which will be a parameter that is sent to insert_new_product method in the products_dao file, the data is formed by product_name, uom_id and price_per_unit
    # also converts back from string to json format.
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)
