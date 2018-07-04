import pymysql

db = pymysql.connect(host = "127.0.0.1",
                     user = "root",
                     password = "alimno",
                     db = "mydb",
                     charset = "utf8",
                     autocommit = True)
select_cursor = db.cursor()
id = input(id: )
select_cursor.execute("Select * from Usuarios where idUsuario = " + id +";")