import mysql.connector
from datetime import datetime
import csv

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="DjangoRESTDB")

mycursor = db.cursor()
# mycursor.execute("CREATE TABLE Pokemon (name varchar(50), type char(10), fast_move char(20), charged_move char(20), created datetime not null, id int PRIMARY KEY AUTO_INCREMENT)")

with open('pokemon.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    count = 1
    for line in csv_reader:
        mycursor.execute("INSERT INTO pokemonapp_pokemon (pokemon_id, pokemon_name, type, fast_move, charged_move, created) VALUES (%s, %s, %s, %s, %s, %s)",
                         (count, line[0], line[1], line[2], line[3], datetime.now()))
        db.commit()
        count += 1

mycursor.execute("SELECT * FROM pokemonapp_pokemon")

for i in mycursor:
    print(i)
