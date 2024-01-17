import mysql.connector


def create_database_and_table():
    try:
        # Conectar ao MySQL (certifique-se de fornecer suas próprias credenciais)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        # Criar o banco de dados se não existir
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS academia")
        cursor.execute("USE academia")

        # Criar a tabela "Academia" se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Academia (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome_do_exercicio VARCHAR(255),
                repeticoes INT,
                series INT,
                ativacao_muscular VARCHAR(255),
                carga_velocidade VARCHAR(255),
                descanso VARCHAR(255),
                anotacoes TEXT,
                exercicio_substituto VARCHAR(255)
            )
        """)

        # Commit e fechar a conexão
        connection.commit()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Erro ao criar o banco de dados e a tabela:\n{err}")


if __name__ == "__main__":
    create_database_and_table()
