#!/usr/bin/env python3

# This file is mainly for displaying uom names ("kg", "each") instead of the uom ids (1, 2) when adding new product

def get_uoms(connection):
    cursor = connection.cursor()

    # query to select all values from uom
    query = ("select * from uom")
    cursor.execute(query)

    response = []

    # loop to create a dictionary with the uom id and name then returning it
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response

# returns something similar to this [{'uom_id': 1, 'uom_name': 'kg'}, {'uom_id': 2, 'uom_name': 'each'}]

if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    print(get_uoms(connection))
