import requests
import json

# All Package Information
r = requests.get('https://formulae.brew.sh/api/formula.json')  # All packages
all_packages_info_json = r.json()
print(type(all_packages_info_json))  # list type
print('----------------------------------------------------')
print('')

all_package_info_str = json.dumps(all_packages_info_json, indent=2)
# print(all_package_info_str)
print(type(all_package_info_str))  # list type
print('----------------------------------------------------')
print('')

# Information on a single package
package_name = all_packages_info_json[0]['name']
any_package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'

r = requests.get(any_package_url)
single_package_json = r.json()

single_first_package_info_str = json.dumps(single_package_json, indent=2)
print(single_first_package_info_str)
print('----------------------------------------------------')
print('')

# Name of all the packages
all_packages_name = []
for i in range(len(all_packages_info_json)):
    all_packages_name.append(all_packages_info_json[i]['name'])
print(f'package_name: {all_packages_name}')
print('----------------------------------------------------')
print('')

# Information of a single pack
# Single pack information
package_info = []
for i in all_packages_info_json[0].keys():
    package_info.append(i)
print(f'Package Info: {package_info}')
print('----------------------------------------------------')
print('')

# Information of python
python_info = []
for i in range(len(all_packages_info_json)):
    if all_packages_info_json[i]['name'] == 'a2ps':
        python_info = [i for i in all_packages_info_json[i].keys()]
print(f'python_info: {python_info}')
print('----------------------------------------------------')
print('')

# Find the installed data
for i in range(len(all_packages_info_json)):
    current_package_name = all_packages_info_json[i]['name']
    current_package_description = all_packages_info_json[i]['desc']

    current_url = f'https://formulae.brew.sh/api/formula/{current_package_name}.json'
    req = requests.get(current_url)
    current_package_json = req.json()

    installed_30days = current_package_json['analytics']['install_on_request']['30d'][current_package_name]
    installed_90days = current_package_json['analytics']['install_on_request']['90d'][current_package_name]
    installed_365days = current_package_json['analytics']['install_on_request']['365d'][current_package_name]

    print(f"name: {current_package_name}, description: {current_package_name}, installed_on_request: 30days: {installed_30days}, 90days: {installed_90days}, 365days: {installed_365days}")








