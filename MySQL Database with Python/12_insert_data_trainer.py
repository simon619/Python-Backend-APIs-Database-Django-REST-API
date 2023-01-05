import csv

import mysql.connector
import random

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
# mycursor.execute("SELECT COUNT(*) FROM Pokemon")
mycursor.execute("SELECT * FROM Pokemon")
record = mycursor.fetchall()
for i in range(len(record)):
    print(record[i][0])

mycursor.execute("SELECT COUNT(*) FROM Pokemon")
temp_length = mycursor.fetchall()
pokemon_length = temp_length[0][0]

with open('trainer.csv', 'r') as csV_file:
    csv_reader = csv.reader(csV_file)

    for line in csv_reader:
        mycursor.execute("INSERT INTO Trainer (trainer_name, age, team, pk_id) VALUES (%s, %s, %s, %s)", (line[0], line[1], line[2], random.randint(1, pokemon_length + 1)))
        db.commit()






