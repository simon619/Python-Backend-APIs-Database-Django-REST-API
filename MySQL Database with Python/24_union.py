import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
mycursor.execute("SELECT t.trainer_name, t.age, 'Under Age' AS Status FROM trainer t WHERE age <= 25 UNION SELECT t.trainer_name, t.age, 'Proper Age' AS Status FROM Trainer t WHERE age > 25")
for i in mycursor:
    print(i)