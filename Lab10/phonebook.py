import psycopg2
import csv

# connection instance
conn = psycopg2.connect(database = "PhoneBook",
                        user = "postgres",
                        host = "localhost",
                        password = "Tam-47-lan")

# open a cursor to perform database operations
cur = conn.cursor()

# execute command: create a table
cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL);
            """)

def insert_csv(filename):
   with open(filename, "r") as csvfile:
      csvreader = csv.reader(csvfile, delimiter=",")
      _ = next(csvreader)
      for row in csvreader:
         name, phone = row
         cur.execute("INSERT INTO users (name, phone) VALUES (%s, %s)", (name, phone))

def insert():
   name = input("Name: ")
   phone = input("Phone: ")
   cur.execute("INSERT INTO users (name, phone) VALUES (%s, %s)", (name, phone))

# insert data
insert_csv("phonebook.csv")
insert()

# update data
cur.execute("UPDATE users SET phone = %s WHERE name = %s", ("87771112233", "Tamerlan"))

# query data
cur.execute("SELECT * FROM users WHERE name LIKE 'T%'")
print(cur.fetchall())

# delete data
cur.execute("DELETE FROM users WHERE name = %s OR phone = %s", ("James", "123"))

# make the changes to the database persistent
conn.commit()

# close cursor and communication with the database
cur.close()
conn.close()