from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from backend.models.mysql_trabajador_model import TrabajadorModel

trabajador_model = TrabajadorModel()
trabajador_blueprint = Blueprint('trabajador_blueprint', __name__)

@trabajador_blueprint.route('/trabajador', methods=['POST'])
@cross_origin()
def create_trabajador():
    data = request.json
    trabajador_id = data['trabajador_id']
    trabajador_fecha_nacimiento = data['trabajador_fecha_nacimiento']
    trabajador_tipo_documento = data['trabajador_tipo_documento']
    trabajador_path_documento = data['trabajador_path_documento']
    trabajador_nacionalidad = data['trabajador_nacionalidad']
    trabajador_ubigeo = data['trabajador_ubigeo']
    trabajador_estado_civil = data['trabajador_estado_civil']
    trabajador_path_doc_estado_civil = data['trabajador_path_doc_estado_civil']
    trabajador_fecha_ingreso = data['trabajador_fecha_ingreso']
    trabajador_exp_previa = data['trabajador_exp_previa']

    content = trabajador_model.create_trabajador(trabajador_id, trabajador_fecha_nacimiento, trabajador_tipo_documento, trabajador_path_documento, trabajador_nacionalidad, trabajador_ubigeo, trabajador_estado_civil, trabajador_path_doc_estado_civil, trabajador_fecha_ingreso,trabajador_exp_previa)
    return jsonify(content)

@trabajador_blueprint.route('/trabajador', methods=['PUT'])
@cross_origin()
def update_trabajador():
    data = request.json
    trabajador_id = data['trabajador_id']
    trabajador_fecha_nacimiento = data['trabajador_fecha_nacimiento']
    trabajador_tipo_documento = data['trabajador_tipo_documento']
    trabajador_path_documento = data['trabajador_path_documento']
    trabajador_nacionalidad = data['trabajador_nacionalidad']
    trabajador_ubigeo = data['trabajador_ubigeo']
    trabajador_estado_civil = data['trabajador_estado_civil']
    trabajador_path_doc_estado_civil = data['trabajador_path_doc_estado_civil']
    trabajador_fecha_ingreso = data['trabajador_fecha_ingreso']
    trabajador_exp_previa = data['trabajador_exp_previa']
    content = trabajador_model.update_trabajador(trabajador_id, trabajador_fecha_nacimiento, trabajador_tipo_documento, trabajador_path_documento, trabajador_nacionalidad, trabajador_ubigeo, trabajador_estado_civil, trabajador_path_doc_estado_civil, trabajador_fecha_ingreso,trabajador_exp_previa)    
    return jsonify(content)

@trabajador_blueprint.route('/trabajador', methods=['DELETE'])
@cross_origin()
def delete_trabajador():
    trabajador_id = request.json['trabajador_id']
    return jsonify(trabajador_model.delete_trabajador(trabajador_id))

@trabajador_blueprint.route('/trabajador', methods=['GET'])
@cross_origin()
def get_trabajador():
    trabajador_id = request.json['trabajador_id']
    return jsonify(trabajador_model.get_trabajador(trabajador_id))

@trabajador_blueprint.route('/trabajadores', methods=['GET'])
@cross_origin()
def get_trabajadores():
    return jsonify(trabajador_model.get_trabajadores())

@trabajador_blueprint.route('/all_trabajadores', methods=['GET'])
@cross_origin()
def get_all_trabajadores():
    return jsonify(trabajador_model.get_all_trabajadores())
