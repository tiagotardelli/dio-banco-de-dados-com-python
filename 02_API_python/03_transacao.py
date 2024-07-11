import sqlite3

from pathlib import Path

DB_FILE = Path(__file__).parent / 'meu_banco.sqlite'

conexao = sqlite3.connect(DB_FILE)
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', ("Teste 2", "teste2@1@gmail.com"))
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?, ?)', (2, 'Teste 3', 'teste3@1@gmail.com'))
    conexao.commit()
except Exception as exc:
    print(f'Ops! Um erro ocorreu {exc}')
    conexao.rollback
# Alguns casos usam assim
# finally:
  #  conexao.commit()
