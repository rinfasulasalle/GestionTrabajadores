from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin 

from backend.blueprints.usuario_blueprint import usuario_blueprint
from backend.blueprints.trabajador_blueprint import trabajador_blueprint
from backend.blueprints.sueldo_blueprint import sueldo_blueprint
from backend.blueprints.contrato_blueprint import contrato_blueprint
from backend.blueprints.cuenta_bancaria_blueprint import cuenta_bancaria_blueprint
from backend.blueprints.direccion_blueprint import direccion_blueprint
from backend.blueprints.estudio_blueprint import estudio_blueprint
from backend.blueprints.all_trabajador_blueprint import all_trabajador_blueprint

app = Flask(__name__)

app.register_blueprint(usuario_blueprint)
app.register_blueprint(trabajador_blueprint)
app.register_blueprint(sueldo_blueprint)
app.register_blueprint(contrato_blueprint)
app.register_blueprint(cuenta_bancaria_blueprint)
app.register_blueprint(direccion_blueprint)
app.register_blueprint(estudio_blueprint)
app.register_blueprint(all_trabajador_blueprint)

cors = CORS(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port= 8090)
