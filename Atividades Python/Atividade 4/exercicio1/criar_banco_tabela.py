# criar_banco_tabela.py
import mysql.connector

# Conectando ao servidor MySQL local
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Criando o banco de dados 'escola'
cursor = conexao.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS escola")
print("Banco de dados 'escola' criado com sucesso.")

# Conectando ao banco de dados 'escola'
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="escola"
)

# Criando a tabela 'alunos'
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        idade INT,
        cidade VARCHAR(100)
    )
""")
print("Tabela 'alunos' criada com sucesso.")
