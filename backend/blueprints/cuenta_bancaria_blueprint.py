from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from backend.models.mysql_cuenta_bancaria_model import CuentaBancariaModel

cuenta_bancaria_model = CuentaBancariaModel()
cuenta_bancaria_blueprint = Blueprint('cuenta_bancaria_blueprint', __name__)

@cuenta_bancaria_blueprint.route('/cuenta_bancaria', methods=['POST'])
@cross_origin()
def create_cuenta_bancaria():
    data = request.json
    id_trabajador = data['id_trabajador']
    cuenta_bancaria_codigo_cci = data.get('cuenta_bancaria_codigo_cci', None)
    cuenta_bancaria_codigo = data.get('cuenta_bancaria_codigo', None)
    cuenta_bancaria_banco = data['cuenta_bancaria_banco']
    cuenta_bancaria_tipo = data['cuenta_bancaria_tipo']
    content = cuenta_bancaria_model.create_cuenta_bancaria(id_trabajador, cuenta_bancaria_codigo_cci, cuenta_bancaria_codigo, cuenta_bancaria_banco, cuenta_bancaria_tipo)
    return jsonify(content)

@cuenta_bancaria_blueprint.route('/cuenta_bancaria', methods=['PUT'])
@cross_origin()
def update_cuenta_bancaria():
    data = request.json
    id = data['id']
    cuenta_bancaria_codigo_cci = data.get('cuenta_bancaria_codigo_cci', None)
    cuenta_bancaria_codigo = data.get('cuenta_bancaria_codigo', None)
    cuenta_bancaria_banco = data['cuenta_bancaria_banco']
    cuenta_bancaria_tipo = data['cuenta_bancaria_tipo']
    content = cuenta_bancaria_model.update_cuenta_bancaria(id, cuenta_bancaria_codigo_cci, cuenta_bancaria_codigo, cuenta_bancaria_banco, cuenta_bancaria_tipo)
    return jsonify(content)

@cuenta_bancaria_blueprint.route('/cuenta_bancaria', methods=['DELETE'])
@cross_origin()
def delete_cuenta_bancaria():
    id = request.json['id']
    cuenta_bancaria_model.delete_cuenta_bancaria(id)
    result = {'result': 1}
    return jsonify(result)

@cuenta_bancaria_blueprint.route('/cuenta_bancaria', methods=['GET'])
@cross_origin()
def get_cuenta_bancaria():
    id = request.json['id']
    return jsonify(cuenta_bancaria_model.get_cuenta_bancaria(id))

@cuenta_bancaria_blueprint.route('/cuentas_bancarias', methods=['GET'])
@cross_origin()
def get_cuentas_bancarias():
    return jsonify(cuenta_bancaria_model.get_cuentas_bancarias())
