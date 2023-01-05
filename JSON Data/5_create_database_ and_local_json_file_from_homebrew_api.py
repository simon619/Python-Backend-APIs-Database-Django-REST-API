import mysql.connector
from datetime import datetime
import requests
import json

# https://github.com/DetainedDeveloper/Pokedex
# db = mysql.connector.connect(host="localhost", user="root", password="pwroot")
#
# mycursor = db.cursor()
# mycursor.execute("CREATE DATABASE Homebrew_Packages_DB")

db = mysql.connector.connect(host="localhost", user="root", password="pwroot", database="Homebrew_Packages_DB")

mycursor = db.cursor()
mycursor.execute("CREATE TABLE Packages (id int PRIMARY KEY AUTO_INCREMENT, package_name varchar(50), description varchar(200), url char(150), requirements char(200), created datetime not null, install_on_request_30days int, install_on_request_90days int, install_on_request_365days int)")

mycursor.execute("DESCRIBE Packages")

for i in mycursor:
    print(i)

# mycursor.execute("DROP TABLE Packages")
# db.commit()


r = requests.get('https://formulae.brew.sh/api/formula.json')  # All packages
all_packages_info_json = r.json()

all_package_info_str = json.dumps(all_packages_info_json, indent=2)

results = []
# number = len(all_packages_info_json) - (len(all_packages_info_json) - 30)
for i in range(len(all_packages_info_json)):
    current_package_name = all_packages_info_json[i]['name']
    print(current_package_name)

    current_url = f'https://formulae.brew.sh/api/formula/{current_package_name}.json'
    req = requests.get(current_url)
    current_package_json = req.json()

    package_desc = current_package_json['desc']
    package_url = current_package_json['urls']['stable']['url']
    temp_req = current_package_json['requirements']
    package_req = ''
    if temp_req:
        for r in temp_req[0].keys():
            if temp_req[0][r] and type(temp_req[0][r]) == 'str':
                package_req += temp_req[0][r] + ', '
    days_30 = current_package_json['analytics']['install_on_request']['30d'][current_package_name]
    days_90 = current_package_json['analytics']['install_on_request']['90d'][current_package_name]
    days_365 = current_package_json['analytics']['install_on_request']['365d'][current_package_name]

    mycursor.execute("INSERT INTO Packages (package_name, description, url, requirements, created, install_on_request_30days, install_on_request_90days, install_on_request_365days) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                     (current_package_name, package_desc, package_url, package_req, datetime.now(), days_30, days_90, days_365))
    db.commit()

    temp_data = {
        'name': current_package_name,
        'dsec': package_desc,
        'url': package_url,
        'requirements': temp_req,
        'analytics': {
            '30d': days_30,
            '90d': days_90,
            '365d': days_365
        }
    }

    results.append(temp_data)

with open('package_data.json', 'w') as file:
    json.dump(results, file, indent=2)
print('done')


