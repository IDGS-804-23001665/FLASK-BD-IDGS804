from . import maestros
from flask import redirect, request, render_template, url_for
from maestros.routes import maestros, maestros
from models import db
from models import Alumnos, Maestros
import forms
from flask_migrate import Migrate
from flask import g
from config import DevelopmentConfig
from flask import flash
from flask_wtf.csrf import CSRFProtect

@maestros.route("/maestros", methods=['GET', 'POST'])
@maestros.route("/index")
def index():
    create_form = forms.UserForm(request.form)
    maestros = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form, maestros=maestros)

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"