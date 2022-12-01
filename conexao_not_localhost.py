import mysql.connector

#========================
# PRIMEIRA CONEXAO
#========================
def conectar_pc_1():
    con=mysql.connector.connect(host ='localhost',
                                database='Aulas',
                                user='root',
                                password='123456',
                                port='3306')
    print('CONECTADO')

    return con
# ========================================================

#=========================
# SEGUNDA CONEXAO
#=========================
def conectar_pc_2(host, database, user, password, port):
    con=mysql.connector.connect(
                                host =host,
                                database=database,
                                user=user,
                                password=password,
                                port=port)
    print('CONECTADO')

    return con
def dados_conexao_pc_2():
    host = 'localhost'
    database = 'Aulas'
    user = 'root'
    password = '123456'
    port = '3306'

    return conectar_pc_2(host, database, user, password, port)

# ========================================================
primeira=conectar_pc_1()
segunda=dados_conexao_pc_2()
if __name__ == '__main__':
    #primeira()
    segunda()

# =========================================================