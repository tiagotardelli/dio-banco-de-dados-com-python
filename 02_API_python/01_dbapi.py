import sqlite3

from pathlib import Path

DB_FILE = Path(__file__).parent / 'meu_banco.sqlite'

conexao = sqlite3.connect(DB_FILE)
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(cursor):
    cursor.execute("""
    CREATE TABLE clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        email VARCHAR(150)
    );
    """)

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("""
    INSERT INTO clientes (nome, email)
        VALUES (?, ?); 
    """, data)
    conexao.commit();

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("""
    UPDATE clientes 
       SET nome = ?
         , email = ?
     WHERE id = ?; 
    """, data)
    conexao.commit();

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("""
    DELETE FROM clientes 
          WHERE id = ?; 
    """, data)
    conexao.commit();

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("""
    INSERT INTO clientes (nome, email)
        VALUES (?, ?); 
    """, dados)
    conexao.commit();

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome")

# atualizar_registro(conexao, cursor, "Tiago Baldo Tardelli", "tiagob.tardelli@gmail.com", 1)
# excluir_registro(conexao, cursor, 1)

# dados = [
#    ("Vanessa Murta Soares", "van@gmail.com"),
#    ("Enrico Souza Silva", "teste@teste.com.br"),
#    ("Carlos Almeida Melo", "teste@teste.com.br"),
#    ("Keyte Hugo Kiko", "teste@teste.com.br"),
#    ("Ramiro Crepalim Perduz", "teste@teste.com.br")
# ]
# inserir_muitos(conexao, cursor, dados)


# cliente = recuperar_cliente(cursor, 1)
# print(cliente)

# clientes = listar_clientes(cursor)
# for cliente in clientes:
#    print(cliente)

# com row_factory adicionado
clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente["id"], cliente["nome"])