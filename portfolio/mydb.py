import mysql.connector

data_base = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'

)


cursor_object = data_base.cursor()

cursor_object.execute('CREATE DATABASE portfolio')

print('Exito al crear la db.')