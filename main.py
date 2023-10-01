import sqlite3
import random
conn = sqlite3.connect("Project_2 (3) (2).db")
cursor = conn.cursor()
score = 9
cursor.execute('''SELECT * FROM Favorites_Games ''')

data = cursor.fetchall()

i = random.randint(0, len(data))
print(data[i])