import psycopg2

conn = psycopg2.connect(database = "PhoneBook",
                        user = "postgres",
                        host = "localhost",
                        password = "Tam-47-lan")

cur = conn.cursor()

# creates table 'users' if not exists
cur.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) NOT NULL);
            """)

# creates a function, that retrieves data from 'users'
cur.execute("""               
            CREATE OR REPLACE FUNCTION fetch_data(pattern VARCHAR(50))
            RETURNS TABLE (user_id INTEGER, name VARCHAR(50), phone VARCHAR(20))
            AS
            $$
            BEGIN
	            RETURN QUERY
	            SELECT * FROM users WHERE users.name LIKE '%' || pattern || '%' 
               OR users.phone LIKE '%' || pattern || '%';
            END;
            $$
            LANGUAGE plpgsql;
            """)

# creates a procedure, that deletes data from table by name or phone
cur.execute("""
            CREATE OR REPLACE PROCEDURE delete_data(value VARCHAR(50))
            AS
            $$
            BEGIN
               DELETE FROM users WHERE users.name = value OR users.phone = value;
            END;
            $$
            LANGUAGE plpgsql;
            """)

# creates a procedure, that insert data or updates it
cur.execute("""
            CREATE OR REPLACE PROCEDURE change_data(name_to_add VARCHAR(50), phone_to_add VARCHAR(20))
            AS
            $$
            BEGIN
               IF EXISTS (SELECT 1 FROM users WHERE users.name = name_to_add) THEN
                  UPDATE users SET phone = phone_to_add WHERE users.name = name_to_add;
               ELSE
                  INSERT INTO users (name, phone) VALUES (name_to_add, phone_to_add);
               END IF;
            END;
            $$
            LANGUAGE plpgsql;
            """)

# retrieves data from fetch_data()
pattern = input("Pattern: ")
cur.execute("SELECT * FROM fetch_data(%s)", (pattern,))
print(cur.fetchall())

# calls delete_data()
value = input("Value: ")
cur.execute("CALL delete_data(%s)", (value,))

# calls change_data()
name_to_add = input("Name: ")
phone_to_add = input("Phone: ")
cur.execute("CALL change_data(%s, %s)", (name_to_add, phone_to_add))

conn.commit()

cur.close()
conn.close()