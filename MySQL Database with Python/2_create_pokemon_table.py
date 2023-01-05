import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
mycursor.execute("CREATE TABLE Pokemon (name varchar(50), type char(10), fast_move char(20), charged_move char(20), created datetime not null, id int PRIMARY KEY AUTO_INCREMENT)")