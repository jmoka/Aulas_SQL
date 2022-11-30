import mysql.connector

def conectar():
    con=mysql.connector.connect(
                                host ='localhost',
                                database='jotaempresas',
                                user='root',
                                password='Jota1@79',
                                port='3306')
    print('CONECTADO')

    return con
if __name__ == '__main__':
        conectar()
