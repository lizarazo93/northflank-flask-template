from flask import Flask
from modules.index.index import index
from modules.evaluaciones_desempeño.e_desempeño import e_desempeño
from modules.rotacion_personal.r_personal import r_personal
from modules.encuestas.encuestas import encuestas
from modules.control_inventarios.inventarios import inventarios
from waitress import serve

app = Flask(__name__)

# Blueprints

app.register_blueprint(index)
app.register_blueprint(e_desempeño)
app.register_blueprint(r_personal)
app.register_blueprint(encuestas)
app.register_blueprint(inventarios)

# EndBlueprints

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=80)
