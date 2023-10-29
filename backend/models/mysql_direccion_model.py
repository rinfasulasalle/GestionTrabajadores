from backend.models.mysql_connection_pool import MySQLPool

class DireccionModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def create_direccion(self, id_trabajador, direccion_pais, direccion_departamento, direccion_provincia, direccion_distrito, direccion_detalle):
        try:
            data = {
                'id_trabajador': id_trabajador,
                'direccion_pais': direccion_pais,
                'direccion_departamento': direccion_departamento,
                'direccion_provincia': direccion_provincia,
                'direccion_distrito': direccion_distrito,
                'direccion_detalle': direccion_detalle
            }
            query = """INSERT INTO direccion (id_trabajador, direccion_pais, direccion_departamento, direccion_provincia, direccion_distrito, direccion_detalle) 
                    VALUES (%(id_trabajador)s, %(direccion_pais)s, %(direccion_departamento)s, %(direccion_provincia)s, %(direccion_distrito)s, %(direccion_detalle)s)"""
            cursor = self.mysql_pool.execute(query, data, commit=True)
            return data
        except Exception as e:
                error_message = str(e)  # Obtener el mensaje de error específico
                return {'error': error_message}

    def update_direccion(self, id_trabajador, direccion_pais, direccion_departamento, direccion_provincia, direccion_distrito, direccion_detalle):
        data = {
            'id_trabajador': id_trabajador,
            'direccion_pais': direccion_pais,
            'direccion_departamento': direccion_departamento,
            'direccion_provincia': direccion_provincia,
            'direccion_distrito': direccion_distrito,
            'direccion_detalle': direccion_detalle
        }
        query = """UPDATE direccion SET direccion_pais = %(direccion_pais)s, 
                   direccion_departamento = %(direccion_departamento)s, 
                   direccion_provincia = %(direccion_provincia)s, 
                   direccion_distrito = %(direccion_distrito)s, 
                   direccion_detalle = %(direccion_detalle)s
                   WHERE id_trabajador = %(id_trabajador)s"""
        self.mysql_pool.execute(query, data, commit=True)
        result = {'result': 1}
        return result

    def delete_direccion(self, id_trabajador):
        params = {'id_trabajador': id_trabajador}
        query = "DELETE FROM direccion WHERE id_trabajador = %(id_trabajador)s"
        self.mysql_pool.execute(query, params, commit=True)
    
    def get_direccion(self, id_trabajador):
        query = "SELECT * FROM direccion WHERE id_trabajador = %(id_trabajador)s"
        params = {'id_trabajador': id_trabajador}
        rv = self.mysql_pool.execute(query, params)
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0],
                'id_trabajador': result[1],
                'direccion_pais': result[2],
                'direccion_departamento': result[3],
                'direccion_provincia': result[4],
                'direccion_distrito': result[5],
                'direccion_detalle': result[6]
            }
            data.append(content)
            content = {}
        return data

    def get_direcciones(self):
        query = "SELECT * FROM direccion"
        rv = self.mysql_pool.execute(query)
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0],
                'id_trabajador': result[1],
                'direccion_pais': result[2],
                'direccion_departamento': result[3],
                'direccion_provincia': result[4],
                'direccion_distrito': result[5],
                'direccion_detalle': result[6]
            }
            data.append(content)
            content = {}
        return data
