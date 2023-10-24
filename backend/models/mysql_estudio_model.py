from backend.models.mysql_connection_pool import MySQLPool

class EstudioModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def create_estudio(self, id_trabajador, estudio_nivel_educativo, estudio_situacion_especial, estudio_regimen_laboral,
                       estudio_regimen_laboral_aseguramiento, estudio_institucion, estudio_carrera_educativa,
                       estudio_capacitacion, estudio_especializacion, estudio_id_colegiatura,
                       estudio_fecha_colegiatura, estudio_sede_colegiatura, estudio_condicion):
        data = {
            'id_trabajador': id_trabajador,
            'estudio_nivel_educativo': estudio_nivel_educativo,
            'estudio_situacion_especial': estudio_situacion_especial,
            'estudio_regimen_laboral': estudio_regimen_laboral,
            'estudio_regimen_laboral_aseguramiento': estudio_regimen_laboral_aseguramiento,
            'estudio_institucion': estudio_institucion,
            'estudio_carrera_educativa': estudio_carrera_educativa,
            'estudio_capacitacion': estudio_capacitacion,
            'estudio_especializacion': estudio_especializacion,
            'estudio_id_colegiatura': estudio_id_colegiatura,
            'estudio_fecha_colegiatura': estudio_fecha_colegiatura,
            'estudio_sede_colegiatura': estudio_sede_colegiatura,
            'estudio_condicion': estudio_condicion
        }
        query = """INSERT INTO estudio (id_trabajador, estudio_nivel_educativo, estudio_situacion_especial,
                   estudio_regimen_laboral, estudio_regimen_laboral_aseguramiento, estudio_institucion,
                   estudio_carrera_educativa, estudio_capacitacion, estudio_especializacion, estudio_id_colegiatura,
                   estudio_fecha_colegiatura, estudio_sede_colegiatura, estudio_condicion) 
                   VALUES (%(id_trabajador)s, %(estudio_nivel_educativo)s, %(estudio_situacion_especial)s,
                   %(estudio_regimen_laboral)s, %(estudio_regimen_laboral_aseguramiento)s, %(estudio_institucion)s,
                   %(estudio_carrera_educativa)s, %(estudio_capacitacion)s, %(estudio_especializacion)s,
                   %(estudio_id_colegiatura)s, %(estudio_fecha_colegiatura)s, %(estudio_sede_colegiatura)s,
                   %(estudio_condicion)s)"""
        cursor = self.mysql_pool.execute(query, data, commit=True)
        return data

    def update_estudio(self, id_trabajador, estudio_nivel_educativo, estudio_situacion_especial, estudio_regimen_laboral,
                       estudio_regimen_laboral_aseguramiento, estudio_institucion, estudio_carrera_educativa,
                       estudio_capacitacion, estudio_especializacion, estudio_id_colegiatura,
                       estudio_fecha_colegiatura, estudio_sede_colegiatura, estudio_condicion):
        data = {
            'id_trabajador': id_trabajador,
            'estudio_nivel_educativo': estudio_nivel_educativo,
            'estudio_situacion_especial': estudio_situacion_especial,
            'estudio_regimen_laboral': estudio_regimen_laboral,
            'estudio_regimen_laboral_aseguramiento': estudio_regimen_laboral_aseguramiento,
            'estudio_institucion': estudio_institucion,
            'estudio_carrera_educativa': estudio_carrera_educativa,
            'estudio_capacitacion': estudio_capacitacion,
            'estudio_especializacion': estudio_especializacion,
            'estudio_id_colegiatura': estudio_id_colegiatura,
            'estudio_fecha_colegiatura': estudio_fecha_colegiatura,
            'estudio_sede_colegiatura': estudio_sede_colegiatura,
            'estudio_condicion': estudio_condicion
        }
        query = """UPDATE estudio SET estudio_nivel_educativo = %(estudio_nivel_educativo)s, 
                   estudio_situacion_especial = %(estudio_situacion_especial)s, 
                   estudio_regimen_laboral = %(estudio_regimen_laboral)s, 
                   estudio_regimen_laboral_aseguramiento = %(estudio_regimen_laboral_aseguramiento)s, 
                   estudio_institucion = %(estudio_institucion)s, 
                   estudio_carrera_educativa = %(estudio_carrera_educativa)s, 
                   estudio_capacitacion = %(estudio_capacitacion)s, 
                   estudio_especializacion = %(estudio_especializacion)s, 
                   estudio_id_colegiatura = %(estudio_id_colegiatura)s, 
                   estudio_fecha_colegiatura = %(estudio_fecha_colegiatura)s, 
                   estudio_sede_colegiatura = %(estudio_sede_colegiatura)s, 
                   estudio_condicion = %(estudio_condicion)s 
                   WHERE id_trabajador = %(id_trabajador)s"""
        self.mysql_pool.execute(query, data, commit=True)
        result = {'result': 1}
        return result

    def delete_estudio(self, id_trabajador):
        params = {'id_trabajador': id_trabajador}
        query = "DELETE FROM estudio WHERE id_trabajador = %(id_trabajador)s"
        self.mysql_pool.execute(query, params, commit=True)
        
    def get_estudio(self, id_trabajador):
        query = "SELECT * FROM estudio WHERE id_trabajador = %(id_trabajador)s"
        params = {'id_trabajador': id_trabajador}
        rv = self.mysql_pool.execute(query, params)
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0],
                'id_trabajador': result[1],
                'estudio_nivel_educativo': result[2],
                'estudio_situacion_especial': result[3],
                'estudio_regimen_laboral': result[4],
                'estudio_regimen_laboral_aseguramiento': result[5],
                'estudio_institucion': result[6],
                'estudio_carrera_educativa': result[7],
                'estudio_capacitacion': result[8],
                'estudio_especializacion': result[9],
                'estudio_id_colegiatura': result[10],
                'estudio_fecha_colegiatura': result[11].strftime('%Y-%m-%d'),
                'estudio_sede_colegiatura': result[12],
                'estudio_condicion': result[13]
            }
            data.append(content)
            content = {}
        return data

    def get_estudios(self):
        query = "SELECT * FROM estudio"
        rv = self.mysql_pool.execute(query)
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0],
                'id_trabajador': result[1],
                'estudio_nivel_educativo': result[2],
                'estudio_situacion_especial': result[3],
                'estudio_regimen_laboral': result[4],
                'estudio_regimen_laboral_aseguramiento': result[5],
                'estudio_institucion': result[6],
                'estudio_carrera_educativa': result[7],
                'estudio_capacitacion': result[8],
                'estudio_especializacion': result[9],
                'estudio_id_colegiatura': result[10],
                'estudio_fecha_colegiatura': result[11].strftime('%Y-%m-%d'),
                'estudio_sede_colegiatura': result[12],
                'estudio_condicion': result[13]
            }
            data.append(content)
            content = {}
        return data
