import mysql.connector

#to connect with existing database
mydb = mysql.connector.connect(
  host="127.0.0.1",
  port = "3306",
  user="root",
  password="qwerty*123",
  database = "mydatabase"
)

#this calls cursor method from mydb which acts as a pointer to the database
mycursor = mydb.cursor()

def create_database():
    #create a database and gives error if the database already exists
    mycursor.execute("CREATE DATABASE trialdatabase")

def show_database():
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x) #this returns a tuple

def create_table():
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

def show_table():
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)

def create_customer_table():
    #customer table already exists so throws an error so use ALTER
    # mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


def insert_into_table():
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)

    #THIS SYNTAX WILL UPDATE THE CHANGES
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def insert_many_into_table():
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = [("Kaus", "MIG 1"),("tubh", "MIG 2")]
    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def insert_at_lastrow():
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("tonpe", "BHEL")
    mycursor.execute(sql, val)

    mydb.commit()

    print("1 record inserted, ID:", mycursor.lastrowid)

if __name__ == "__main__":
    '''
    create_database()
    show_database()
    create_table()
    show_table()
    create_customer_table()
    insert_into_table()
    insert_many_into_table()
    '''
    insert_at_lastrow()