import sqlite3

from pathlib import Path

DB_FILE = Path(__file__).parent / 'meu_banco.sqlite'

conexao = sqlite3.connect(DB_FILE)
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


#  1 OR nome LIKE '%Vanessa%' ORDER BY nome DESC
id_cliente = input('Informe o ID do cliente: ')
cursor.execute(f'SELECT * FROM clientes WHERE id={id_cliente}')
cliente = cursor.fetchone()
print(dict(cliente))

id_cliente = input('Informe o ID do cliente: ')
cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
cliente = cursor.fetchone()
print(dict(cliente))