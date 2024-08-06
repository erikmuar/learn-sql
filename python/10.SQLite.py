import sqlite3
# from pathlib import Path

class DBConnector():
    
    # constructor
    # ruta a la db de sqlite
    def __init__(self, ruta_a_db: str) -> None:
        self.database = ruta_a_db
        print("ruta a db:", self.database)
    
    def conectar(self):
        conn = sqlite3.connect(self.database)
        return conn
    
    def desconectar(self, conn):
        conn.close()
    
    # create table
    def crear_tabla(self, params=None, sql=None):
        conn = self.conectar()
        cur = conn.cursor()
        # create table por param
        # nombre tabla por param
        cur.execute('''
        CREATE TABLE IF NOT EXISTS tblUsuarios (
          idx INTEGER PRIMARY KEY AUTOINCREMENT,
          usuario TEXT NOT NULL,
          nombre TEXT NOT NULL,
          sexo TEXT CHECK(sexo IN ('M', 'H')),
          nivel INTEGER CHECK(nivel BETWEEN 0 AND 255),
          email TEXT,
          telefono TEXT,
          marca TEXT,
          compañia TEXT,
          saldo REAL,
          activo INTEGER CHECK(activo IN (0, 1))
        )
        ''')
        conn.commit()
        self.desconectar(conn)

    # podemos pasarle una fuente de datos como un CSV:
    def seed(datos):
        pass
    
    # leer datos
      # order by... 
    def select(id):
        pass
    
    # actualizar
    def update(id):
        pass
    
    # borrar por id
    def delete(id):
        pass
    

if __name__ == '__main__':
    db_conn = DBConnector("db.sqlite3")
    db_conn.crear_tabla()
