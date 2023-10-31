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

    def get_all_trabajadores(self):
            query = """
            SELECT 
                u.id AS usuario_id, 
                u.usuario_nombres,
                u.usuario_apellidos,
                u.usuario_correo,
                u.usuario_sexo,
                u.usuario_telefono,
                t.trabajador_id, 
                t.trabajador_fecha_nacimiento, 
                t.trabajador_tipo_documento, 
                t.trabajador_path_documento, 
                t.trabajador_nacionalidad, 
                t.trabajador_ubigeo, 
                t.trabajador_estado_civil, 
                t.trabajador_path_doc_estado_civil, 
                t.trabajador_fecha_ingreso, 
                t.trabajador_fecha_ingreso_sistema, 
                t.trabajador_edad, 
                t.trabajador_record, 
                t.trabajador_exp_previa, 
                t.trabajador_total_anios_exp, 
                c.contrato_tipo, 
                c.contrato_opcion, 
                c.empleo_tipo, 
                c.empleo_situacion, 
                c.empleo_area, 
                c.empleo_proyecto, 
                c.empleo_departamento, 
                c.empleo_cargo, 
                s.sueldo_valor_básico, 
                s.sueldo_asigfam_porcentaje, 
                s.sueldo_asignacion_familiar, 
                s.sueldo_bono_porcentaje, 
                s.sueldo_monto_bono, 
                s.sueldo_mensual, 
                s.sueldo_anual, 
                cb.cuenta_bancaria_codigo_cci, 
                cb.cuenta_bancaria_codigo, 
                cb.cuenta_bancaria_banco, 
                cb.cuenta_bancaria_tipo, 
                d.direccion_pais, 
                d.direccion_departamento, 
                d.direccion_provincia, 
                d.direccion_distrito, 
                d.direccion_detalle, 
                e.estudio_nivel_educativo, 
                e.estudio_situacion_especial, 
                e.estudio_regimen_laboral, 
                e.estudio_regimen_laboral_aseguramiento, 
                e.estudio_institucion, 
                e.estudio_carrera_educativa, 
                e.estudio_capacitacion, 
                e.estudio_especializacion, 
                e.estudio_id_colegiatura, 
                e.estudio_fecha_colegiatura, 
                e.estudio_sede_colegiatura, 
                e.estudio_condicion
            FROM 
                usuario u
                JOIN trabajador t ON u.id = t.trabajador_id
                JOIN contrato c ON t.trabajador_id = c.id_trabajador
                JOIN sueldo s ON t.trabajador_id = s.id_trabajador
                JOIN cuenta_bancaria cb ON t.trabajador_id = cb.id_trabajador
                JOIN direccion d ON t.trabajador_id = d.id_trabajador
                JOIN estudio e ON t.trabajador_id = e.id_trabajador;
            """
            rv = self.mysql_pool.execute(query)
            data = []
            for result in rv:
                content = {
                    'usuario_id': result[0],
                    'usuario_nombres': result[1],
                    'usuario_apellidos': result[2],
                    'usuario_correo': result[3],
                    'usuario_sexo': result[4],
                    'usuario_telefono': result[5],
                    'trabajador_id': result[6],
                    'trabajador_fecha_nacimiento': result[7].strftime("%Y-%m-%d"),
                    'trabajador_tipo_documento': result[8],
                    'trabajador_path_documento': result[9],
                    'trabajador_nacionalidad': result[10],
                    'trabajador_ubigeo': result[11],
                    'trabajador_estado_civil': result[12],
                    'trabajador_path_doc_estado_civil': result[13],
                    'trabajador_fecha_ingreso': result[14].strftime("%Y-%m-%d"),
                    'trabajador_fecha_ingreso_sistema': result[15].strftime("%Y-%m-%d"),
                    'trabajador_edad': result[16],
                    'trabajador_record': float(result[17]) if result[17] is not None else 0.0,
                    'trabajador_exp_previa': float(result[18]) if result[18] is not None else 0.0,
                    'trabajador_total_anios_exp': float(result[19]) if result[19] is not None else 0.0,
                    'contrato_tipo': result[20],
                    'contrato_opcion': result[21],
                    'empleo_tipo': result[22],
                    'empleo_situacion': result[23],
                    'empleo_area': result[24],
                    'empleo_proyecto': result[25],
                    'empleo_departamento': result[26],
                    'empleo_cargo': result[27],
                    'sueldo_valor_básico': float(result[28]) if result[28] is not None else 0.0,
                    'sueldo_asigfam_porcentaje': float(result[29]) if result[29] is not None else 0.0,
                    'sueldo_asignacion_familiar': float(result[30]) if result[30] is not None else 0.0,
                    'sueldo_bono_porcentaje': float(result[31]) if result[31] is not None else 0.0,
                    'sueldo_monto_bono': float(result[32]) if result[32] is not None else 0.0,
                    'sueldo_mensual': float(result[33]) if result[33] is not None else 0.0,
                    'sueldo_anual': float(result[34]) if result[34] is not None else 0.0,
                    'cuenta_bancaria_codigo_cci': result[35],
                    'cuenta_bancaria_codigo': result[36],
                    'cuenta_bancaria_banco': result[37],
                    'cuenta_bancaria_tipo': result[38],
                    'direccion_pais': result[39],
                    'direccion_departamento': result[40],
                    'direccion_provincia': result[41],
                    'direccion_distrito': result[42],
                    'direccion_detalle': result[43],
                    'estudio_nivel_educativo': result[44],
                    'estudio_situacion_especial': result[45],
                    'estudio_regimen_laboral': result[46],
                    'estudio_regimen_laboral_aseguramiento': result[47],
                    'estudio_institucion': result[48],
                    'estudio_carrera_educativa': result[49],
                    'estudio_capacitacion': result[50],
                    'estudio_especializacion': result[51],
                    'estudio_id_colegiatura': result[52],
                    'estudio_fecha_colegiatura': result[53].strftime("%Y-%m-%d") if result[53] is not None else None,
                    'estudio_sede_colegiatura': result[54],
                    'estudio_condicion': result[55]
        }
                data.append(content)
                content = {}
            return data