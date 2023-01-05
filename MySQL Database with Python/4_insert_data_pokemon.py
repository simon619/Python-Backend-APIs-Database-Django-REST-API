import mysql.connector
import csv
from datetime import datetime

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
with open('pokemon.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        mycursor.execute("INSERT INTO Pokemon (name, type, fast_move, charged_move, created) VALUES (%s,%s,%s,%s,%s)",
                         (line[0], line[1], line[2], line[3], datetime.now()))
        db.commit()

mycursor.execute("SELECT * FROM Pokemon")

for i in mycursor:
    print(i)


