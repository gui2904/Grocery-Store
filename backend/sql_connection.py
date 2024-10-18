#!/usr/bin/env python3

import mysql.connector

# global variable to create connection, because if function is called multiple times, there will be multiple connections.
__cnx = None

def get_sql_connection():
    global __cnx

    # if there is no connection, then create one and return.
    if __cnx is None:

        # creating connection with database.
        __cnx = mysql.connector.connect(user='archie', password='Guigui1243', host='127.0.0.1', database='gs')

    return __cnx
