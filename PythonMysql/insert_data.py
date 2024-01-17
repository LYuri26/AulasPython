import mysql.connector


def insert_data_into_table(data):
    try:
        # Conectar ao MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="academia"
        )

        # Ajustar dados antes de inserir
        data = adjust_data(data)

        # Inserir dados na tabela
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO Academia 
            (nome_do_exercicio, repeticoes, series, ativacao_muscular, carga_velocidade, descanso, anotacoes, exercicio_substituto) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, data)

        # Commit e fechar a conexão
        connection.commit()
        connection.close()
    except mysql.connector.Error as err:
        raise err


def adjust_data(data):
    # Ajustar dados conforme necessário
    nome_do_exercicio, repeticoes, series, ativacao_muscular, carga_velocidade, descanso, anotacoes, exercicio_substituto = data

    # Verificar e ajustar anotações
    if not anotacoes:
        anotacoes = "Sem anotações."

    # Converter descanso para formato desejado
    descanso = descanso.strip() if descanso else None
    if descanso is not None and descanso.isdigit():
        descanso = f"{descanso} segundos."

    # Garantir que repetições, vezes de repetições e descanso sejam inteiros
    repeticoes = int(
        repeticoes) if repeticoes and repeticoes.isdigit() else None
    series = int(series) if series and series.isdigit() else None

    return (nome_do_exercicio, repeticoes, series, ativacao_muscular, carga_velocidade, descanso, anotacoes, exercicio_substituto)
