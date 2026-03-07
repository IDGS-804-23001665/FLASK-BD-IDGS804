from flask import render_template, request, jsonify
from . import consultas
from models import Alumnos, Curso


@consultas.route('/', methods=['GET'])
def index():
    cursos = Curso.query.order_by(Curso.nombre).all()
    alumnos = Alumnos.query.order_by(Alumnos.apellidos, Alumnos.nombre).all()
    return render_template('consultas/index.html', cursos=cursos, alumnos=alumnos)


@consultas.route('/por-curso', methods=['GET'])
def por_curso():
    curso_id = request.args.get('curso_id', type=int)
    if not curso_id:
        return jsonify({'error': 'Falta el parámetro curso_id'}), 400

    curso = Curso.query.get_or_404(curso_id)

    resultado = [
        {
            'matricula': a.id,
            'nombre': a.nombre,
            'apellidos': a.apellidos,
            'email': a.email,
        }
        for a in curso.alumnos
    ]

    return jsonify({'curso': curso.nombre, 'total': len(resultado), 'alumnos': resultado})


@consultas.route('/por-alumno', methods=['GET'])
def por_alumno():
    alumno_id = request.args.get('alumno_id', type=int)
    if not alumno_id:
        return jsonify({'error': 'Falta el parámetro alumno_id'}), 400

    alumno = Alumnos.query.get_or_404(alumno_id)

    resultado = [
        {
            'id': c.id,
            'nombre': c.nombre,
            'descripcion': c.descripcion or '',
        }
        for c in alumno.cursos
    ]

    return jsonify({'alumno': f"{alumno.nombre} {alumno.apellidos}", 'total': len(resultado), 'cursos': resultado})