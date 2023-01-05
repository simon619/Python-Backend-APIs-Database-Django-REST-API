import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
mycursor.execute("DESCRIBE Pokemon")

for i in mycursor:
    print(i)