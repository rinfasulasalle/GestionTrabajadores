from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from backend.models.mysql_direccion_model import DireccionModel

direccion_model = DireccionModel()
direccion_blueprint = Blueprint('direccion_blueprint', __name__)

@direccion_blueprint.route('/direccion', methods=['POST'])
@cross_origin()
def create_direccion():
    data = request.json
    id_trabajador = data['id_trabajador']
    direccion_pais = data['direccion_pais']
    direccion_departamento = data['direccion_departamento']
    direccion_provincia = data['direccion_provincia']
    direccion_distrito = data['direccion_distrito']
    direccion_detalle = data['direccion_detalle']
    content = direccion_model.create_direccion(id_trabajador, direccion_pais, direccion_departamento, direccion_provincia, direccion_distrito, direccion_detalle)
    return jsonify(content)

@direccion_blueprint.route('/direccion', methods=['PUT'])
@cross_origin()
def update_direccion():
    data = request.json
    id_trabajador = data['id_trabajador']
    direccion_pais = data['direccion_pais']
    direccion_departamento = data['direccion_departamento']
    direccion_provincia = data['direccion_provincia']
    direccion_distrito = data['direccion_distrito']
    direccion_detalle = data['direccion_detalle']
    content = direccion_model.update_direccion(id_trabajador, direccion_pais, direccion_departamento, direccion_provincia, direccion_distrito, direccion_detalle)
    return jsonify(content)

@direccion_blueprint.route('/direccion', methods=['DELETE'])
@cross_origin()
def delete_direccion():
    id_trabajador = request.json['id_trabajador']
    direccion_model.delete_direccion(id_trabajador)
    result = {'result': 1}
    return jsonify(result)

@direccion_blueprint.route('/direccion', methods=['GET'])
@cross_origin()
def get_direccion():
    id_trabajador = request.json['id_trabajador']
    return jsonify(direccion_model.get_direccion(id_trabajador))

@direccion_blueprint.route('/direcciones', methods=['GET'])
@cross_origin()
def get_direcciones():
    return jsonify(direccion_model.get_direcciones())
