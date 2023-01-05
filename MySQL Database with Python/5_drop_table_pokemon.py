import mysql.connector
import csv

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
mycursor.execute("DROP TABLE Pokemon")
db.commit()
