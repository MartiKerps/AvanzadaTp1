# -*- coding: utf-8 -*-


from modules.curso import Curso
from modules.departamento import Departamento
from modules.facultad import Facultad 
from modules.estudiante import Estudiante
from modules.profesor import Profesor



facultad = Facultad()
curso1 = Curso ("Programacion")
prof1 = Profesor ("Ramon",curso1)
# ya se asocia al curso y se agrga a la lista de profesores del curso
dpto_informatica = Departamento("Informatica")
alumno = Estudiante("Mateo")


#dpto_informatica.agregar_miembro(prof1)
curso1.set_estudiantes(alumno)
facultad.set_departamento(dpto_informatica)
departamento = facultad.get_departamentos()

for i in departamento:
    print(i)
    
if __name__ == '__main__':
       
    curso = Curso ("Biologia")
    profesor = Profesor ("Ramon",curso)  
    curso.set_profesor(profesor) 
    estudiante = Estudiante ("Juan") 
    departamentos = []
    facultad = Facultad()
    dep = Estudiante ("Informatica")
    departamento = Departamento ("Lengua")
    facultad.set_departamento(dep)
    facultad.set_estudiante(estudiante)
    departamento.agregar_miembro(estudiante)
    departamento.agregar_miembro(profesor)
    departamento.agregar_director(estudiante)

    