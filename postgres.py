import psycopg2
import os 
from webscrap import *

host = "localhost"
dbname = "postgres"
user = "postgres"
password = "123"

conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

def erase_table():
    cursor.execute("DROP Table Carpet")
    cursor.execute("DROP Table Mirror")
    conn.commit()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Carpet (ID SERIAL PRIMARY KEY , NOM VARCHAR(255), PRIX VARCHAR(30))")
    cursor.execute("CREATE TABLE IF NOT EXISTS Mirror (ID SERIAL PRIMARY KEY, NOM VARCHAR(255), PRIX VARCHAR(30))")
    conn.commit()

def insert_info():
    carpet_sql = "INSERT INTO Carpet (NOM, PRIX) VALUES (%s,%s)"
    carpet_valeur = c.zip_list_carpet()
    cursor.executemany(carpet_sql, carpet_valeur)
    
    mirror_sql = "INSERT INTO Mirror (NOM, PRIX) VALUES (%s,%s)"
    mirror_valeur = m.zip_list_mirror()
    cursor.executemany(mirror_sql, mirror_valeur)

    conn.commit()

erase_table()
create_table()
insert_info()

cursor.close()
conn.close()