import sqlite3
import random
import time, datetime

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

def random_id(): # Creates "unique" 9-digit account ID
    unix_temp = int(time.time())
    temp_id = str((unix_temp + random.randint(1,unix_temp))**5)
    return temp_id[-18:-9]

def new_account(name, deposit):
    unix = time.time()
    id = random_id()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute('INSERT INTO accountbook (accountid, name, balance, opendate) VALUES (?, ?, ?, ?)',
        (id, name, deposit, date))
    conn.commit()

def new_table():
    c.execute('CREATE TABLE IF NOT EXISTs accountbook(accountid TEXT, name TEXT, balance REAL , opendate TEXT)')
