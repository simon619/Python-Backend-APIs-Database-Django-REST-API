import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
mycursor.execute("SELECT weight_in_kg FROM Pokemon AS KG WHERE weight_in_kg > (SELECT avg(weight_in_kg) FROM Pokemon)")
for i in mycursor:
    print(i)
