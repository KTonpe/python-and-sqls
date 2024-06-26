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

def alter_customer_table():
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
    val = [("Kaustubh", "MIG 1"),("Jaikar", "MIG 2")]
    mycursor.executemany(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def insert_at_lastrow():
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("Aditi", "BHEL")
    mycursor.execute(sql, val)

    mydb.commit()

    #add at last row in the table
    print("1 record inserted, ID:", mycursor.lastrowid)

def select_all_from_table():
    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def select_only_one_row(): # print only 1ST ROW use fetchone() method
    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchone()

    print(myresult)

def select_by_only_location():
    sql = "SELECT * FROM customers WHERE address ='BHEL'"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def select_by_like_location(): # use LIKE '%xyz%' keyword
    sql = "SELECT * FROM customers WHERE address LIKE '%MIG%'"

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def select_by_specific_location():
    sql = "SELECT * FROM customers WHERE address = %s"
    adr = ("MIG 1", )

    mycursor.execute(sql, adr)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

def delete_by_specific_record():
    sql = "DELETE FROM customers WHERE id = %s"
    name = ("1", )

    mycursor.execute(sql,name)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

def drop_the_table(): # IF Exist is COMPULSORY
    mycursor = mydb.cursor()

    sql = "DROP TABLE IF EXISTS customers"

    mycursor.execute(sql)

if __name__ == "__main__":
    '''
    create_database()
    show_database()
    create_table()
    show_table()
    alter_customer_table()
    insert_into_table()
    insert_many_into_table()
    insert_at_lastrow()
    select_all_from_table()
    select_only_one_row() # 1st Row
    select_by_only_location()
    select_by_like_location()
    select_by_specific_location()
    delete_by_specific_record()
    drop_the_table()
    '''


