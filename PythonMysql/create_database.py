import mysql.connector


def create_database_and_table():
    try:
        # Conectar ao MySQL (certifique-se de fornecer suas próprias credenciais)
        connection = mysql.connector.connect(
            host="seu_host",
            user="seu_usuario",
            password="sua_senha"
        )

        # Criar o banco de dados se não existir
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS academia")
        cursor.execute("USE academia")

        # Criar a tabela "Academia" se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Academia (
                id INT AUTO_INCREMENT PRIMARY KEY,
                exercise_name VARCHAR(255),
                repetitions INT,
                sets INT,
                muscle_activation VARCHAR(255),
                load_speed VARCHAR(255),
                rest VARCHAR(255),
                notes TEXT,
                substitute_exercise VARCHAR(255)
            )
        """)

        # Commit e fechar a conexão
        connection.commit()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Erro ao criar o banco de dados e a tabela:\n{err}")


if __name__ == "__main__":
    create_database_and_table()
