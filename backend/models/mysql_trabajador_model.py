from backend.models.mysql_connection_pool import MySQLPool

class TrabajadorModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_trabajador(self, trabajador_id):
        query = "SELECT * FROM trabajador WHERE trabajador_id = %(trabajador_id)s"
        params = {'trabajador_id': trabajador_id}
        rv = self.mysql_pool.execute(query, params)
        data = []
        content = {}
        for result in rv:
            content = {
                'trabajador_id': result[0],
                'trabajador_tipo_documento': result[1],
                'trabajador_path_documento': result[2],
                'trabajador_nacionalidad': result[3],
                'trabajador_fecha_nacimiento': result[4].strftime('%Y-%m-%d'),
                'trabajador_ubigeo': result[5],
                'trabajador_telefono': result[6],
                'trabajador_sexo': result[7],
                'trabajador_estado_civil': result[8],
                'trabajador_path_doc_estado_civil': result[9],
                'trabajador_fecha_ingreso': result[10].strftime('%Y-%m-%d') if result[10] else None,
                'trabajador_fecha_ingreso_sistema': result[11].strftime('%Y-%m-%d') if result[11] else None,
                'trabajador_edad': result[12],
                'trabajador_record': float(result[13]) if result[13] is not None else 0.0,
                'trabajador_exp_previa': float(result[14]) if result[14] is not None else 0.0,
                'trabajador_total_anios_exp': float(result[15]) if result[15] is not None else 0.0

            }
            data.append(content)
            content = {}
        return data

    def get_trabajadores(self):
        query = "SELECT * FROM trabajador"
        rv = self.mysql_pool.execute(query)
        data = []
        content = {}
        for result in rv:
            content = {
                'trabajador_id': result[0],
                'trabajador_tipo_documento': result[1],
                'trabajador_path_documento': result[2],
                'trabajador_nacionalidad': result[3],
                'trabajador_fecha_nacimiento': result[4].strftime('%Y-%m-%d'),
                'trabajador_ubigeo': result[5],
                'trabajador_telefono': result[6],
                'trabajador_sexo': result[7],
                'trabajador_estado_civil': result[8],
                'trabajador_path_doc_estado_civil': result[9],
                'trabajador_fecha_ingreso': result[10].strftime('%Y-%m-%d') if result[10] else None,
                'trabajador_fecha_ingreso_sistema': result[11].strftime('%Y-%m-%d') if result[11] else None,
                'trabajador_edad': result[12],
                'trabajador_record': float(result[13]) if result[13] is not None else 0.0,
                'trabajador_exp_previa': float(result[14]) if result[14] is not None else 0.0,
                'trabajador_total_anios_exp': float(result[15]) if result[15] is not None else 0.0
            }
            data.append(content)
            content = {}
        return data

    def create_trabajador(self, trabajador_id, trabajador_tipo_documento, trabajador_path_documento,
                      trabajador_nacionalidad, trabajador_fecha_nacimiento, trabajador_ubigeo,
                      trabajador_telefono, trabajador_sexo, trabajador_estado_civil,
                      trabajador_path_doc_estado_civil, trabajador_fecha_ingreso):

        data = {
            'trabajador_id': trabajador_id,
            'trabajador_tipo_documento': trabajador_tipo_documento,
            'trabajador_path_documento': trabajador_path_documento,
            'trabajador_nacionalidad': trabajador_nacionalidad,
            'trabajador_fecha_nacimiento': trabajador_fecha_nacimiento,
            'trabajador_ubigeo': trabajador_ubigeo,
            'trabajador_telefono': trabajador_telefono,
            'trabajador_sexo': trabajador_sexo,
            'trabajador_estado_civil': trabajador_estado_civil,
            'trabajador_path_doc_estado_civil': trabajador_path_doc_estado_civil,
            'trabajador_fecha_ingreso': trabajador_fecha_ingreso
        }
        query = """INSERT INTO trabajador (trabajador_id, trabajador_tipo_documento, trabajador_path_documento,
                   trabajador_nacionalidad, trabajador_fecha_nacimiento, trabajador_ubigeo,
                   trabajador_telefono, trabajador_sexo, trabajador_estado_civil, trabajador_path_doc_estado_civil, trabajador_fecha_ingreso) 
                   VALUES (%(trabajador_id)s, %(trabajador_tipo_documento)s, %(trabajador_path_documento)s,
                   %(trabajador_nacionalidad)s, %(trabajador_fecha_nacimiento)s, %(trabajador_ubigeo)s,
                   %(trabajador_telefono)s, %(trabajador_sexo)s, %(trabajador_estado_civil)s, %(trabajador_path_doc_estado_civil)s, %(trabajador_fecha_ingreso)s)"""
        cursor = self.mysql_pool.execute(query, data, commit=True)
        return trabajador_id

    def update_trabajador(self, trabajador_id, trabajador_tipo_documento, trabajador_path_documento,
                          trabajador_nacionalidad, trabajador_fecha_nacimiento, trabajador_ubigeo,
                          trabajador_telefono, trabajador_sexo, trabajador_estado_civil,
                          trabajador_path_doc_estado_civil, trabajador_fecha_ingreso):
        data = {
            'trabajador_id': trabajador_id,
            'trabajador_tipo_documento': trabajador_tipo_documento,
            'trabajador_path_documento': trabajador_path_documento,
            'trabajador_nacionalidad': trabajador_nacionalidad,
            'trabajador_fecha_nacimiento': trabajador_fecha_nacimiento,
            'trabajador_ubigeo': trabajador_ubigeo,
            'trabajador_telefono': trabajador_telefono,
            'trabajador_sexo': trabajador_sexo,
            'trabajador_estado_civil': trabajador_estado_civil,
            'trabajador_path_doc_estado_civil': trabajador_path_doc_estado_civil,
            'trabajador_fecha_ingreso': trabajador_fecha_ingreso
        }
        query = """UPDATE trabajador SET trabajador_tipo_documento = %(trabajador_tipo_documento)s,
                   trabajador_path_documento = %(trabajador_path_documento)s,
                   trabajador_nacionalidad = %(trabajador_nacionalidad)s,
                   trabajador_fecha_nacimiento = %(trabajador_fecha_nacimiento)s,
                   trabajador_ubigeo = %(trabajador_ubigeo)s,
                   trabajador_telefono = %(trabajador_telefono)s,
                   trabajador_sexo = %(trabajador_sexo)s,
                   trabajador_estado_civil = %(trabajador_estado_civil)s,
                   trabajador_path_doc_estado_civil = %(trabajador_path_doc_estado_civil)s,
                   trabajador_fecha_ingreso = %(trabajador_fecha_ingreso)s
                   WHERE trabajador_id = %(trabajador_id)s"""
        self.mysql_pool.execute(query, data, commit=True)
        return trabajador_id

    def delete_trabajador(self, trabajador_id):
        params = {'trabajador_id': trabajador_id}
        query = "DELETE FROM trabajador WHERE trabajador_id = %(trabajador_id)s"
        self.mysql_pool.execute(query, params, commit=True)
        return {'result': 1}
