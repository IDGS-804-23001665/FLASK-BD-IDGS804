from wtforms import Form, StringField, DateField, IntegerField, EmailField,validators
from flask_wtf import FlaskForm
 
class UserForm(Form):
    id = IntegerField('id')

   
    nombre = StringField('nombre',[
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=20, message='requiere minimo 4, maximo 20')
    ])
   
    apellidos = StringField('apellidos',[
        validators.DataRequired(message='El apellido es requerido')
    ])
   
    email = EmailField('correo',[
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
    
    telefono = StringField('telefono',[
        validators.DataRequired(message='El telefono es requerido'),
    ])
    
class MaestroForm(Form):
    matricula = IntegerField('matricula')
    
    
    nombre = StringField('nombre', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=50, message='requiere minimo 4, maximo 50')
    ])
    apellidos = StringField('apellidos', [
        validators.DataRequired(message='El apellido es requerido')
    ])
    especialidad = StringField('especialidad', [
        validators.DataRequired(message='La especialidad es requerida')
    ])
    email = EmailField('correo', [
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message='Ingrese un correo valido')
    ])
    
class CursoForm(Form):
    id = IntegerField('ID')
    nombre = StringField('Nombre del Curso', [
        validators.DataRequired(message='El nombre es requerido'),
        validators.length(min=4, max=150)
    ])
    descripcion = StringField('Descripción', [
        validators.DataRequired(message='La descripción es requerida')
    ])
    maestro_id = IntegerField('Matrícula del Maestro', [
        validators.DataRequired(message='La matrícula del maestro es requerida')
    ])