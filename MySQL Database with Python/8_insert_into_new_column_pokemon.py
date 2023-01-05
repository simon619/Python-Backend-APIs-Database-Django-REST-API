import mysql.connector
import csv

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()

with open('pokemon.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        mycursor.execute("UPDATE Pokemon SET weight_in_kg = (%s) WHERE name = (%s)", (line[4], line[0]))
        db.commit()



