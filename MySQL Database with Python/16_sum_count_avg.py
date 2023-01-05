import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")
mycursor = db.cursor()

mycursor.execute("SELECT AVG(weight_in_kg) FROM Pokemon")
for i in mycursor:
    print(i)
print('')

mycursor.execute("SELECT SUM(weight_in_kg) FROM Pokemon WHERE type = 'Fire'")
for i in mycursor:
    print(i)
print('')

mycursor.execute("SELECT COUNT(name) FROM Pokemon WHERE type = 'Water'")
for i in mycursor:
    print(i)
print('')
