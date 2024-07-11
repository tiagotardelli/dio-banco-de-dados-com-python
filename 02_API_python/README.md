# Conectado-se a um Banco de Dados
A primeira etapa para trabalhar com um banco de dados é estabelecer uma conexão. Vamos ver como é possível usando Python
DB API. 

```python
import sqlite3

con = sqlite3.connect('meu_banco_de_dados.db')
```
# Criar uma tabela
Crear uma tabela é uma operação para que possamos iniciar os nosso modelos. Com a Python API, usamos um cursor para 
executar o comando CREATE.

# Inserir registros
Inserir registros em um banco de dados é uma operação comum. Com a Pyhthon DB API, usamos a operação INSERT do SQL para
isso.

# Atualizando registros
A operação UPDATE do SQL é usada para modificar registros existentes. É importante ser específico ao usar o UPDATE para
evitar alterar mais registros do que o planejado.

# Deletando registros
A operação DELETE do SQL é usada para remover registros. Novamente, precisamos ser específicos ao usar o DELETE para 
evitar remover mais registros do que o planejado.

# Operações em lote
Operações em lote são úteis quando precisamos inserir muitos registros de uma vez. Com Python DB API, podemos usar o
método 'executemany()' para isso.
```python
data = [(5, "abcde"), (6, "asdada"), (7, 'asdefref')]
cursor.executemany('INSERT INTO minha_tabela VALUES (?, ?)', data)
con.commit
```

# Consultas com único resultado
O método 'fetchone()' pode ser usado para recuperar um único registro de resultado. Ele retorna o próximo registro na
lista de resultados ou 'None' se não houver resultados.
```python
cursor.execute('SELECT * FROM minha_tabela WHERE id = 1')
result = cursor.fetchone()
print(result)
```
# Consultas com múltiplos resultados
O método 'fetchall()' pode ser usado para recuperar todos os registros de resultados de uma vez. Ele reorna uma lista de
registros ou uma lista vazia se não houver mais resultados.
```python
cursor.execute('SELECT * FROM minha_tabela')
results = cursor.fetchall()
for row in results:
    print(row)
```

# Trabalhando com resultados de consulta
Os resultados das consultas são retornados como tuplas por padrão. Se a tupla não atender as nossas necessidades podemos
usar a classe 'sqlite3.Row' ou uma 'row_factory' customizada.
```python
cursor.row_factory = sqlite3.Row
cursor.execute('SELECT * FROM minha_tabela WHERE id = 1')
results = cursor.fetchone()
print(dict(result))
```

# Boas Práticas
## Introdução
Ao escrever consultas SQL em Pytho, é importante seguir boas práticas para garantir a segurança do seu código.

## Pensando em segurança
Uma dessas práticas é evitar a concatenação de strings nas consultas e usar consultas parametrizadas. Isso não apemas 
melhora a legibilidade do código, mas também ajuda a prevenir ataques de injeção SQL.
```python
# Evite isso
id = 1
cursor.execute(f'SELECT * FROM minha_tabela WHERE id = ' + str(id))

# Faça isso
id = 1
cursor.execute(f'SELECT * FROM minha_tabela WHERE id = ?', (id,))
```

# Gerenciamento de Transações
## Introdução
A DB API também nos permite gerenciar transações, o que é crucial para mater a integridade dos dados.
```python
try:
    cursor.execute('INSERT INTO minha_tabela VALUES (?, ?)', (1, 'abc'))
    conn.commit()
except Exception as e:
    print(f'Ocorreu um erro: {e}')
    conn.rollback

```


