import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")
mycursor = db.cursor()

mycursor.execute("SELECT name, charged_move, id FROM Pokemon WHERE type = 'Grass' GROUP BY name ORDER BY id")
for i in mycursor:
    print(i)

mycursor.execute("SELECT COUNT(id), charged_move FROM Pokemon GROUP BY charged_move ORDER BY COUNT(id) DESC")
for i in mycursor:
    print(i)

mycursor.execute("SELECT COUNT(name) AS Flamethrower FROM Pokemon WHERE charged_move = 'Flamethrower'")
for i in mycursor:
    print(i)
