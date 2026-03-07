from . import alumnos
from flask import render_template, request, redirect, url_for
from models import db, Alumnos
import forms


@alumnos.route("/alumnos")
def index():
    alumnos_list = Alumnos.query.all()
    return render_template("alumnos/index.html", alumno=alumnos_list)


@alumnos.route("/nuevo_alumno", methods=['GET','POST'])
def nuevo_alumno():

    form = forms.UserForm(request.form)

    if request.method == 'POST' and form.validate():

        alumno = Alumnos(
            nombre=form.nombre.data,
            apellidos=form.apellidos.data,
            email=form.email.data,
            telefono=form.telefono.data
        )

        db.session.add(alumno)
        db.session.commit()

        return redirect(url_for('alumnos.index'))

    return render_template("alumnos/nuevo_alumno.html", form=form)


@alumnos.route("/detalles_alumno")
def detalles_alumno():

    id = request.args.get('id')
    alumno = Alumnos.query.get(id)

    return render_template(
        "alumnos/detalles_alumno.html",
        nombre=alumno.nombre,
        apellidos=alumno.apellidos,
        email=alumno.email,
        telefono=alumno.telefono
    )


@alumnos.route("/modificar_alumno", methods=['GET','POST'])
def modificar_alumno():

    form = forms.UserForm(request.form)

    if request.method == 'GET':

        id = request.args.get('id')
        alumno = Alumnos.query.get(id)

        form.id.data = alumno.id
        form.nombre.data = alumno.nombre
        form.apellidos.data = alumno.apellidos
        form.email.data = alumno.email
        form.telefono.data = alumno.telefono

    if request.method == 'POST' and form.validate():

        id = request.args.get('id')

        alumno = Alumnos.query.get(id)

        alumno.nombre = form.nombre.data
        alumno.apellidos = form.apellidos.data
        alumno.email = form.email.data
        alumno.telefono = form.telefono.data

        db.session.commit()

        return redirect(url_for('alumnos.index'))

    return render_template("alumnos/modificar_alumno.html", form=form)


@alumnos.route("/eliminar_alumno", methods=['GET','POST'])
def eliminar_alumno():

    form = forms.UserForm(request.form)

    if request.method == 'GET':

        id = request.args.get('id')
        alumno = Alumnos.query.get(id)

        form.id.data = alumno.id
        form.nombre.data = alumno.nombre
        form.apellidos.data = alumno.apellidos
        form.email.data = alumno.email
        form.telefono.data = alumno.telefono

    if request.method == 'POST':

        id = request.args.get('id')
        alumno = Alumnos.query.get(id)

        db.session.delete(alumno)
        db.session.commit()

        return redirect(url_for('alumnos.index'))

    return render_template("alumnos/eliminar_alumno.html", form=form)