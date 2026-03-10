import pandas as pd
import numpy as np

import psycopg2

import os
from dotenv import load_dotenv, dotenv_values

# load_dotenv()

# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASS = os.getenv("DB_PASS")
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")

config = dotenv_values(".env")

print(config)
DB_NAME = config["DB_NAME"]
DB_USER = config["DB_USER"]
DB_PASS = config["DB_PASS"]
DB_HOST = config["DB_HOST"]
DB_PORT = config["DB_PORT"]

try:
    conn = psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

    print(conn)
    print("Database Connected!")

    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM customers;
     """)
    
    rows = cur.fetchall()

    for data in rows:
        print(f"ID: {data[0]}")
        print(f"Name: {data[1]}")
        print(f"Email: {data[2]}")

    print("-"* 50)
    print(type(rows))
    print(rows)
    print("Data Fetched")

    # INSERT
    query = """ INSERT INTO customers (name, email)
                VALUES ('Tectigon', 'tectigon@email.com'); """

    cur.execute(query)
    conn.commit()

    # SELECT
    cur.execute("SELECT * FROM customers;")

    data1 = cur.fetchone()
    print(data1)

    data2 = cur.fetchone()
    print(data2)

    data3 = cur.fetchmany(3)

    for row in data3:
        print(row)

    data4 = cur.fetchmany(4)

    for row in data4:
        print(row)

except Exception as e:
    print(f"Error: {e}")
finally:
    cur.close()
    conn.close()
    
    print("Conn closed")


# DB_NAME = "JANPython"  # 'Database Name'
# DB_USER =  "postgres" #"Database User"
# DB_PASS =  "admin" # "Database Password"
# DB_HOST =  "localhost" # ose 127.0.0.1 # "Database Host"
# DB_PORT = "5432"