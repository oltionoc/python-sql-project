import psycopg2


class PostgresDB:
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        self.conn = {
            "dbname": dbname,
            "user": user,
            "password": password,
            "host": host,
            "port": port
        }

    def get_connecetion(self):
        return psycopg2.connect(**self.conn)

    def execute_select(self, query, parmas=None):
        with psycopg2.connect(**self.conn) as conn:
            with conn.cursor() as cur:
                cur.execute(query, parmas)
                return cur.fetchall()
            
    def execute_modify(self, query, params=None):
        with psycopg2.connect(**self.conn) as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                conn.commit()
                return cur.rowcount