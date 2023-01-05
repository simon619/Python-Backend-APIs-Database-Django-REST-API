import mysql.connector
from datetime import datetime
import csv
import random

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="DjangoRESTDB")

mycursor = db.cursor()
# mycursor.execute(
#     "CREATE TABLE Trainer (trainer_name varchar(50), age int, team char(10), trainer_id int NOT NULL PRIMARY KEY AUTO_INCREMENT, pk_id int, FOREIGN KEY (pk_id) REFERENCES Pokemon(id))")

mycursor.execute("SELECT COUNT(*) FROM pokemonapp_pokemon")
temp_length = mycursor.fetchall()
pokemon_length = temp_length[0][0]

with open('trainer.csv', 'r') as csV_file:
    csv_reader = csv.reader(csV_file)
    
    count = 1
    for line in csv_reader:
        mycursor.execute("INSERT INTO pokemonapp_trainer (trainer_id, trainer_name, team, poke_id, age) VALUES (%s, %s, %s, %s, %s)", (count, line[0], line[2], random.randint(1, pokemon_length), line[1]))
        db.commit()
        count += 1

mycursor.execute("SELECT * FROM pokemonapp_trainer")

for i in mycursor:
    print(i)
