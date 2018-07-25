import mysql.connector

cnx = mysql.connector.connect(user='admin', password='admin', host='127.0.0.1', database='instashit')
cnx.autocommit = True
cursor = cnx.cursor()

empty_table = 'DELETE FROM default_list;'
set_autoincrement = 'ALTER TABLE default_list AUTO_INCREMENT = 1;'
select = "SELECT * FROM default_list ORDER BY id;"
insert = "INSERT INTO default_list(name) VALUES (%s), (%s);"
insert1 = "INSERT INTO default_list(name) VALUE (%s);"


first_attr = 'lol'
second_attr = 'kek'
test = 'https://www.instagram.com/happy_hostel_kiev/'

cursor.execute(empty_table)
cursor.execute(set_autoincrement)
cursor.execute(insert, (first_attr, second_attr))
cursor.execute(insert1, (test,))
cursor.execute(select)

for (id, name, time) in cursor:
    print("{}    {}     {}".format(id, name, time))

cursor.close()
cnx.close()

