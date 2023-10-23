from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from backend.models.mysql_usuario_model import UsuarioModel

usuario_model = UsuarioModel()
usuario_blueprint = Blueprint('usuario_blueprint', __name__)

@usuario_blueprint.route('/usuario', methods=['POST'])
@cross_origin()
def create_usuario():
    data = request.json
    usuario_id = data['id']
    usuario_rol = data['usuario_rol']
    usuario_nombres = data['usuario_nombres']
    usuario_apellidos = data['usuario_apellidos']
    usuario_correo = data['usuario_correo']
    usuario_contrasenia = data['usuario_contrasenia']
    content = usuario_model.create_usuario(usuario_id,usuario_rol, usuario_nombres, usuario_apellidos, usuario_correo, usuario_contrasenia)
    return jsonify(content)

@usuario_blueprint.route('/usuario', methods=['PUT'])
@cross_origin()
def update_usuario():
    data = request.json
    usuario_id = data['id']
    usuario_rol = data['usuario_rol']
    usuario_nombres = data['usuario_nombres']
    usuario_apellidos = data['usuario_apellidos']
    usuario_correo = data['usuario_correo']
    usuario_contrasenia = data['usuario_contrasenia']
    content = usuario_model.update_usuario(usuario_id, usuario_rol, usuario_nombres, usuario_apellidos, usuario_correo, usuario_contrasenia)
    return jsonify(content)

@usuario_blueprint.route('/usuario', methods=['DELETE'])
@cross_origin()
def delete_usuario():
    usuario_id = request.json['id']
    return jsonify(usuario_model.delete_usuario(usuario_id))

@usuario_blueprint.route('/usuario', methods=['GET'])
@cross_origin()
def get_usuario():
    usuario_id = request.json['id']
    return jsonify(usuario_model.get_usuario(usuario_id))

@usuario_blueprint.route('/usuarios', methods=['GET'])
@cross_origin()
def get_usuarios():
    return jsonify(usuario_model.get_usuarios())
