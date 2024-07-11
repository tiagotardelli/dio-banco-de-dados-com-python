# Banco de Dados Relacional

## O que é um Banco de Dados?
Os banco de dados são coleções organizadas de dados, geralmente armazenados e acessados eletronicamente a partir de 
um sistema de computador.

## Tipos de Bancos de Dados
Existem vários tipos de banco de dados, incluindo relacionais, não relacionais, orientados a objetos e muito mais. O
tipo mais comum é o banco de dados relacional, que organiza os dados em tabelas.

## O papel do SGBD
Os Sistemas de Gerenciamento de Banco de Dados (SGBD) são softwares que interagem com o usuário, outras aplicações e o
próprio banco de dados para capturar e analisar os dados. Existem muitos SGBDs diponíveis no mercado, alguns dos mais
populares incluem: MySQL, PostgreSQL, SQLite, Oracle Database, Microsoft SQL Server e MariaDB.

## Introdução aos Banco de Dados Relacionais
Um banco de dados relacional é um tipo de banco de dados que organiza os dados em tabelas. Cada tabela é composta de
linhas, que representam registros individuais, e colunas, que repesentam campos de dados.

## Tabelas
Em um banco de dados relacional, uma tabela é uma estrutura que organiza os dados em linhas e colunas, semelhante a uma
planilha.
Cada linha representa um registro distinto e cada coluna representa um tipo de informação, chamado de campo. Por
exemplo, uma tabela 'Clientes' pode ter campos como 'ID', 'nome', 'email', 'telefone'.

Clientes
|Id    |nome   |e-mail              |telefone        |
|:---: |:---:  |:---:               |:---:           |
|1     | Tiago | teste@teste.com.br | 15-33333-33333 |


## Chaves Primárias (Primary Key / PK )
Cada tabela em um banco de dados relacional deve ter uma chave primária. A chave primária é uma coluna (ou conjunto de
colunas) cujo valor é único para cada registro. Isso garante que cada registro na tabela possa ser identificado de
maneira única. Por exemplo, na tabela 'Cliente', o campo 'ID' pode ser a chave primária.

Clientes
|**Id(PK)**|nome  |e-mail             |telefone       |
|:---:     |:---: |:---:              |:---:          |
|**1**     |Tiago |teste@teste.com.br |15-33333-33333 |
|**2**     |Luis  |teste@teste.com.br |15-33333-33333 |

## Chaves Estrangeiras (Forign Key / FK )
Por exemplo, em uma tabela 'Pedidos', podemos ter um campo 'ClienteID' que seja uma chave estrangeira apontando para a
chave primária da tabela 'Clientes'. Isso cria um relacionamento entre 'Pedidos' e 'Clientes', permitindo que cada
pedido seja associado a um cliente específico.

Clientes
|**Id(PK)**|nome  |e-mail             |telefone       |
|:---:     |:---: |:---:              |:---:          |
|**1**     |Tiago |teste@teste.com.br |15-33333-33333 |
|**2**     |Luis  |teste@teste.com.br |15-33333-33333 |

Pedidos
|**Id(PK)**|valor      |Id_Cliente(FK)|
|:---:     |:---:      |:---:         |
|**1**     |R$ 200,00  |1             |   
|**2**     |R$ 1500,00 |2             |

## Relacionamento entre tabelas
Os bancos de dados relacionais permitem estabelecer relações entre tabelas. As relações podem ser 'um para um', 'um para
muitos', ou 'muitos para muitos'. Estas relações permitem efetuar consultas complexas que unem dados de várias tabelas.

** Documento (1,1)
** Pets_Usuarios (n,n)

Usuarios
|**Id(PK)**|nome      |e-mail             |**id_documento(FK)**|
|:---:     |:---:     |:---:              |:---:               |
|**1**     |Tiago     |teste@teste.com.br |1                   |
|**2**     |Guilherme |teste@teste.com.br |2                   |

Pets
|**Id(PK)**|nome  |data_nascimento|
|:---:     |:---: |:---:          |
|**1**     |Sky   |21/02/2020     |   
|**2**     |Thor  |21/02/2020     |

Documentos
|**Id(PK)**|nome  |valor          |**id_cliente(FK)**|
|:---:     |:---: |:---:          |:---:             |
|**1**     |cpf   |123.123.123-09 |1                 |
|**2**     |cpf   |124.124.124-09 |2                 |

Pets_Usuarios
|**Id(PK)**|id_usuario  |id_pet|
|:---:     |:---:       |:---: |
|**1**     |1           |1     |   
|**2**     |2           |1     |

![Exemplo Visual](exemplo_relacionamento.png)

## SQL (Structured Query Language)
O SQL é a linguagem usada para interagir com banco de dados relacionais. Com SQL, podemos criar tabelas, inserir,
atualizar e deletar registros, bem como executar consultas para buscar dados.

```sql
-- Cria um novo banco de dados
CREATE DATABASE loja;

-- Cria uma tabela para armazenar informações de produtos
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    preco DECIMAL
);

-- Inclui um novo produto
INSERT INTO produtos (nome, preco)
     VALUES ('Curso de Python', 250.00);

-- Lista todos os produtos
SELECT *
  FROM produtos;

-- Atualiza o produto com id informado
UPDATE produtos
   SET nome = 'Curso de Python para iniciantes'
 WHERE id = 1;

 -- Exclui um produto om id informado
 DELETE FROM produtos
       WHERE id =
```
