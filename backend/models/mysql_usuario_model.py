from backend.models.mysql_connection_pool import MySQLPool

class UsuarioModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_usuario(self, usuario_id):
        query = "SELECT * FROM usuario WHERE id = %(usuario_id)s"
        params = {'usuario_id': usuario_id}
        rv = self.mysql_pool.execute(query, params)
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0],
                'usuario_rol': result[1],
                'usuario_nombres': result[2],
                'usuario_apellidos': result[3],
                'usuario_correo': result[4],
                'usuario_contrasenia': result[5]
            }
            data.append(content)
            content = {}
        return data

    def get_usuarios(self):
        query = "SELECT * FROM usuario"
        rv = self.mysql_pool.execute(query)
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0],
                'usuario_rol': result[1],
                'usuario_nombres': result[2],
                'usuario_apellidos': result[3],
                'usuario_correo': result[4],
                'usuario_contrasenia': result[5]
            }
            data.append(content)
            content = {}
        return data

    def create_usuario(self, id, usuario_rol, usuario_nombres, usuario_apellidos, usuario_correo, usuario_contrasenia):
        data = {
            'id': id,
            'usuario_rol': usuario_rol,
            'usuario_nombres': usuario_nombres,
            'usuario_apellidos': usuario_apellidos,
            'usuario_correo': usuario_correo,
            'usuario_contrasenia': usuario_contrasenia
        }
        query = """INSERT INTO usuario (id,usuario_rol, usuario_nombres, usuario_apellidos, usuario_correo, usuario_contrasenia) 
                   VALUES (%(id)s, %(usuario_rol)s, %(usuario_nombres)s, %(usuario_apellidos)s, %(usuario_correo)s, %(usuario_contrasenia)s)"""
        cursor = self.mysql_pool.execute(query, data, commit=True)
        return data

    def update_usuario(self, usuario_id, usuario_rol, usuario_nombres, usuario_apellidos, usuario_correo, usuario_contrasenia):
        data = {
            'id': usuario_id,
            'usuario_rol': usuario_rol,
            'usuario_nombres': usuario_nombres,
            'usuario_apellidos': usuario_apellidos,
            'usuario_correo': usuario_correo,
            'usuario_contrasenia': usuario_contrasenia
        }
        query = """UPDATE usuario SET usuario_rol = %(usuario_rol)s, 
                   usuario_nombres = %(usuario_nombres)s, 
                   usuario_apellidos = %(usuario_apellidos)s, 
                   usuario_correo = %(usuario_correo)s, 
                   usuario_contrasenia = %(usuario_contrasenia)s 
                   WHERE id = %(id)s"""
        self.mysql_pool.execute(query, data, commit=True)
        result = {'result': 1}
        return result

    def delete_usuario(self, usuario_id):
        params = {'id': usuario_id}
        query = "DELETE FROM usuario WHERE id = %(id)s"
        self.mysql_pool.execute(query, params, commit=True)
        result = {'result': 1}
        return result