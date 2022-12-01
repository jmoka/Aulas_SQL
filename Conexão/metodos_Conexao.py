# MÉTODOS
import conexao_mysql_1, conexao_mysql_2

def metodos_mysql1(sql):
  con=conexao_mysql_1.conectar()
  cur = con.cursor()
  cur.execute(sql)
  con.commit()
  con.close()