#METODOS
import mysql
import Conexao_pc_localhost, Conexao_note_localhost

def metodo_mysql_1(sql):
  con=conexao_mysql_1.conectar()
  cur = con.cursor()
  cur.execute(sql)
  con.commit()
  con.close()

def metodo_mysql_2(sql):
  con=conexao_mysql_2.conectar()
  cur = con.cursor()
  cur.execute(sql)
  con.commit()
  con.close()





if __name__=="__main__":
  metodo_mysql_1(sql = '''CREATE TABLE brasil
            (  id  character varying(10), 
               nome VARCHAR(255), 
               cpf int, 
               email  VARCHAR(100) 
        )''')


