import sqlite3
conn = sqlite3.connect('sqlite3test.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS quote
          (nickname text, message text, number INTEGER) ''')

c.execute("INSERT INTO quote VALUES('r0flcopter','heyheyhey','1')")

conn.commit()

for row in c.execute('SELECT * FROM quote'):
    print(row)

conn.close()
