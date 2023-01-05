import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
mycursor.execute("SELECT * FROM Pokemon p NATURAL JOIN Trainer t")
for i in mycursor:
    print(i)