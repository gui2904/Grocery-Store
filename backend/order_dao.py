#!/usr/bin/env python3

from datetime import datetime
from sql_connection import get_sql_connection

def insert_order(connection, order):
    cursor = connection.cursor()

    # building the order query, order_data values will substitute the values inside the query.
    order_query = ("insert into orders (customer_name, total, datetime) values (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], datetime.now())

    cursor.execute(order_query, order_data)

    # storing the id of last order.
    order_id = cursor.lastrowid

    # building the query for the order_details, with the products id, quantity and total price.
    order_details_query = ("insert into order_details (order_id, product_id, quantity, total_price) values (%s, %s, %s, %s)")

    # looping through and building the array of orders.
    order_details_data = []
    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])

    cursor.executemany(order_details_query, order_details_data)

    connection.commit()

    return order_id

if __name__ == '__main__':
    connection = get_sql_connection()
    print(insert_order(connection, {
        'customer_name': 'Hulk',
        'grand_total': '500',
        'order_details': [
            {
                'product_id': 2,
                'quantity': 2,
                'total_price': 50
            },
            {
                'product_id': 1,
                'quantity': 1,
                'total_price': 30
            },
        ]
    }))
