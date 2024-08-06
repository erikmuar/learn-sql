import sqlite3

def insert_one(usuario, nombre, sexo, nivel, email, telefono, marca, compania, saldo, activo):
    # Conectar a la base de datos
    conn = sqlite3.connect('db_python.sqlite')
    cur = conn.cursor()

    # Leer el archivo SQL
    with open('insertOne.sql', 'r') as sql_file:
        sql_query = sql_file.read()

    # Ejecutar la consulta
    cur.execute(sql_query,((usuario, nombre, sexo, nivel, email, telefono, marca, compania, saldo, activo)))
    
    conn.commit()

    # Cerrar la conexión
    conn.close()

if __name__ == '__main__':
  # Ejemplo de uso
  insert_one('pepe','Pepe','H','2','pepe@larana.com','666-510-423','LG','TELECEL',120,1)
