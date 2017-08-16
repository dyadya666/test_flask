import sqlite3
conn = sqlite3.connect('/home/sergey/projects/test_flask/app.db')
c = conn.cursor()

query1 = 'SELECT * FROM user;'
query2 = 'SELECT * FROM score;'

c.execute(query1)
row = c.fetchone()
print('user')
while row is not None:
    print('{0}: {1}'.format(row[0], row[1]))
    row = c.fetchone()

c.execute(query2)
row2 = c.fetchone()
print('score')
while row2 is not None:
    print('{0}: {1}, {2}, {3}, {4}'.format(row2[0], row2[1], row2[2], row2[3], row2[4]))
    row2 = c.fetchone()

c.close()
conn.close()