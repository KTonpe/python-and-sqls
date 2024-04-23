import mysql.connector
import json

with open('Apprentices.json') as json_file:
    data = json.load(json_file)


db_connection = mysql.connector.connect(
    host='127.0.0.1',
    port = '3306',
    user='root',
    password='qwerty*123',
    database='apprentice_data'
)

db_cursor = db_connection.cursor()
# db_cursor.execute("CREATE DATABASE trialdatabase")
# db_cursor.execute("CREATE DATABASE IF NOT EXISTS my_database")

db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS apprentices (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        employee_id VARCHAR(255),
        email VARCHAR(255),
        contact VARCHAR(255),
        location VARCHAR(255)
    )
""")

for location, apprentices in data['Apprentices'].items():
    for apprentice in apprentices:
        db_cursor.execute("""
            INSERT INTO apprentices (name, employee_id, email, contact, location)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            apprentice['name'],
            apprentice['employee_id'],
            apprentice['email'],
            apprentice['contact'],
            location
        ))

db_connection.commit()
'''sql = "DROP TABLE IF EXISTS apprentices"
db_cursor.execute(sql)'''

db_cursor.execute("SELECT * FROM apprentices")
myresult = db_cursor.fetchall()
for x in myresult:
    print(x)


# db_cursor.close()
# db_connection.close()


