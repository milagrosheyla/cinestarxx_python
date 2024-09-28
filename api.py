from flask import Flask
from flask_cors import CORS
import mysql.connector 

app = Flask(__name__)
CORS(app)

local = {
    'host' : 'localhost',
    'user' : 'root',
    'database' : 'cinestar'
}

hostinger = {
    'host' : 'srv1467.hstgr.io',
    'user' : 'u719737586_cinestar',
    'password' : 'Senati2024@',
    'database' : 'u719737586_cinestar'
}

cnx = mysql.connector.connect(**hostinger)
cursor = cnx.cursor(dictionary=True)


@app.route("/cines")
def cines():
    return  "cines"

@app.route("/peliculas")
def peliculas():
    return  "peliculas"


if __name__ == "__main__":
    app.run(debug=True)
