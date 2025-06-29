from dotenv import load_dotenv
import pyodbc
import os


def conexao():
    try:
        
        load_dotenv()
        
        DRIVER = os.getenv("MYSQL_DRIVER")
        SERVER = os.getenv("MYSQL_HOST")
        DATABASE = os.getenv("MYSQL_DB")
        USER = os.getenv("MYSQL_USER")
        PSWD = os.getenv("MYSQL_PASSWORD")
        
        conexao_db = pyodbc.connect(
            f'DRIVER={DRIVER};'
            f'SERVER={SERVER};'
            f'DATABASE={DATABASE};'
            f'UID={USER};PWD={PSWD};'
        )
    
    except Exception as e:
        print(str(e))
    return conexao_db
    

def cadastrar_produto(nome_produto:str, descricao:str, valor_produto:float, valor_revenda: float, unidade:str,
                      quantidade:int, imagem:str, codigo_produto:str):
    try:
        
        cursor = conexao().cursor()
        
        string_sql = f"""
                        INSERT INTO PROJETOS_PYTHON.dbo.CADASTRO_PRODUTOS_FLASK
                            (NOME_PRODUTO, DESCRICAO_PRODUTO, VALOR_PRODUTO, VALOR_REVENDA, UNIDADE, QUANTIDADE_ESTOQUE, IMAGEM_PRODUTO, CODIGO_PRODUTO)
                        VALUES('{nome_produto}', '{descricao}', {valor_produto}, {valor_revenda}, '{unidade}', {quantidade}, '{imagem}', '{codigo_produto}');      
                    """
        cursor.execute(string_sql)
        cursor.commit()
        cursor.close()
        conexao().close()
        
    except Exception as e:
        print(str(e))
                        
