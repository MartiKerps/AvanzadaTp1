from modules.config import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from flask_login import UserMixin

palabras = ["inscripcion titulo horarios feriados fecha curso cursos mesas examen","limpieza sucio lavar pasillo baño trapo escoba"]

#https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html
class Reclamo(db.Model):
    __tablename__ = 'reclamos'
    id = Column(Integer(), primary_key=True)
    estado = Column(String(500), nullable=False)
    fecha = Column(String(1000))
    contenido = Column(String(1000), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id'))
    departamento = Column(String(500))
    adheridos= Column(String(1000))
    #adheridos = Column(String(15))

    def filtrar_departamento(self):
        
        palabras_alumnado = ["inscripcion", "titulo", "horarios", "feriados", "fecha", "curso", "cursos", "mesas", "examen"]  # Palabras clave para el departamento de alumnado
        palabras_limpieza = ["limpieza", "sucio", "lavar", "pasillo","baño","trapo", "escoba"]  # Palabras clave para el departamento de limpieza
        
        palabras_reclamo = self.contenido.lower().split()  # Dividir el reclamo en palabras individuales
        
        # Contar el número de palabras en común con el departamento de alumnado
        palabras_comunes_alumnado = len(set(palabras_reclamo) & set(palabras_alumnado))
        
        # Contar el número de palabras en común con el departamento de limpieza
        palabras_comunes_limpieza = len(set(palabras_reclamo) & set(palabras_limpieza))

        if palabras_comunes_alumnado > palabras_comunes_limpieza:
            self.departamento = "alumnado"
            return "alumnado"
        elif palabras_comunes_limpieza > palabras_comunes_alumnado:
            self.departamento = "limpieza"
            return "limpieza"
        else:
            self.departamento = "desconocido"
            return "desconocido"


        
        



    


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(1000))
    
