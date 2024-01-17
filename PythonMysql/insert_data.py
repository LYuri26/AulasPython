import mysql.connector


def insert_data_into_table(data):
    try:
        # Conectar ao MySQL (certifique-se de fornecer suas próprias credenciais)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="academia"
        )

        # Inserir dados na tabela
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO Academia 
            (exercise_name, repetitions, sets, muscle_activation, load_speed, rest, notes, substitute_exercise) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, data)

        # Commit e fechar a conexão
        connection.commit()
        connection.close()
    except mysql.connector.Error as err:
        raise err


if __name__ == "__main__":
    # Exemplo de uso para testar a inserção de dados
    sample_data = ("Agachamento", 10, 3, "Quadríceps", "80kg",
                   "2min", "Anotações de teste", "Leg press")
    insert_data_into_table(sample_data)
