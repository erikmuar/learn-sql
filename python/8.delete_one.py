import sqlite3

def delete_one(id):
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect('db_python.sqlite')
        cur = conn.cursor()

        # Leer el archivo SQL
        with open('deleteOne.sql', 'r') as sql_file:
            sql_query = sql_file.read()

        # Ejecutar la consulta
        cur.execute(sql_query, (id, ))

        # Confirmar la transacción
        conn.commit()

    except sqlite3.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

if __name__ == '__main__':
    # Ejemplo de uso
    delete_one(1)