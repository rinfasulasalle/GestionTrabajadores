from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from backend.models.mysql_contrato_model import ContratoModel

contrato_model = ContratoModel()
contrato_blueprint = Blueprint('contrato_blueprint', __name__)

@contrato_blueprint.route('/contrato', methods=['POST'])
@cross_origin()
def create_contrato():
    data = request.json
    id_trabajador = data['id_trabajador']
    contrato_tipo = data['contrato_tipo']
    contrato_opcion = data['contrato_opcion']
    empleo_tipo = data['empleo_tipo']
    empleo_situacion = data['empleo_situacion']
    empleo_area = data['empleo_area']
    empleo_proyecto = data['empleo_proyecto']
    empleo_departamento = data['empleo_departamento']
    empleo_cargo = data['empleo_cargo']
    empleo_proyecto_rol = data['empleo_proyecto_rol']
    content = contrato_model.create_contrato(id_trabajador, contrato_tipo, contrato_opcion, empleo_tipo, empleo_situacion, empleo_area, empleo_proyecto, empleo_departamento, empleo_cargo, empleo_proyecto_rol)
    return jsonify(content)

@contrato_blueprint.route('/contrato', methods=['PUT'])
@cross_origin()
def update_contrato():
    data = request.json
    id_trabajador = data['id_trabajador']
    contrato_tipo = data['contrato_tipo']
    contrato_opcion = data['contrato_opcion']
    empleo_tipo = data['empleo_tipo']
    empleo_situacion = data['empleo_situacion']
    empleo_area = data['empleo_area']
    empleo_proyecto = data['empleo_proyecto']
    empleo_departamento = data['empleo_departamento']
    empleo_cargo = data['empleo_cargo']
    empleo_proyecto_rol = data['empleo_proyecto_rol']
    content = contrato_model.update_contrato(id_trabajador, contrato_tipo, contrato_opcion, empleo_tipo, empleo_situacion, empleo_area, empleo_proyecto, empleo_departamento, empleo_cargo, empleo_proyecto_rol)
    return jsonify(content)

@contrato_blueprint.route('/contrato', methods=['DELETE'])
@cross_origin()
def delete_contrato():
    id_trabajador = request.json['id_trabajador']
    contrato_model.delete_contrato(id_trabajador)
    result = {'result': 1}
    return jsonify(result)

@contrato_blueprint.route('/contrato', methods=['GET'])
@cross_origin()
def get_contrato():
    id_trabajador = request.json['id_trabajador']
    return jsonify(contrato_model.get_contrato(id_trabajador))

@contrato_blueprint.route('/contratos', methods=['GET'])
@cross_origin()
def get_contratos():
    return jsonify(contrato_model.get_contratos())
