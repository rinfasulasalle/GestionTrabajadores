from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin
from backend.models.mysql_all_trabajador_model import AllTrabajadorModel

all_trabajador_model = AllTrabajadorModel()
all_trabajador_blueprint = Blueprint('all_trabajador_blueprint', __name__)

@all_trabajador_blueprint.route('/all_trabajadores', methods=['GET'])
@cross_origin()
def get_all_trabajadores():
    return jsonify(all_trabajador_model.get_all_trabajadores())