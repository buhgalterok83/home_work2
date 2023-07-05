import sqlite3

class DatabaseTable:
    def __init__(self, table_name, fields):
        self.table_name = table_name
        self.fields = fields
        self.connection = None
        self.cursor = None

        self.create_table()

    def connect(self):
        if not self.connection:
            self.connection = sqlite3.connect('database.db')
            self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            self.connection = None
            self.cursor = None

    def create_table(self):
        self.connect()
        query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({','.join(self.fields)})"
        self.cursor.execute(query)
        self.connection.commit()
        self.disconnect()

    def get_all_records(self):
        self.connect()
        query = f"SELECT * FROM {self.table_name}"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        self.disconnect()
        return records

    def add_records(self, records):
        self.connect()
        query = f"INSERT INTO {self.table_name} VALUES ({','.join(['?']*len(self.fields))})"
        self.cursor.executemany(query, records)
        self.connection.commit()
        self.disconnect()

    def update_records(self, condition, values):
        self.connect()
        query = f"UPDATE {self.table_name} SET {','.join([f'{field}=?' for field in values.keys()])} WHERE {condition}"
        self.cursor.execute(query, list(values.values()))
        self.connection.commit()
        self.disconnect()

    def get_records_by_condition(self, condition):
        self.connect()
        query = f"SELECT * FROM {self.table_name} WHERE {condition}"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        self.disconnect()
        return records

    def delete_records_by_condition(self, condition):
        self.connect()
        query = f"DELETE FROM {self.table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()
        self.disconnect()
# Создание экземпляра класса для таблицы "users" с полями "id", "name", "email"
table = DatabaseTable("users", ["id INTEGER", "name TEXT", "email TEXT"])

# Добавление записей
records_to_add = [(1, "John Doe", "john@example.com"), (2, "Jane Smith", "jane@example.com")]
table.add_records(records_to_add)

# Получение всех записей
all_records = table.get_all_records()
for record in all_records:
    print(record)

# Обновление записей, у которых поле "name" равно "John Doe"
condition = "name = 'John Doe'"
new_values = {"email": "new_email@example.com"}
table.update_records(condition, new_values)

# Получение записей по условию
condition = "name LIKE 'J%'"
filtered_records = table.get_records_by_condition(condition)
for record in filtered_records:
    print(record)

# Удаление записей, у которых поле "email" содержит "example.com"
condition = "email LIKE '%example.com%'"
table.delete_records_by_condition(condition)
