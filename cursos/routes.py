from . import cursos
from flask import render_template, request, redirect, url_for, flash
from models import db, Curso, Alumnos, Maestros
import forms
from sqlalchemy.exc import IntegrityError

@cursos.route("/cursos")
def index():
    lista = Curso.query.all()
    return render_template("cursos/listado_cursos.html", cursos=lista)

@cursos.route("/nuevo_curso", methods=['GET', 'POST'])
def nuevo_curso():
    form = forms.CursoForm(request.form)
    maestros = Maestros.query.all()

    if request.method == 'POST' and form.validate():
        curso = Curso(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            maestro_id=request.form.get('maestro_id')
        )
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('cursos.detalles_curso', id=curso.id))

    return render_template("cursos/nuevo_curso.html", form=form, maestros=maestros)

@cursos.route("/detalles_curso", methods=['GET', 'POST'])
def detalles_curso():
    id = request.args.get('id')
    curso = Curso.query.get(id)
    alumnos = Alumnos.query.all()

    if request.method == 'POST':
        alumno_id = request.form.get('alumno_id')
        alumno = Alumnos.query.get(alumno_id)

        try:
            curso.alumnos.append(alumno)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash("El alumno ya está inscrito en este curso.", "error")

        return redirect(url_for('cursos.detalles_curso', id=id))

    return render_template("cursos/detalles_curso.html", curso=curso, alumnos=alumnos)

@cursos.route("/inscribir_alumno", methods=['POST'])
def inscribir_alumno():
    curso_id = request.form.get('curso_id')
    alumno_id = request.form.get('alumno_id')

    curso = Curso.query.get(curso_id)
    alumno = Alumnos.query.get(alumno_id)

    try:
        curso.alumnos.append(alumno)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()

    return redirect(url_for('cursos.detalles_curso', id=curso_id))

@cursos.route("/modificar_curso", methods=['GET', 'POST'])
def modificar_curso():
    form = forms.CursoForm(request.form)
    maestros = Maestros.query.all()

    if request.method == 'GET':
        id = request.args.get('id')
        curso = Curso.query.get(id)
        form.id.data = curso.id
        form.nombre.data = curso.nombre
        form.descripcion.data = curso.descripcion
        form.maestro_id.data = curso.maestro_id

    if request.method == 'POST' and form.validate():
        id = request.args.get('id')
        curso = Curso.query.get(id)
        curso.nombre = form.nombre.data
        curso.descripcion = form.descripcion.data
        curso.maestro_id = request.form.get('maestro_id')
        db.session.commit()
        return redirect(url_for('cursos.index'))

    return render_template("cursos/modificar_curso.html", form=form, maestros=maestros)

@cursos.route("/eliminar_curso", methods=['GET', 'POST'])
def eliminar_curso():
    form = forms.CursoForm(request.form)

    if request.method == 'GET':
        id = request.args.get('id')
        curso = Curso.query.get(id)
        form.id.data = curso.id
        form.nombre.data = curso.nombre
        form.descripcion.data = curso.descripcion
        form.maestro_id.data = curso.maestro_id

    if request.method == 'POST':
        id = request.args.get('id')
        curso = Curso.query.get(id)
        db.session.delete(curso)
        db.session.commit()
        return redirect(url_for('cursos.index'))

    return render_template("cursos/eliminar_curso.html", form=form)