import mysql.connector

connection = mysql.connector.connect(user='   ', password='   ', host='   ', database='   ',
                                     auth_plugin='mysql_native_password')

cursor = connection.cursor()
# insertQuery= "INSERT INTO test(name, city)VALUES(%(name)s,%(city)s)"
# insertData= {
    # 'name': '    ',
    # 'city': '    ',


# }
# cursor.execute(insertQuery,insertData)


# deleteQuery= "DELETE FROM test WHERE name ='   '"
# cursor.execute(deleteQuery)
query = 'SELECT id, name, city FROM test'

connection.commit()
cursor.execute(query)
for (id ,name,city) in cursor:
    print(name,city)

connection.close()