import json

with open('pokemon_data.json') as f:
    data = json.load(f)

print(type(data))
print('----------------------------------------------------')

for pk in data['pokemon']:
    print(pk['name'], pk['weight_in_kg'])
    