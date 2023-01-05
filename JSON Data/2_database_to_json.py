import csv
import mysql.connector
import json

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="PokemonDB")

mycursor = db.cursor()
mycursor.execute("SELECT * FROM Pokemon")
pk_records = mycursor.fetchall()
mycursor.execute("SELECT * FROM Trainer")
tr_records = mycursor.fetchall()

pokemon_info_dic = {'pokemon': [], 'trainer': []}
for i in range(len(pk_records)):
    temp_dic = {'name': pk_records[i][0], 'type': pk_records[i][1], 'fast_move': pk_records[i][2],
                'charged_move': pk_records[i][3], 'created': str(pk_records[i][4]), 'id': pk_records[i][5],
                'weight_in_kg': pk_records[i][6]}
    pokemon_info_dic['pokemon'].append(temp_dic)

for i in range(len(tr_records)):
    temp_dic = {'trainer_name': tr_records[i][0], 'team': tr_records[i][1], 'tainer_id': tr_records[i][2],
                'pk_id': tr_records[i][3]}
    pokemon_info_dic['trainer'].append(temp_dic)

pokemon_info_json = json.dumps(pokemon_info_dic, indent=2)
print(pokemon_info_json)

with open('pokemon_data.json', 'w') as file:
    json.dump(pokemon_info_dic, file, indent=2)

