import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
mycursor.execute("SELECT p.name, p.type, t.trainer_name, t.team FROM Pokemon p CROSS JOIN Trainer t")
for i in mycursor:
    print(i)