import sqlite3
import random
import time, datetime

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

def random_id(): # Creates "unique" 9-digit account ID
    unix_temp = int(time.time())
    temp_id = str((unix_temp + random.randint(1,unix_temp))**5)
    return temp_id[-18:-9]

def new_account(client, deposit):
    if account_lookup(client) != []:
        print('{} already has an account.'.format(client))
    else:
        unix = time.time()
        id = random_id()
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        c.execute('INSERT INTO accountbook (accountid, name, balance, opendate) VALUES (?, ?, ?, ?) ',
            (id, client, deposit, date))
        conn.commit()

def connect_table():
    c.execute('CREATE TABLE IF NOT EXISTS accountbook(accountid TEXT, name TEXT, balance INTEGER , opendate TEXT)')

def account_lookup(client):
    c.execute('SELECT name, balance, accountid, opendate FROM accountbook WHERE name=?', [client])
    data = c.fetchall() # This is the data set for client
    #print("Account '{}' has a balance of {}.".format(data[0][0], data[0][1]))
    return data
