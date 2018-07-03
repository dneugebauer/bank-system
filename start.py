from bank_system import *

connect_table()

# Test
for i in range(100):
    new_account('Bot_' + str(i), 100)

account_lookup("Bot_7")

# Close Memory
c.close()
conn.close()
