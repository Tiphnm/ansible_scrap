from main import *
from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

host = "localhost"
dbname = "postgres"
user = "tiphaineminguet"

conn_string = "host={0} user={1} dbname={2}".format(host, user, dbname)
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

@app.route('/home_page')
def welcome(): 
    return "Welcome to Maison Du Monde's API ! "    

@app.route('/api')
def api():
    cursor.execute("SELECT * FROM Carpet, Mirror WHERE Carpet.ID = Mirror.ID ORDER BY Carpet.ID")
    output = cursor.fetchall()
    return jsonify(output)

@app.route('/api_carpet')
def api_carpet(): 
    cursor.execute("SELECT * FROM Carpet")
    output = cursor.fetchall()
    return jsonify(output)

@app.route('/api_mirror')
def api_mirror(): 
    cursor.execute("SELECT * FROM Mirror")
    output = cursor.fetchall()
    return jsonify(output)

@app.route('/api_carpet_price')
def ranking_price_carpet(): 
    #http://http://localhost:4050/api_carpet_price?PRIX=200

    carpet_price = request.args.get("PRIX")

    cursor.execute("SELECT * FROM Carpet WHERE PRIX <= ('%s')" %(carpet_price))
    #print(result)
    output = cursor.fetchall()
    #print(output)
    return jsonify(output)

@app.route('/api_mirror_price')
def ranking_price_mirror(): 
    #http://http://localhost:4050/api_mirror_price?PRIX=200

    mirror_price = request.args.get("PRIX")

    cursor.execute("SELECT * FROM Mirror WHERE PRIX <= ('%s')" %(mirror_price))
    output = cursor.fetchall()
    return jsonify(output)

if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=3050, debug = True)