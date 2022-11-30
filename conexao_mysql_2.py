import mysql.connector

def conectar(host, database, user, password, port):
    con=mysql.connector.connect(
                                host =host,
                                database=database,
                                user=user,
                                password=password,
                                port=port)
    print('CONECTADO')

    return con

if __name__ == '__main__':

    host = 'localhost'
    database = 'jotaempresas'
    user = 'root'
    password = 'Jota1@79'
    port = '3306'

    conectar(host, database, user, password, port)
