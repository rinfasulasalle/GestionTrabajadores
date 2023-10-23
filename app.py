from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin 

from backend.blueprints.usuario_blueprint import usuario_blueprint
from backend.blueprints.trabajador_blueprint import trabajador_blueprint

app = Flask(__name__)

app.register_blueprint(usuario_blueprint)
app.register_blueprint(trabajador_blueprint)

cors = CORS(app)

if __name__ == "__main__":
    app.run(port= 8090, debug=True)