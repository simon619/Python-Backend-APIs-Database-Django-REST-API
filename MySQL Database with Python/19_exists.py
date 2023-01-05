import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
mycursor.execute("SELECT name FROM Pokemon WHERE EXISTS(SELECT trainer_name FROM Trainer WHERE Trainer.pk_id = Pokemon.id)")

print("EXISTS")
for i in mycursor:
    print(i)

print("ANY")
mycursor = db.cursor()
mycursor.execute("SELECT name FROM Pokemon WHERE id = ANY (SELECT pk_id FROM Trainer WHERE age >= 32)")
for i in mycursor:
    print(i)

print("ALL")
mycursor.execute("SELECT name FROM Pokemon WHERE id > ALL (SELECT pk_id FROM Trainer WHERE age >= 32)")
for i in mycursor:
    print(i)
