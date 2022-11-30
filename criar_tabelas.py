import mysql.connector

# Criar Tabela
def conectar():
    con=mysql.connector.connect(
                                host ='localhost',
                                database='db_aulas',
                                user='root',
                                password='Jota1@79',
                                port='3306')
    print('CONECTADO')

    return con

# Métodos
def metodo_mysql_1(sql):
  con=conectar()
  cur = con.cursor()
  cur.execute(sql)
  con.commit()
  con.close()

# CRIAR UMA TABELA
def tabela():
    sql = '''CREATE TABLE brasil
            (  id  character varying(10), 
               nome VARCHAR(255), 
               cpf int, 
               email  VARCHAR(100) 
        )'''
    return metodo_mysql_1(sql)




if __name__ == "__main__":
    tabela()

