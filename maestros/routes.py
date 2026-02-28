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
def index():
    create_form = forms.UserForm(request.form)
    maestros = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form, maestros=maestros)

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"

@maestros.route("/nuevo_maestro", methods=['GET', 'POST'])
def nuevo_maestro():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'POST':
        maes = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.index')) 
    
    return render_template("maestros/nuevo_maestro.html", form=create_form)

@maestros.route("/modificar_maestro", methods=['GET', 'POST'])
def modificar_maestro():
    create_form = forms.MaestroForm(request.form)
    
    if request.method == 'GET':
        id = request.args.get('id')
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        create_form.matricula.data = maes1.matricula
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.especialidad.data = maes1.especialidad
        create_form.email.data = maes1.email
 
    if request.method == 'POST':
        id = request.args.get('id')
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        maes1.nombre = create_form.nombre.data
        maes1.apellidos = create_form.apellidos.data
        maes1.especialidad = create_form.especialidad.data
        maes1.email = create_form.email.data
        
        db.session.add(maes1)
        db.session.commit()
        return redirect(url_for('maestros.index'))
       
    return render_template("maestros/modificar_maestro.html", form=create_form)

@maestros.route("/detalles_maestro", methods=['GET'])
def detalles_maestro():
    id = request.args.get('id')
    maes1 = db.session.query(Maestros).filter(Maestros.matricula == id).first()
    
    return render_template('maestros/detalles_maestro.html', maes=maes1)

@maestros.route("/eliminar_maestro", methods=['GET', 'POST'])
def eliminar_maestro():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        create_form.matricula.data = maes1.matricula
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.especialidad.data = maes1.especialidad
        create_form.email.data = maes1.email
 
    if request.method == 'POST':
        id = request.args.get('id')
        maes = Maestros.query.get(id)
        db.session.delete(maes)
        db.session.commit()
        return redirect(url_for('maestros.index'))
       
    return render_template("maestros/eliminar_maestro.html", form=create_form)