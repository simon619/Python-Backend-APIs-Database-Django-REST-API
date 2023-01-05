import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
print("LEFT Outer Join")
mycursor.execute("SELECT * FROM Pokemon p LEFT JOIN Trainer t ON t.pk_id = p.id")
for i in mycursor:
    print(i)

print('')
print("RIGHT Outer Join")
mycursor.execute("SELECT * FROM Pokemon p RIGHT JOIN Trainer t ON t.pk_id = p.id")
for i in mycursor:
    print(i)