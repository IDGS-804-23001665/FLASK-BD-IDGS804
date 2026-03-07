from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db
from flask_migrate import Migrate
from cursos import cursos
from maestros import maestros
from alumnos import alumnos
from consultas import consultas

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.register_blueprint(maestros)
app.register_blueprint(cursos)
app.register_blueprint(alumnos)
app.register_blueprint(consultas, url_prefix='/consultas')

db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_fount(e):
    return render_template("404.html"), 404

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()