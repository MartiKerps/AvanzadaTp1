from flask import Flask, render_template, request
from modules import module
import datetime

#PARTE DE MOSTRAR LISTA =======================================================================
archi=open('./data/frases_de_peliculas.txt', 'r')

info=archi.readlines()

#listas 
""""""
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
#hasta aca =======================================================================

#PARTE TRIVIA==========================================================================

#frase, opciones, correcta=module.pregunta_2(pelis_aux)
#op1=opciones[0]
#op2=opciones[1]
#op3=opciones[2] 

#======================================================================================

app = Flask(__name__)

@app.route('/home', methods=['GET','POST'])
def home():

    module.vaciarRegistrop()

    if request.method == 'POST':
        usuario= request.form["user"]
        fecha = str(datetime.datetime.now()) 
        nomyfe.append([usuario,fecha])
        module.guardar_lista_en_archivo('./data/Registrop.txt', nomyfe)
        nomyfe.clear()

    return render_template('home.html',)

@app.route('/trivia')
def trivia():

    
    frase, opciones, correcta=module.pregunta_2(pelis_aux)
    op1=opciones[0]
    op2=opciones[1]
    op3=opciones[2] 

    return render_template('trivia.html', frase=frase, op1=op1, op2=op2, op3=op3, correcta=correcta)

@app.route('/lista')
def lista():
    return render_template('listado.html', pelis_1=pelis_1)

@app.route('/correcto', methods=['GET','POST'])
def bien():
    if request.method == 'POST':
        suma=request.form["valor"]
        total = module.contador()
        if suma == "Correcto":
            module.cargarRegistroP()
    total = module.contador()

    if total == 5:
        x=module.historico()
        
    return render_template('correcto.html', total=total)

@app.route('/incorrect', methods=['GET','POST'])
def mal():
    if request.method == 'POST':
        punto=request.form["valori"]
        total = module.contador()
        if punto == "Incorrecto":
            module.cargarRegistroN()

    total = module.contador()

    if total == 5:
        x=module.historico()

    return render_template('incorrect.html', total=total)

@app.route('/historial')
def histo():
    historiall=module.historial()

    return render_template('historial.html', historiall=historiall)





if __name__ == '__main__':
    app.run(debug=True)


