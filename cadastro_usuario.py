import bcrypt

def listar_usuarios(conexao):
    usuarios = []
    cursor = conexao.cursor()
    cursor.execute("select id,login from usuario")
    registros = cursor.fetchall()
 
    for registro in registros:
        item = {
            "id": registro[0],
            "nome": registro[1]
        }
        usuarios.append(item)
    return usuarios

def inserir_usuario_bd(conexao, login, senha):
    criptografia = bcrypt.gensalt()
    senha_criptografada = bcrypt.hashpw(senha.encode("utf-8"), criptografia)
    print(senha_criptografada)
    cursor = conexao.cursor()
    cursor.execute("insert into usuario (login,senha) values ('" + login + "', '" + senha_criptografada + "')")
    conexao.commit()

def alterar_usuario_bd(conexao,id,login):
    cursor = conexao.cursor()
    sql_update = "update usuario set login = %s where id = %s"
    dados   = (login, id)
    cursor.execute(sql_update,dados)
    conexao.commit()

def deletar_usuario_bd(conexao,id):
    cursor = conexao.cursor()
    sql_delete = "delete from usuario where id = %s"
    cursor.execute(sql_delete,[id])
    conexao.commit()


def consultar_usuario_por_id(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("select id,login from usuario where id = %s",[id])
    registro = cursor.fetchone()
    item = {
        "id": registro[0], 
        "login": registro[1]
    }
    return item

def verificar_login(conexao, login, senha):
    cursor = conexao.cursor()
    cursor.execute("select id, login, senha from usuario" + " where login = %s and senha = %s", (login,senha))
    registro = cursor.fetchone()
    
    if registro is None:
        return False
    else:
        return True
    

    
