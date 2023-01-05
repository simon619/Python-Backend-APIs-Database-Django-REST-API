import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
print("Example 1")
mycursor.execute("SELECT * FROM Pokemon JOIN Trainer ON Pokemon.id = Trainer.pk_id")
for i in mycursor:
    print(i)

print("Example 2")
mycursor.execute("SELECT p.name, p.type, t.trainer_name, p.id, t.tainer_id FROM Trainer t JOIN Pokemon p ON p.id = t.pk_id")
for i in mycursor:
    print(i)

