import json
import re

users = []
with open('/Users/goncharovvitalii/Downloads/users-3.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        name, age_str, *phones = line.split(';')
        name = name.strip()
        phones = [phone.strip() for phone in phones]

        age = None
        if age_str:
            match = re.match(r'^\d+$', age_str)
            if match:
                age = int(age_str)

        user = {'name': name, 'age': age, 'phones': phones}
        users.append(user)

with open('users_out.json', 'w') as file:
    json.dump(users, file)

with open('users_out.txt', 'w') as file:
    for user in users:
        age = str(user['age']).replace(' ', '') if user['age'] is not None else ''
        phones = ','.join([phone.replace(' ', '') for phone in user['phones']]) if user['phones'] else ''
        file.write(f"{user['name']};{age};{phones}\n")

