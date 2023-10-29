from backend.models.mysql_connection_pool import MySQLPool

class ContratoModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()


    def create_contrato(self, id_trabajador, contrato_tipo, contrato_opcion, empleo_tipo, empleo_situacion, empleo_area, empleo_proyecto, empleo_departamento, empleo_cargo):
        try:
            data = {
                'id_trabajador': id_trabajador,
                'contrato_tipo': contrato_tipo,
                'contrato_opcion': contrato_opcion,
                'empleo_tipo': empleo_tipo,
                'empleo_situacion': empleo_situacion,
                'empleo_area': empleo_area,
                'empleo_proyecto': empleo_proyecto,
                'empleo_departamento': empleo_departamento,
                'empleo_cargo': empleo_cargo
            }
            query = """INSERT INTO contrato (id_trabajador, contrato_tipo, contrato_opcion, empleo_tipo, empleo_situacion, empleo_area, empleo_proyecto, empleo_departamento, empleo_cargo) 
                    VALUES (%(id_trabajador)s, %(contrato_tipo)s, %(contrato_opcion)s, %(empleo_tipo)s, %(empleo_situacion)s, %(empleo_area)s, %(empleo_proyecto)s, %(empleo_departamento)s, %(empleo_cargo)s)"""
            cursor = self.mysql_pool.execute(query, data, commit=True)
            return data
        except Exception as e:
            error_message = str(e)  # Obtener el mensaje de error específico
            return {'error': error_message}

    def update_contrato(self, id_trabajador, contrato_tipo, contrato_opcion, empleo_tipo, empleo_situacion, empleo_area, empleo_proyecto, empleo_departamento, empleo_cargo):
        data = {
            'id_trabajador': id_trabajador,
            'contrato_tipo': contrato_tipo,
            'contrato_opcion': contrato_opcion,
            'empleo_tipo': empleo_tipo,
            'empleo_situacion': empleo_situacion,
            'empleo_area': empleo_area,
            'empleo_proyecto': empleo_proyecto,
            'empleo_departamento': empleo_departamento,
            'empleo_cargo': empleo_cargo
        }
        query = """UPDATE contrato SET contrato_tipo = %(contrato_tipo)s, 
                   contrato_opcion = %(contrato_opcion)s, 
                   empleo_tipo = %(empleo_tipo)s, 
                   empleo_situacion = %(empleo_situacion)s, 
                   empleo_area = %(empleo_area)s ,
                   empleo_proyecto = %(empleo_proyecto)s,
                   empleo_departamento = %(empleo_departamento)s,
                   empleo_cargo = %(empleo_cargo)s
                   WHERE id_trabajador = %(id_trabajador)s"""
        self.mysql_pool.execute(query, data, commit=True)
        result = {'result': 1}
        return result

    def delete_contrato(self, id_trabajador):
        params = {'id_trabajador': id_trabajador}
        query = "DELETE FROM contrato WHERE id = %(id_trabajador)s"
        self.mysql_pool.execute(query, params, commit=True)
    
    def get_contrato(self, id_trabajador):
        query = "SELECT * FROM contrato WHERE id_trabajador = %(id_trabajador)s"
        params = {'id_trabajador': id_trabajador}
        rv = self.mysql_pool.execute(query, params)
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0],
                'id_trabajador': result[1],
                'contrato_tipo': result[2],
                'contrato_opcion': result[3],
                'empleo_tipo': result[4],
                'empleo_situacion': result[5],
                'empleo_area': result[6],
                'empleo_proyecto': result[7],
                'empleo_departamento': result[8],
                'empleo_cargo': result[9]
            }
            data.append(content)
            content = {}
        return data

    def get_contratos(self):
        query = "SELECT * FROM contrato"
        rv = self.mysql_pool.execute(query)
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0],
                'id_trabajador': result[1],
                'contrato_tipo': result[2],
                'contrato_opcion': result[3],
                'empleo_tipo': result[4],
                'empleo_situacion': result[5],
                'empleo_area': result[6],
                'empleo_proyecto': result[7],
                'empleo_departamento': result[8],
                'empleo_cargo': result[9]
            }
            data.append(content)
            content = {}
        return data
