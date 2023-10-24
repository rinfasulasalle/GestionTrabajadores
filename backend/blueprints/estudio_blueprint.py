from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from backend.models.mysql_estudio_model import EstudioModel

estudio_model = EstudioModel()
estudio_blueprint = Blueprint('estudio_blueprint', __name__)

@estudio_blueprint.route('/estudio', methods=['POST'])
@cross_origin()
def create_estudio():
    data = request.json
    id_trabajador = data['id_trabajador']
    estudio_nivel_educativo = data['estudio_nivel_educativo']
    estudio_situacion_especial = data['estudio_situacion_especial']
    estudio_regimen_laboral = data['estudio_regimen_laboral']
    estudio_regimen_laboral_aseguramiento = data['estudio_regimen_laboral_aseguramiento']
    estudio_institucion = data['estudio_institucion']
    estudio_carrera_educativa = data['estudio_carrera_educativa']
    estudio_capacitacion = data['estudio_capacitacion']
    estudio_especializacion = data['estudio_especializacion']
    estudio_id_colegiatura = data['estudio_id_colegiatura']
    estudio_fecha_colegiatura = data['estudio_fecha_colegiatura']
    estudio_sede_colegiatura = data['estudio_sede_colegiatura']
    estudio_condicion = data['estudio_condicion']
    content = estudio_model.create_estudio(id_trabajador, estudio_nivel_educativo, estudio_situacion_especial,
                                           estudio_regimen_laboral, estudio_regimen_laboral_aseguramiento,
                                           estudio_institucion, estudio_carrera_educativa, estudio_capacitacion,
                                           estudio_especializacion, estudio_id_colegiatura,
                                           estudio_fecha_colegiatura, estudio_sede_colegiatura, estudio_condicion)
    return jsonify(content)

@estudio_blueprint.route('/estudio', methods=['PUT'])
@cross_origin()
def update_estudio():
    data = request.json
    id_trabajador = data['id_trabajador']
    estudio_nivel_educativo = data['estudio_nivel_educativo']
    estudio_situacion_especial = data['estudio_situacion_especial']
    estudio_regimen_laboral = data['estudio_regimen_laboral']
    estudio_regimen_laboral_aseguramiento = data['estudio_regimen_laboral_aseguramiento']
    estudio_institucion = data['estudio_institucion']
    estudio_carrera_educativa = data['estudio_carrera_educativa']
    estudio_capacitacion = data['estudio_capacitacion']
    estudio_especializacion = data['estudio_especializacion']
    estudio_id_colegiatura = data['estudio_id_colegiatura']
    estudio_fecha_colegiatura = data['estudio_fecha_colegiatura']
    estudio_sede_colegiatura = data['estudio_sede_colegiatura']
    estudio_condicion = data['estudio_condicion']
    content = estudio_model.update_estudio(id_trabajador, estudio_nivel_educativo, estudio_situacion_especial,
                                           estudio_regimen_laboral, estudio_regimen_laboral_aseguramiento,
                                           estudio_institucion, estudio_carrera_educativa, estudio_capacitacion,
                                           estudio_especializacion, estudio_id_colegiatura,
                                           estudio_fecha_colegiatura, estudio_sede_colegiatura, estudio_condicion)
    return jsonify(content)

@estudio_blueprint.route('/estudio', methods=['DELETE'])
@cross_origin()
def delete_estudio():
    id_trabajador = request.json['id_trabajador']
    estudio_model.delete_estudio(id_trabajador)
    result = {'result': 1}
    return jsonify(result)

@estudio_blueprint.route('/estudio', methods=['GET'])
@cross_origin()
def get_estudio():
    id_trabajador = request.json['id_trabajador']
    return jsonify(estudio_model.get_estudio(id_trabajador))

@estudio_blueprint.route('/estudios', methods=['GET'])
@cross_origin()
def get_estudios():
    return jsonify(estudio_model.get_estudios())
