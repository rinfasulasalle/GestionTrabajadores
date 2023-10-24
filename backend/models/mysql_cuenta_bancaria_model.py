from backend.models.mysql_connection_pool import MySQLPool

class CuentaBancariaModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def create_cuenta_bancaria(self, id_trabajador, cuenta_bancaria_codigo_cci, cuenta_bancaria_codigo, cuenta_bancaria_banco, cuenta_bancaria_tipo):
        data = {
            'id_trabajador': id_trabajador,
            'cuenta_bancaria_codigo_cci': cuenta_bancaria_codigo_cci,
            'cuenta_bancaria_codigo': cuenta_bancaria_codigo,
            'cuenta_bancaria_banco': cuenta_bancaria_banco,
            'cuenta_bancaria_tipo': cuenta_bancaria_tipo
        }
        query = """INSERT INTO cuenta_bancaria (id_trabajador, cuenta_bancaria_codigo_cci, cuenta_bancaria_codigo, cuenta_bancaria_banco, cuenta_bancaria_tipo) 
                   VALUES (%(id_trabajador)s, %(cuenta_bancaria_codigo_cci)s, %(cuenta_bancaria_codigo)s, %(cuenta_bancaria_banco)s, %(cuenta_bancaria_tipo)s)"""
        cursor = self.mysql_pool.execute(query, data, commit=True)
        return data

    def update_cuenta_bancaria(self, id, cuenta_bancaria_codigo_cci, cuenta_bancaria_codigo, cuenta_bancaria_banco, cuenta_bancaria_tipo):
        data = {
            'id': id,
            'cuenta_bancaria_codigo_cci': cuenta_bancaria_codigo_cci,
            'cuenta_bancaria_codigo': cuenta_bancaria_codigo,
            'cuenta_bancaria_banco': cuenta_bancaria_banco,
            'cuenta_bancaria_tipo': cuenta_bancaria_tipo
        }
        query = """UPDATE cuenta_bancaria SET cuenta_bancaria_codigo_cci = %(cuenta_bancaria_codigo_cci)s, 
                   cuenta_bancaria_codigo = %(cuenta_bancaria_codigo)s, 
                   cuenta_bancaria_banco = %(cuenta_bancaria_banco)s, 
                   cuenta_bancaria_tipo = %(cuenta_bancaria_tipo)s
                   WHERE id = %(id)s"""
        self.mysql_pool.execute(query, data, commit=True)
        result = {'result': 1}
        return result

    def delete_cuenta_bancaria(self, id):
        params = {'id': id}
        query = "DELETE FROM cuenta_bancaria WHERE id = %(id)s"
        self.mysql_pool.execute(query, params, commit=True)

    def get_cuenta_bancaria(self, id):
        query = "SELECT * FROM cuenta_bancaria WHERE id = %(id)s"
        params = {'id': id}
        rv = self.mysql_pool.execute(query, params)
        data = []
        content = {}
        for result in rv:
            content = {
                'id': result[0],
                'id_trabajador': result[1],
                'cuenta_bancaria_codigo_cci': result[2],
                'cuenta_bancaria_codigo': result[3],
                'cuenta_bancaria_banco': result[4],
                'cuenta_bancaria_tipo': result[5]
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
                'cuenta_bancaria_codigo_cci': result[2],
                'cuenta_bancaria_codigo': result[3],
                'cuenta_bancaria_banco': result[4],
                'cuenta_bancaria_tipo': result[5]
            }
            data.append(content)
            content = {}
        return data
