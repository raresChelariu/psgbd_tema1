import cx_Oracle
# pip install cx_Oracle

user = 'student'
pw = 'STUDENT'
dsn = 'localhost'

con = cx_Oracle.connect(user, pw, dsn)

c = con.cursor()
c.execute('select * from studenti')
for row in c:
    print(row[0], '-', row[1], '-', row[2], '-', row[3], '-', row[4])
con.close()
