import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    DB='biblioteca'
    user="root",
    password="@Ddaa0927"
)

if mydb.is_connected():
    print('conectou com sucesso')

# -- Connection Id: 10
# -- User: root
# -- Host: localhost
# -- DB: biblioteca
# -- Command: Sleep
# -- Time: 19
# -- State: None
