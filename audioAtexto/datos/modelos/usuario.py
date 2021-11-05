from datos.base_de_datos import BaseDeDatos


def obtener_usuario(id_usuario):
    obtener_usuarios_sql = f"""
        SELECT id, nombre, correo, rol 
        FROM USUARIOS 
        WHERE ID = {id_usuario}
    """
    bd = BaseDeDatos()
    return [{"id": registro[0],
             "nombre": registro[1],
             "correo": registro[2],
             "rol": registro[3]
             } for registro in bd.ejecutar_sql(obtener_usuarios_sql)]


def obtener_usuarios():
    obtener_usuarios_sql = f"""
        SELECT id, nombre, correo, rol 
        FROM USUARIOS
    """
    bd = BaseDeDatos()
    return [{"id": registro[0],
             "nombre": registro[1],
             "correo": registro[2],
             "rol": registro[3]
             } for registro in bd.ejecutar_sql(obtener_usuarios_sql)]


def crear_usuario(nombre, correo, clave):
    crear_usuario_sql = f"""
        INSERT INTO USUARIOS(NOMBRE, CORREO, CLAVE)
        VALUES ('{nombre}','{correo}','{clave}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)


def modificar_usuario(id_usuario, datos_usuario):
    modificar_usuario_sql = f"""
        UPDATE USUARIOS
        SET NOMBRE='{datos_usuario["nombre"]}', CORREO='{datos_usuario["correo"]}', CLAVE='{datos_usuario["clave"]}', APELLIDO='{datos_usuario["apellido"]}'
        WHERE ID='{id_usuario}')
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_usuario_sql)


def obtener_usuarios_por_nombre_clave(nombre, correo, clave):
    obtener_usuario_sql = f"""
            SELECT id, nombre, correo, rol 
            FROM USUARIOS
            WHERE NOMBRE = '{nombre}' and CORREO = '{correo}' and CLAVE = '{clave}'
        """
    bd = BaseDeDatos()
    print(obtener_usuario_sql)
    #print()
    for registro in bd.ejecutar_sql(obtener_usuario_sql):
        print(registro)
    return [{"id": registro[0],
             "nombre": registro[1],
             "correo": registro[2],
             "rol": registro[3]
             } for registro in bd.ejecutar_sql(obtener_usuario_sql)]


def borrar_usuario(id_usuario):
    obtener_usuarios_sql = f"""
        DELETE
        FROM USUARIOS 
        WHERE ID = {id_usuario}
    """
    bd = BaseDeDatos()
    bd.ejecutar_sql(obtener_usuarios_sql)


def crear_sesion(id_usuario, dt_string):
    crear_sesion_sql = f"""
               INSERT INTO SESIONES(ID_USUARIO, FECHA_HORA)
               VALUES ('{id_usuario}', '{dt_string}')
           """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(crear_sesion_sql, True)


def obtener_sesion(id_sesion):
    obtener_sesion_sql = f"""
        SELECT ID, ID_USUARIO, FECHA_HORA FROM SESIONES WHERE ID = {id_sesion}
    """
    bd = BaseDeDatos()
    return [{"id": registro[0],
             "id_usuario": registro[1], "fecha_hora": registro[2]}
            for registro in bd.ejecutar_sql(obtener_sesion_sql)]
