from conexao import conecta_db

# DML = Linguagem de manipulação de Dados
#CRUD => Create, Read, Update , Delete
#        INSERT, SELECT , UPDATE, DELETE 


# DDL = Linguagem de Criação de tabelas
#  Create table 
#  DROP table
#  Alter table 

def consultar(conexao):
    livros = []
    cursor = conexao.cursor()
    select_livro = """
    select livro.id as id_livro,
	   livro.nome as livro_nome,
       autor.nome as autor_nome,
	   editora.nome as editora_nome
	   from livro
       
    inner join autor on (livro.id_autor = autor.id)

    inner join editora on (livro.id_editora = editora.id)
    """
    cursor.execute(select_livro)
    registros = cursor.fetchall()
    print("|-----------------------------------|")
    for registro in registros:
        item = {
            "id": registro[0],
            "nome_livro": registro[1],
            "nome_autor": registro[2],
            "nome_editora": registro[3]
        }
        livros.append(item)
    return livros


def consultar_por_id(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("select id,nome from livro where id = %s",[id])
    registro = cursor.fetchone()
    item = {
        "id": registro[0],
        "nome": registro[1]
    }
    return item

def inserir(conexao, nome, id_editora, id_autor):
    cursor = conexao.cursor()
    sql_insert = "insert into livro (nome,id_editora,id_autor) values (%s, %s, %s)"
    dados = (nome, id_editora, id_autor)
    cursor.execute(sql_insert, dados)
    conexao.commit()
        
def alterar(conexao, id, nome):
    cursor = conexao.cursor()
    sql_update = "update livro set nome = %s where id = %s"
    dados   = (nome, id)
    cursor.execute(sql_update,dados)
    conexao.commit()    


def deletar(conexao, id):
    cursor = conexao.cursor()
    sql_delete = "delete from  livro where id =  %s"
    cursor.execute(sql_delete,[id])
    conexao.commit()