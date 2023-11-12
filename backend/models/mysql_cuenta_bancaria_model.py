from backend.models.mysql_connection_pool import MySQLPool

class CuentaBancariaModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def create_cuenta_bancaria(self, id_trabajador, cuenta_sueldo_codigo_cci, cuenta_sueldo_codigo, cuenta_sueldo_banco, cuenta_cts_codigo_cci, cuenta_cts_codigo, cuenta_cts_banco):
        try:
            data = {
                'id_trabajador': id_trabajador,
                'cuenta_sueldo_codigo_cci': cuenta_sueldo_codigo_cci,
                'cuenta_sueldo_codigo': cuenta_sueldo_codigo,
                'cuenta_sueldo_banco': cuenta_sueldo_banco,
                'cuenta_cts_codigo_cci': cuenta_cts_codigo_cci,
                'cuenta_cts_codigo': cuenta_cts_codigo,
                'cuenta_cts_banco': cuenta_cts_banco
            }
            query = """INSERT INTO cuenta_bancaria (id_trabajador, cuenta_sueldo_codigo_cci, cuenta_sueldo_codigo, cuenta_sueldo_banco, cuenta_cts_codigo_cci, cuenta_cts_codigo, cuenta_cts_banco) 
                    VALUES (%(id_trabajador)s, %(cuenta_sueldo_codigo_cci)s, %(cuenta_sueldo_codigo)s, %(cuenta_sueldo_banco)s, %(cuenta_cts_codigo_cci)s, %(cuenta_cts_codigo)s, %(cuenta_cts_banco)s)"""
            cursor = self.mysql_pool.execute(query, data, commit=True)
            return data
        except Exception as e:
                error_message = str(e)  # Obtener el mensaje de error específico
                return {'error': error_message}

    def update_cuenta_bancaria(self, id_trabajador, cuenta_sueldo_codigo_cci, cuenta_sueldo_codigo, cuenta_sueldo_banco, cuenta_cts_codigo_cci, cuenta_cts_codigo, cuenta_cts_banco):
        data = {
            'id_trabajador': id_trabajador,
            'cuenta_sueldo_codigo_cci': cuenta_sueldo_codigo_cci,
            'cuenta_sueldo_codigo': cuenta_sueldo_codigo,
            'cuenta_sueldo_banco': cuenta_sueldo_banco,
            'cuenta_cts_codigo_cci': cuenta_cts_codigo_cci,
            'cuenta_cts_codigo': cuenta_cts_codigo,
            'cuenta_cts_banco': cuenta_cts_banco
        }
        query = """
            UPDATE cuenta_bancaria
            SET cuenta_sueldo_codigo_cci = %(cuenta_sueldo_codigo_cci)s,
                cuenta_sueldo_codigo = %(cuenta_sueldo_codigo)s,
                cuenta_sueldo_banco = %(cuenta_sueldo_banco)s,
                cuenta_cts_codigo_cci = %(cuenta_cts_codigo_cci)s,
                cuenta_cts_codigo = %(cuenta_cts_codigo)s,
                cuenta_cts_banco = %(cuenta_cts_banco)s
            WHERE id_trabajador = %(id_trabajador)s
        """
        self.mysql_pool.execute(query, data, commit=True)
        result = {'result': 1}
        return result
    def delete_cuenta_bancaria(self, id_trabajador):
        params = {'id_trabajador': id_trabajador}
        query = "DELETE FROM cuenta_bancaria WHERE id_trabajador = %(id_trabajador)s"
        self.mysql_pool.execute(query, params, commit=True)

    def get_cuenta_bancaria(self, id_trabajador):
        query = "SELECT * FROM cuenta_bancaria WHERE id_trabajador = %(id_trabajador)s"
        params = {'id_trabajador': id_trabajador}
        rv = self.mysql_pool.execute(query, params)
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0],
                'id_trabajador': result[1],
                'cuenta_sueldo_codigo_cci': result[2],
                'cuenta_sueldo_codigo': result[3],
                'cuenta_sueldo_banco': result[4],
                'cuenta_cts_codigo_cci': result[5],
                'cuenta_cts_codigo': result[6],
                'cuenta_cts_banco':result[7]
            }
            data.append(content)
            content = {}
        return data
    
    def get_cuentas_bancarias(self):
        query = "SELECT * FROM cuenta_bancaria"
        rv = self.mysql_pool.execute(query)
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0],
                'id_trabajador': result[1],
                'cuenta_sueldo_codigo_cci': result[2],
                'cuenta_sueldo_codigo': result[3],
                'cuenta_sueldo_banco': result[4],
                'cuenta_cts_codigo_cci': result[5],
                'cuenta_cts_codigo': result[6],
                'cuenta_cts_banco':result[7]
            }
            data.append(content)
            content = {}
        return data
