from backend.models.mysql_connection_pool import MySQLPool

class SueldoModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def create_sueldo(self, id_trabajador, sueldo_valor_básico, sueldo_asigfam_porcentaje, sueldo_bono_porcentaje):
        try:
            data = {
                'id_trabajador': id_trabajador,
                'sueldo_valor_básico': sueldo_valor_básico,
                'sueldo_asigfam_porcentaje': sueldo_asigfam_porcentaje,
                'sueldo_bono_porcentaje': sueldo_bono_porcentaje
            }
            query = """INSERT INTO sueldo (id_trabajador, sueldo_valor_básico, sueldo_asigfam_porcentaje, sueldo_bono_porcentaje) 
                    VALUES (%(id_trabajador)s, %(sueldo_valor_básico)s, %(sueldo_asigfam_porcentaje)s, %(sueldo_bono_porcentaje)s)"""
            cursor = self.mysql_pool.execute(query, data, commit=True)
            return data
        except Exception as e:
            error_message = str(e)  # Obtener el mensaje de error específico
            return {'error': error_message}

    def update_sueldo(self, id_trabajador, sueldo_valor_básico, sueldo_asigfam_porcentaje, sueldo_bono_porcentaje):
        data = {
            'id_trabajador': id_trabajador,
            'sueldo_valor_básico': sueldo_valor_básico,
            'sueldo_asigfam_porcentaje': sueldo_asigfam_porcentaje,
            'sueldo_bono_porcentaje': sueldo_bono_porcentaje
        }
        query = """UPDATE sueldo SET sueldo_valor_básico = %(sueldo_valor_básico)s, 
                   sueldo_asigfam_porcentaje = %(sueldo_asigfam_porcentaje)s, 
                   sueldo_bono_porcentaje = %(sueldo_bono_porcentaje)s
                   WHERE id_trabajador = %(id_trabajador)s"""
        self.mysql_pool.execute(query, data, commit=True)
        result = {'result': 1}
        return result

    def delete_sueldo(self, id_trabajador):
        params = {'id_trabajador': id_trabajador}
        query = "DELETE FROM sueldo WHERE id = %(id_trabajador)s"
        self.mysql_pool.execute(query, params, commit=True)

    def get_sueldo(self, id_trabajador):
        query = "SELECT * FROM sueldo WHERE id_trabajador = %(id_trabajador)s"
        params = {'id_trabajador': id_trabajador}
        rv = self.mysql_pool.execute(query, params)
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0],
                'id_trabajador': result[1],
                'sueldo_valor_básico': float(result[2]),
                'sueldo_asigfam_porcentaje': float(result[3]) if result[3] is not None else None,
                'sueldo_asignacion_familiar': float(result[4]) if result[4] is not None else None,
                'sueldo_bono_porcentaje': float(result[5]) if result[5] is not None else None,
                'sueldo_monto_bono': float(result[6]) if result[6] is not None else None,
                'sueldo_mensual': float(result[7]) if result[7] is not None else None,
                'sueldo_anual': float(result[8]) if result[8] is not None else None,
            }
            data.append(content)
            content = {}
        return data

    def get_sueldos(self):
        query = "SELECT * FROM sueldo"
        rv = self.mysql_pool.execute(query)
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0],
                'id_trabajador': result[1],
                'sueldo_valor_básico': float(result[2]),
                'sueldo_asigfam_porcentaje': float(result[3]) if result[3] is not None else None,
                'sueldo_asignacion_familiar': float(result[4]) if result[4] is not None else None,
                'sueldo_bono_porcentaje': float(result[5]) if result[5] is not None else None,
                'sueldo_monto_bono': float(result[6]) if result[6] is not None else None,
                'sueldo_mensual': float(result[7]) if result[7] is not None else None,
                'sueldo_anual': float(result[8]) if result[8] is not None else None,
            }
            data.append(content)
            content = {}
        return data
