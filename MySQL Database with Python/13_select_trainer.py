import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
mycursor.execute("SELECT * FROM Trainer WHERE team = 'Valor'")
for i in mycursor:
    print(i)

