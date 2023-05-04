from flask import Flask, render_template, request
from modules import module
import datetime
import random

#PARTE DE MOSTRAR LISTA =======================================================================
archi=open('./data/frases_de_peliculas.txt', 'r')

info=archi.readlines()

#listas 


aciertos = int(0)
errores = int(0)

nomyfe=[]
registro= []
frases=[]
peliculas=[]
frases_y_peliculas=[]
pelis_aux = []



for linea in info:
    linea = linea.rstrip('\n')
    frase, pelicula = linea.split(';')
    frases.append(frase)
    peliculas.append(pelicula)
    lineanueva = pelicula + '/' + frase
    frases_y_peliculas.append(lineanueva)

ordenado_alf = sorted(frases_y_peliculas)

pelis_aux = []
pelis_final = []

for n in range(len(ordenado_alf)):
    num=str(n+1)
    linea= num + '/' +ordenado_alf[n]
    pelis_final.append(linea)
    pelis_aux.append(linea)

pelis_1 = module.pregunta_1(pelis_aux)

print("\n","\n","#######################################")
print("#  Películas: Preguntas y respuestas  #")
print("#######################################")
print("Elige una opción")
print("1 - Mostrar lista de películas.")
print("2 - ¡Trivia de película!")
print("3 - Mostrar secuencia de opciones seleccionadas previamente.")
print("4 - Borrar historial de opciones.")
print("5 - Salir")
opcion = int(input("\n"+"\n"+"Ingrese una opcion: "))

while 0<opcion<6:
    
    if opcion == 1:
        pelis_1 = module.pregunta_1(pelis_aux)
        print("eligio opcion 1: ")
        for n in pelis_1:
            print(n)

        
        
    if opcion == 2:
        print("eligio opcion 2: ")
        frase, opciones, correcta=module.pregunta_2(pelis_aux)
        op1=opciones[0]
        op2=opciones[1]
        op3=opciones[2] 
        print("\n","Su frase es: ",frase)
        print("\n","Usted debera elegir escribiendo el numero de las siguientes opciones: ")
        opciones = [op1,op2,op3]
        for i in range(len(opciones)):
            linea = str(i+1) + '-' + opciones[i]
            print(linea)
        n=int(input('Su opcion es: '))
        resultado=module.corrector(opciones[n-1],correcta)
        print("Su respuesta ha sido ",resultado)
        hora = str(datetime.datetime.now())
        texto="Respuesta "+resultado+" el dia: "+hora+"\n"
        module.cargarReg(texto)

    if opcion == 3:
        print("\n","eligio opcion 3: ")
        x=module.leerArchivo("Registro1.txt")
        print(x)


            
    if opcion == 4:
        print("eligio opcion 4: "+"\n")
        module.vaciarRegistrop("Registro1.txt")
    


    if opcion == 5:
        print("eligio opcion 5: ")
        print('Gracias')
        break
        
    opcion = module.preguntar(True)


app = Flask(__name__)

@app.route('/home', methods=['GET','POST'])
def home():

    module.vaciarRegistrop("Registrop.txt")

    if request.method == 'POST':
        usuario= request.form["user"]
        fecha = str(datetime.datetime.now()) 
        nomyfe.append([usuario,fecha])
        module.guardar_lista_en_archivo('./data/Registrop.txt', nomyfe)
        nomyfe.clear()

    return render_template('home.html',)

@app.route('/trivia', methods=['GET','POST'])
def trivia():
    if request.method == 'POST':
        suma=request.form["valor"]
        total = module.contador()
        if suma == "Correcto":
            module.cargarRegistroP()
        if suma == "Incorrecto":
            module.cargarRegistroN()
    total = module.contador()

    if total == 5:
        x=module.historico()

    
    frase, opciones, correcta=module.pregunta_2(pelis_aux)
    op1=opciones[0]
    op2=opciones[1]
    op3=opciones[2] 

    return render_template('trivia.html', frase=frase, op1=op1, op2=op2, op3=op3, correcta=correcta,  total=total)

@app.route('/lista')
def lista():
    return render_template('listado.html', pelis_1=pelis_1)

@app.route('/correcto', methods=['GET','POST'])
def bien():
    return render_template('correcto.html')

@app.route('/incorrect', methods=['GET','POST'])
def mal():
    return render_template('incorrect.html')

@app.route('/historial')
def histo():
    historiall=module.historial()

    return render_template('historial.html', historiall=historiall)

if __name__ == '__main__':
    app.run(debug=True)


