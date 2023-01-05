import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
mycursor.execute("ALTER TABLE Pokemon DROP COLUMN weight_in_kg")
