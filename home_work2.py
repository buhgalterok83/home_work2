import json
import re

users = []
with open('/Users/goncharovvitalii/Downloads/users-3.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        fields = [field.strip() for field in line.split(';')]
        name = fields[0]

        age = None
        if len(fields) > 1 and fields[1]:
            try:
                age = int(fields[1])
            except (ValueError, TypeError):
                pass

        phones = []
        if len(fields) > 2 and fields[2]:
            phones = [phone.strip() for phone in fields[2].split(',')]

        user = {'name': name, 'age': age, 'phones': phones}
        users.append(user)

with open('users_out.json', 'w') as file:
    json.dump(users, file)

with open('users_out.txt', 'w') as file:
    for user in users:
        age = str(user['age']) if user['age'] is not None else ''
        phones = ','.join(user['phones']) if user['phones'] else ''
        file.write(f"{user['name']};{age};{phones}\n")
