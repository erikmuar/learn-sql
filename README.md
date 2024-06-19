# learn-sql

Crear la db:
```bash
  sqlite3 <db>.sqlite3
```
Ver tablas:
```
  .tables
```
No saldrá nada la primera vez
Crear una tabla `usuario`:
```bash
  CREATE TABLE usuario (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      email TEXT NOT NULL UNIQUE,
      nombre TEXT NOT NULL
  );
```
Insertamos un dato:
```bash
  INSERT INTO usuario (email, nombre) VALUES ('example@example.com', 'Example Name');
```
Mirar todos los datos:
```
  SELECT * FROM usuario;
```
