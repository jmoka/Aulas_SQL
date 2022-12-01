import conexao_not_localhost
import metodos

# CRIAR UMA TABELA
def tabela():

    sql = '''CREATE TABLE brasil
            (  id  character varying(10), 
               nome VARCHAR(255), 
               cpf int, 
               email  VARCHAR(100) 
        )'''
    
    return conexao_not_localhost(sql)




if __name__ == "__main__":
    tabela()

