from postgres import PostgresDB

from dotenv import dotenv_values

import pandas as pd

config = dotenv_values(".env")

#print(config)
DB_NAME = config["DB_NAME"]
DB_USER = config["DB_USER"]
DB_PASS = config["DB_PASS"]
DB_HOST = config["DB_HOST"]
DB_PORT = config["DB_PORT"]

# -- Kerkesat
# -- Shfaq te gjithe klientet
def show_all_customers(db):
    results = db.execute_select("SELECT * FROM customers;")
    for row in results:
        print(row)

# -- Shfaq te gjithe produktet me çmimin > 20€
def products_above_price(db, limit=20):
    query = f""" SELECT * FROM products WHERE price > {limit} """
    results = db.execute_select(query)
    for row in results: print(row)

# -- Ndrysho çmimin e “Mouse” ne 25€
def update_mouse_price(db):
    query = """ UPDATE products SET price = 25.00 WHERE name = 'Mouse' """
    db.execute_modify(query)

# --Fshi produktet e kategorise “Food” me çmim < 4€
def delete_food(db):
    query = """ DELETE FROM products WHERE category = 'Food' AND price < 4; """
    db.execute_modify(query)

# --Gjej te gjitha porosite me emrin e klientit
def items_per_order(db):
    query = """ SELECT 
                    order_id, 
                    SUM(quantity) 
                FROM order_items 
                    GROUP BY order_id;  """
    
    results = db.execute_select(query)
    for row in results: print(row)

# --Gjej sa artikuj ka çdo porosi
def orders_with_name(db):
    query = """
            SELECT 
                o.id,
                c.name,
                o.order_date
            FROM orders o
            JOIN customers c ON o.customer_id = c.id
    """
    results = db.execute_select(query)
    for row in results: print(row)

# --Gjej totalin (ne euro) te çdo porosie
def order_totals(db):
    query = """
            SELECT oi.order_id, SUM(oi.quantity * p.price) as total
            FROM order_items oi
            JOIN products p ON oi.product_id = p.id
            GROUP BY oi.order_id;
    """
    results = db.execute_select(query)
    for row in results: print(row)


def get_ardit_spending(db):
    query = """
            SELECT
                c.name,
                SUM(oi.quantity * p.price) as total
            FROM customers c
            JOIN orders o ON c.id = o.customer_id
            JOIN order_items oi ON o.id = oi.order_id
            JOIN products p ON oi.product_id = p.id
           -- WHERE c.name = 'Ardit'
            GROUP BY c.name;
        """
    with db.get_connecetion()as conn:
        df = pd.read_sql(query, conn)

        print(df.head())
        print(df.info())
        print(df.shape)

    return df

# --Gjej klientin me me shume porosi
# --Shfaq 3 produktet me te shtrenjta
# --Gjej totalin e shpenzimeve te klientit “Ardit”
# --Numero sa produkte ka ne çdo kategori
# --Shfaq klientet qe nuk kane bere asnje porosi


if __name__ == "__main__":
    try:
        client = PostgresDB(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )

        get_ardit_spending(client)

        #show_all_customers(client)
        #products_above_price(client, limit=50)
        #update_mouse_price(client)
        #delete_food(client)
        #orders_with_name(client)
        #order_totals(client)


        
    except Exception as e:
        print("Error")
        raise