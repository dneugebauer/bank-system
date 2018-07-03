from bank_system import *

new_table()

# Test
for i in range(100):
    new_account('Bot_' + str(i), 100)

# Close Memory
c.close()
conn.close()
