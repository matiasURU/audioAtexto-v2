import sqlite3

sql_tabla_usuarios = '''
CREATE TABLE USUARIOS(
 ID INTEGER PRIMARY KEY,
 NOMBRE TEXT,
 CORREO TEXT,
 CLAVE TEXT,
 ROL TEXT
)
'''

sql_tabla_sesiones = '''
CREATE TABLE SESIONES(
 ID INTEGER PRIMARY KEY,
 ID_USUARIO TEXT,
 FECHA_HORA TEXT,
 FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS(ID_USUARIO) 
)
'''

if __name__ == '__main__':
    try:
        print('Creando Base de datos..')
        conexion = sqlite3.connect('../../audioAtexto.db')

        print('Creando Tablas..')
        conexion.execute(sql_tabla_usuarios)
        conexion.execute(sql_tabla_sesiones)

        conexion.close()
        print('Creacion Finalizada.')
    except Exception as e:
        print(f'Error creando base de datos: {e}', e)
