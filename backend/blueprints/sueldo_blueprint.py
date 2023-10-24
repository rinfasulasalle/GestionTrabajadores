from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from backend.models.mysql_sueldo_model import SueldoModel

sueldo_model = SueldoModel()
sueldo_blueprint = Blueprint('sueldo_blueprint', __name__)

@sueldo_blueprint.route('/sueldo', methods=['POST'])
@cross_origin()
def create_sueldo():
    data = request.json
    id_trabajador = data['id_trabajador']
    sueldo_valor_básico = data['sueldo_valor_básico']
    sueldo_asigfam_porcentaje = data['sueldo_asigfam_porcentaje']
    sueldo_bono_porcentaje = data['sueldo_bono_porcentaje']
    content = sueldo_model.create_sueldo(id_trabajador, sueldo_valor_básico, sueldo_asigfam_porcentaje, sueldo_bono_porcentaje)
    return jsonify(content)

@sueldo_blueprint.route('/sueldo', methods=['PUT'])
@cross_origin()
def update_sueldo():
    data = request.json
    id = data['id']
    sueldo_valor_básico = data['sueldo_valor_básico']
    sueldo_asigfam_porcentaje = data['sueldo_asigfam_porcentaje']
    sueldo_bono_porcentaje = data['sueldo_bono_porcentaje']
    content = sueldo_model.update_sueldo(id, sueldo_valor_básico, sueldo_asigfam_porcentaje, sueldo_bono_porcentaje)
    return jsonify(content)

@sueldo_blueprint.route('/sueldo', methods=['DELETE'])
@cross_origin()
def delete_sueldo():
    id = request.json['id']
    sueldo_model.delete_sueldo(id)
    result = {'result': 1}
    return jsonify(result)

@sueldo_blueprint.route('/sueldo', methods=['GET'])
@cross_origin()
def get_sueldo():
    id = request.json['id']
    return jsonify(sueldo_model.get_sueldo(id))

@sueldo_blueprint.route('/sueldos', methods=['GET'])
@cross_origin()
def get_sueldos():
    return jsonify(sueldo_model.get_sueldos())
