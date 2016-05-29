import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("DROP TABLE COMPANY")
conn.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print("Table created successfully")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Bredt', 32, 'California', 10000.00 )")
conn.commit()
cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])

conn.close()
