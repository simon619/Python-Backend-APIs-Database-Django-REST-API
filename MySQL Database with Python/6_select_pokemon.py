import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()

print("All Data")
mycursor.execute("SELECT * FROM Pokemon")

for i in mycursor:
    print(i)

print()
print("Only fire types")
mycursor.execute("SELECT * FROM Pokemon WHERE type = 'Fire'")

for i in mycursor:
    print(i)


print()
print("Only ID desending order")
mycursor.execute("SELECT name, charged_move FROM Pokemon WHERE charged_move = 'Hydro_Pump' ORDER BY id DESC")

for i in mycursor:
    print(i)


print()
print("Weight")
mycursor.execute("SELECT name, charged_move FROM Pokemon WHERE weight_in_kg >= 100 ORDER BY id ASC ")

for i in mycursor:
    print(i)