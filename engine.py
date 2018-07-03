import sqlite3
import time, datetime

conn = sqlite3.connect('accounts.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTs accountbook(accountid INTEGER, name TEXT, balance REAL , opendate TEXT)')

# Functions
def new_account(name, deposit):
    unix = time.time()
    id = (int(unix)**5) % 1000000000 # Creates "unique" 9-digit account ID
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute('INSERT INTO accountbook (accountid, name, balance, opendate) VALUES (?, ?, ?, ?)',
        (id, name, deposit, date))
    conn.commit()

# Test
for i in range(10):
    new_account('Bot_' + str(i), 100)
    time.sleep(1)

# Close Memory
c.close()
conn.close()
