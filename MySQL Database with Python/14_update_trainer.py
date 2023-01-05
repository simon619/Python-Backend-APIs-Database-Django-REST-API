import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")
mycursor = db.cursor()
mycursor.execute("UPDATE Trainer SET pk_id = 6 WHERE tainer_id = 1")
db.commit()

