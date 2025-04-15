import psycopg2

# connection instance
conn = psycopg2.connect(database = "SnakeGame",
                        user = "postgres",
                        host = "localhost",
                        password = "Tam-47-lan")

# open a cursor to perform database operations
cur = conn.cursor()

# execute command: create a table
cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL
            );

            CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            level INTEGER,
            score INTEGER
            );
            """)

def get_or_create_user(cur, username):
   cur.execute("SELECT id FROM users WHERE username = %s", (username,))
   user = cur.fetchone()

   if user:
      return user[0]  # existing user id
   else:
      cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
      return cur.fetchone()[0]  # new user id

def get_user_progress(cur, user_id):
   cur.execute("""
      SELECT level, score FROM user_score 
      WHERE user_id = %s ORDER BY id DESC LIMIT 1
      """, (user_id,))
   return cur.fetchone()

def save_score(cur, user_id, level, score):
   cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)",
               (user_id, level, score))

username = input("Enter your username: ")
user_id = get_or_create_user(cur, username)

progress = get_user_progress(cur, user_id)
if progress:
   print(f"Your last level: {progress[0]}, Score: {progress[1]}")

# Placeholder for game...
level = 2
score = 1200

pause = input("Press P to pause and save: ")
if pause.lower() == 'p':
   save_score(cur, user_id, level, score)

conn.commit()
cur.close()
conn.close()