import json

info_string = '''{
    "people" : [
        {
            "name" : "Simon Abhijet Biswas",
            "id" : "546813",
            "email" : ["savi@gmail.com", "savi@yahoo.com"],
            "graduate" : false
        },
        {
            "name" : "Sharia Rahman Susmoy",
            "id" : "986161",
            "email" : null,
            "graduate" : true
        }       
    ]
}
'''

# JSON to python
data = json.loads(info_string)
print(data)
print(type(data))
print('----------------------------------------------------')

print(data['people'])
print('----------------------------------------------------')

for i in data["people"]:
    print(i['email'])
print('----------------------------------------------------')

# Change value of email
for i in data['people']:
    if not i['email']:
        i['email'] = 'defaultemail@gamil.com'

print(data['people'])
print('----------------------------------------------------')

# Python to json
new_info_string = json.dumps(data, indent=2)
print(new_info_string)
print('----------------------------------------------------')