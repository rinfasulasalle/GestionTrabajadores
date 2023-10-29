from backend.models.mysql_connection_pool import MySQLPool

class TrabajadorModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_trabajadores(self):
        query = "SELECT * FROM trabajador"
        rv = self.mysql_pool.execute(query)
        data = []
        content = {}
        for result in rv:
            content = {
                'trabajador_id': result[0],
                'trabajador_fecha_nacimiento': result[1].strftime("%Y-%m-%d"),
                'trabajador_tipo_documento': result[2],
                'trabajador_path_documento': result[3],
                'trabajador_nacionalidad': result[4],
                'trabajador_ubigeo': result[5],
                'trabajador_estado_civil': result[6],
                'trabajador_path_doc_estado_civil': result[7],
                'trabajador_fecha_ingreso': result[8].strftime("%Y-%m-%d"),
                'trabajador_fecha_ingreso_sistema': result[9].strftime("%Y-%m-%d"),
                'trabajador_edad': result[10],
                'trabajador_record': float(result[11]) if result[11] is not None else 0.0,
                'trabajador_exp_previa': float(result[12]) if result[12] is not None else 0.0,
                'trabajador_total_anios_exp': float(result[13]) if result[13] is not None else 0.0
            }
            data.append(content)
            content = {}
        return data

    def get_trabajador(self, trabajador_id):
        query = "SELECT * FROM trabajador WHERE trabajador_id = %(trabajador_id)s"
        params = {'trabajador_id': trabajador_id}
        rv = self.mysql_pool.execute(query, params)
        data = []
        content = {}
        for result in rv:
            content = {
                'trabajador_id': result[0],
                'trabajador_fecha_nacimiento': result[1].strftime("%Y-%m-%d"),
                'trabajador_tipo_documento': result[2],
                'trabajador_path_documento': result[3],
                'trabajador_nacionalidad': result[4],
                'trabajador_ubigeo': result[5],
                'trabajador_estado_civil': result[6],
                'trabajador_path_doc_estado_civil': result[7],
                'trabajador_fecha_ingreso': result[8].strftime("%Y-%m-%d"),
                'trabajador_fecha_ingreso_sistema': result[9].strftime("%Y-%m-%d"),
                'trabajador_edad': result[10],
                'trabajador_record': float(result[11]) if result[11] is not None else 0.0,
                'trabajador_exp_previa': float(result[12]) if result[12] is not None else 0.0,
                'trabajador_total_anios_exp': float(result[13]) if result[13] is not None else 0.0
            }
            data.append(content)
            content = {}
        return data

    def create_trabajador(self, trabajador_id, trabajador_fecha_nacimiento, trabajador_tipo_documento, trabajador_path_documento, trabajador_nacionalidad, trabajador_ubigeo, trabajador_estado_civil, trabajador_path_doc_estado_civil, trabajador_fecha_ingreso, trabajador_exp_previa):
        try:
            data = {
                'trabajador_id': trabajador_id,
                'trabajador_fecha_nacimiento': trabajador_fecha_nacimiento,
                'trabajador_tipo_documento': trabajador_tipo_documento,
                'trabajador_path_documento': trabajador_path_documento,
                'trabajador_nacionalidad': trabajador_nacionalidad,
                'trabajador_ubigeo': trabajador_ubigeo,
                'trabajador_estado_civil': trabajador_estado_civil,
                'trabajador_path_doc_estado_civil': trabajador_path_doc_estado_civil,
                'trabajador_fecha_ingreso': trabajador_fecha_ingreso,
                'trabajador_exp_previa': trabajador_exp_previa
            }
            query = """INSERT INTO trabajador (trabajador_id, trabajador_fecha_nacimiento, trabajador_tipo_documento, trabajador_path_documento, trabajador_nacionalidad, trabajador_ubigeo, trabajador_estado_civil, trabajador_path_doc_estado_civil, trabajador_fecha_ingreso,trabajador_exp_previa) 
                    VALUES (%(trabajador_id)s, %(trabajador_fecha_nacimiento)s, %(trabajador_tipo_documento)s, %(trabajador_path_documento)s, %(trabajador_nacionalidad)s, %(trabajador_ubigeo)s, %(trabajador_estado_civil)s, %(trabajador_path_doc_estado_civil)s, %(trabajador_fecha_ingreso)s, %(trabajador_exp_previa)s)"""
            cursor = self.mysql_pool.execute(query, data, commit=True)
            return data
        except Exception as e:
                error_message = str(e)  # Obtener el mensaje de error específico
                return {'error': error_message}

    def update_trabajador(self, trabajador_id, trabajador_fecha_nacimiento, trabajador_tipo_documento, trabajador_path_documento, trabajador_nacionalidad, trabajador_ubigeo, trabajador_estado_civil, trabajador_path_doc_estado_civil, trabajador_fecha_ingreso, trabajador_exp_previa):
        data = {
            'trabajador_id': trabajador_id,
            'trabajador_fecha_nacimiento': trabajador_fecha_nacimiento,
            'trabajador_tipo_documento': trabajador_tipo_documento,
            'trabajador_path_documento': trabajador_path_documento,
            'trabajador_nacionalidad': trabajador_nacionalidad,
            'trabajador_ubigeo': trabajador_ubigeo,
            'trabajador_estado_civil': trabajador_estado_civil,
            'trabajador_path_doc_estado_civil': trabajador_path_doc_estado_civil,
            'trabajador_fecha_ingreso': trabajador_fecha_ingreso,
            'trabajador_exp_previa': trabajador_exp_previa
        }
        query = """UPDATE trabajador SET trabajador_tipo_documento = %(trabajador_tipo_documento)s, 
                   trabajador_path_documento = %(trabajador_path_documento)s, 
                   trabajador_nacionalidad = %(trabajador_nacionalidad)s, 
                   trabajador_ubigeo = %(trabajador_ubigeo)s, 
                   trabajador_estado_civil = %(trabajador_estado_civil)s ,
                   trabajador_path_doc_estado_civil = %(trabajador_path_doc_estado_civil)s,
                   trabajador_fecha_ingreso = %(trabajador_fecha_ingreso)s,
                   trabajador_exp_previa = %(trabajador_exp_previa)s
                   WHERE trabajador_id = %(trabajador_id)s"""
        self.mysql_pool.execute(query, data, commit=True)
        result = {'result': 1}
        return result

    def delete_trabajador(self, trabajador_id):
        params = {'trabajador_id': trabajador_id}
        query = "DELETE FROM trabajador WHERE trabajador_id = %(trabajador_id)s"
        self.mysql_pool.execute(query, params, commit=True)
        result = {'result': 1}
        return result
