# atualizacao_aluno.py
import mysql.connector

# Conectando ao banco de dados 'escola'
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="escola"
)

# Atualizando o nome de um aluno específico na tabela 'alunos'
cursor = conexao.cursor()

# Exemplo: Atualizando o nome do aluno com id igual a 1 para "José Silva"
id_aluno = 1
novo_nome = "José Silva"

cursor.execute("""
    UPDATE alunos
    SET nome = %s
    WHERE id = %s
""", (novo_nome, id_aluno))

conexao.commit()
print(f"Nome do aluno com id {id_aluno} atualizado para '{novo_nome}'.")

# Fechando a conexão
conexao.close()
