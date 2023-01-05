import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
mycursor.execute(
    "CREATE TABLE Trainer (trainer_name varchar(50), age int, team char(10), tainer_id int NOT NULL PRIMARY KEY AUTO_INCREMENT, pk_id int, FOREIGN KEY (pk_id) REFERENCES Pokemon(id))")


mycursor.execute("DESCRIBE Trainer")
for i in mycursor:
    print(i)

