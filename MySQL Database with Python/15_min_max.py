import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")
mycursor = db.cursor()

mycursor.execute("SELECT MIN(weight_in_kg) FROM Pokemon WHERE type = 'Fire'")
for i in mycursor:
    print(i)
print('')

mycursor.execute("SELECT MAX(weight_in_kg) AS heavy_weight_water FROM Pokemon WHERE type = 'Water'")
for i in mycursor:
    print(i)
print('')