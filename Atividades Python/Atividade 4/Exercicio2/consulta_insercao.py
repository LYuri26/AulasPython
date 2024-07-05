# consulta_insercao.py
import mysql.connector

# Conectando ao banco de dados 'escola'
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="escola"
)

# Inserindo dados na tabela 'alunos'
cursor = conexao.cursor()

# Inserindo três registros fictícios
dados_alunos = [
    ("João", 20, "São Paulo"),
    ("Maria", 22, "Rio de Janeiro"),
    ("Pedro", 19, "Belo Horizonte")
]

cursor.executemany("""
    INSERT INTO alunos (nome, idade, cidade)
    VALUES (%s, %s, %s)
""", dados_alunos)

conexao.commit()
print(f"Foram inseridos {cursor.rowcount} registros.")

# Consultando e exibindo todos os registros da tabela 'alunos'
cursor.execute("SELECT * FROM alunos")
registros = cursor.fetchall()

print("\nRegistros na tabela 'alunos':")
for aluno in registros:
    print(aluno)

# Fechando a conexão
conexao.close()
