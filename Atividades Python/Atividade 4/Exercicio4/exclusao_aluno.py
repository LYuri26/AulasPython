# exclusao_aluno.py
import mysql.connector

# Conectando ao banco de dados 'escola'
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="escola"
)

# Excluindo um aluno da tabela 'alunos' com base no ID
cursor = conexao.cursor()

# Exemplo: Excluindo o aluno com id igual a 2
id_aluno = 2

cursor.execute("""
    DELETE FROM alunos
    WHERE id = %s
""", (id_aluno,))

conexao.commit()
print(f"Aluno com id {id_aluno} excluído com sucesso.")

# Fechando a conexão
conexao.close()
