from flask import render_template, request, redirect, url_for, flash, abort, send_file
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import jinja2
import pdfkit
#pdfkit_config = pdfkit.configuration(wkhtmltopdf='\Program Files\wkhtmltopdf')
from functools import wraps
from modules.config import app, db, login_manager
from modules.databases import Reclamo, User
from modules.forms import LoginForm, RegisterForm
from modules.pie import Grafico
from collections import Counter
#import os
import matplotlib.pyplot as plt

from datetime import date

admin_list = [1]
limpieza_lista = [2,7]
alumnado_lista = [3]




with app.app_context():
    db.create_all()

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.id not in admin_list:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function

def is_admin():
    if current_user.is_authenticated and current_user.id in admin_list:
        return True
    else:
        return False
    
def is_alumnado():
    if current_user.is_authenticated and current_user.id in alumnado_lista:
        return True
    else:
        return False

def is_limpieza():
    if current_user.is_authenticated and current_user.id in limpieza_lista:
        return True
    else:
        return False




@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/", methods=['GET', 'POST'])
def home():    

    return render_template("home.html")


@app.route("/mis_reclamos", methods=['GET', 'POST'])
@login_required
def mis_reclamos():    
    if request.args.get('del'):
        id = request.args.get('id')
        db.session.delete(Reclamo.query.get(id))
        db.session.commit()

    if is_admin():
        lista_reclamos = Reclamo.query.all()
        key = "admin"
    
    elif is_alumnado():
        lista_reclamos = Reclamo.query.filter_by(departamento ="alumnado").all()
        key = "alumnado"
    
    elif is_limpieza():
        lista_reclamos = Reclamo.query.filter_by(departamento ="limpieza").all()
        key = "limpieza"

    else:
        lista_reclamos = Reclamo.query.filter_by(user_id =current_user.id).all()
        key = "usuario"

    if len(lista_reclamos) == 0:
        #lista_reclamos = Reclamo.query.all()
        return render_template(
                                "home.html", esta_vacia=True, key=key, 
                                logged_in=current_user.is_authenticated
                              )
    else:
        return render_template(
                                    "home.html", esta_vacia=False, key=key, lista_reclamos=lista_reclamos ,
                                    logged_in=current_user.is_authenticated 
                              )
    

@app.route("/login", methods= ["GET", "POST"])
def login():
    login_form = LoginForm()
    
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("No hay ningun usuario registrado con este email.")
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, password):
            flash("Contraseña incorrecta, intente otra vez.")
            return redirect(url_for("login"))
        else:
            login_user(user)
            print(current_user)
            if is_admin() or is_alumnado() or is_limpieza():
                return redirect(url_for("menu"))
            else:
             return redirect(url_for('mis_reclamos'))        
    return render_template('login.html', form=login_form)

@app.route("/register", methods= ["GET", "POST"])
def register():
    register_form = RegisterForm()

    if register_form.validate_on_submit():
        
        if User.query.filter_by(email=register_form.email.data).first():
            flash("Ya hay un usuario registrado con ese email")
            return redirect(url_for('login'))
        
        encripted_pass = generate_password_hash(
            password= register_form.password.data,
            method= 'pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email = register_form.email.data,
            password = encripted_pass,
            name = register_form.username.data,
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('register.html', form=register_form)

@app.route("/menu")
@login_required
def menu():
    return render_template("menu.html")

@app.route("/listar", methods=['GET', 'POST'])
@login_required
def listar():
    lista_resueltos = Reclamo.query.filter_by(estado = "pendiente").all()
    if request.args.get('add'):
            id = request.args.get('id')  #Id del reclamo al que se quiere adherir
            
            reclamo = Reclamo.query.filter_by(id= id).one()
            x=reclamo.adheridos
            z=current_user.id
            
            lista_elementos = x.split(",") if len(x) >= 2 else [x.strip()]

            if z in lista_elementos:
                pass
            else:
                flash("Se ha adherido a un reclamo")
                y= x +", "+ str(z)
                reclamo.adheridos = y
                db.session.commit()

    if request.args.get('dptol'):
        lista_resueltos = Reclamo.query.filter_by(estado = "pendiente", departamento="limpieza").all()
    if request.args.get('dptoa'):
        lista_resueltos = Reclamo.query.filter_by(estado = "pendiente", departamento="alumnado").all()
    


    return render_template("lista.html", lista_resueltos=lista_resueltos)

@app.route("/analitica", methods=['GET', 'POST'])
@login_required
def analitica():    
    palabras_alumnado = ["inscripcion", "titulo", "horarios", "feriados", "fecha", "curso", "cursos", "mesas", "examen"]  
    palabras_limpieza = ["limpieza", "sucio", "lavar", "pasillo","baño","trapo", "escoba"]
    lista_reclamos = Reclamo.query.all()
    palabras=[]
    for reclamo in lista_reclamos:
        palabras_reclamo = reclamo.contenido.lower().split()
        if reclamo.departamento == "alumnado":
            palabras_comunes_alumnado = set(palabras_reclamo) & set(palabras_alumnado)
            palabras = palabras + list(palabras_comunes_alumnado)
        elif reclamo.departamento == "limpieza":
            palabras_comunes_limpieza = set(palabras_reclamo) & set(palabras_limpieza)
            palabras = palabras + list(palabras_comunes_limpieza)
    
    word_counts = Counter(palabras)
    
    max_count = max(word_counts.values())
    word_cloud_html = ""

    for word, count in word_counts.items():
        size = int(round((count / max_count) * 30)) + 12
        word_cloud_html += "<span class='word' style='font-size: {}px'>{}</span>".format(size, word)


    lista_resueltos = Reclamo.query.filter_by(estado = "resuelto").all()
    lista_enprogreso = Reclamo.query.filter_by(estado = "en progreso").all()

    cant_total = len(lista_reclamos)
    cant_resueltos = len(lista_resueltos)
    cant_enprogreso = len(lista_enprogreso)
    datos = [cant_resueltos,cant_enprogreso]

    grafico = Grafico()
    grafico.crear_grafico_pie(datos)

    if request.method == 'POST':
        grafico.eliminar_grafico_guardado()
        return redirect(url_for("menu"))

    return render_template("analitico.html", cant_total=cant_total, word_cloud_html=word_cloud_html)

@app.route('/generar_archivo', methods=['POST'])
def generar_archivo():

    otros= []
    if is_admin():
        resueltos = Reclamo.query.filter_by(estado ="pendiente").all()
        lista_reclamos = Reclamo.query.all()
        resueltos= str(len(resueltos))
        otros= str(len(lista_reclamos))

        x= """ Siendo el dia """ + str(date.today()) + """ hay un total de """ + resueltos + """ reclamos resueltos, y """ + otros + """ otros reclamos sin resolver, entre ellos los inactivos, pendientes y en progreso. """
            
    
    elif is_alumnado():
        lista_reclamos = Reclamo.query.filter_by(departamento ="alumnado").all()
        cant = []
        for reclamo in lista_reclamos:
            if reclamo.estado == "pendiente":
                cant.append(reclamo.id)
        resueltos = str(len(cant))
        otros = str(len(lista_reclamos))
        x= """ Siendo el dia """ + str(date.today()) + """ hay un total de """ + resueltos + """ reclamos resueltos, y """ + otros + """ otros reclamos sin resolver hacia el dpto de alumnado, entre ellos los inactivos, pendientes y en progreso. """

    elif is_limpieza():
        lista_reclamos = Reclamo.query.filter_by(departamento ="limpieza").all()
        cant = []
        for reclamo in lista_reclamos:
            if reclamo.estado == "pendiente":
                cant.append(reclamo.id)
        resueltos = str(len(cant))
        otros = str(len(lista_reclamos))
        x= """ Siendo el dia """ + str(date.today()) + """ hay un total de """ + resueltos + """ reclamos resueltos, y """ + otros + """ otros reclamos sin resolver hacia el dpto de limpieza, entre ellos los inactivos, pendientes y en progreso. """


    formato = request.form['formato']
    contenido_html = """
    <html>
    <head>
    <title>Mi archivo HTML</title>
    </head>
    <body>
    <h1>Informe de cantidad de reclamos hasta el dia de la fecha</h1>
    <p>""" + x +""".</p>
    </body>
    </html>
    """

    if formato == 'html':
        with open('analitico.html', 'w') as file:
            file.write(contenido_html)
        return send_file('analitico.html')
    elif formato == 'pdf':
        #config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf')
        path_wkhtmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        ruta_salida= 'C:\\Users\\User\\Desktop\\TP3.2\\analiticopdf.pdf'
        pdfkit.from_string(contenido_html, ruta_salida, configuration=config)
        return send_file("analiticopdf.pdf")

        

@app.route("/add", methods=['GET', 'POST'])
@login_required
def agregar():
    if request.method == 'POST':
            cont = request.form["contenido"]
            if len(cont) == 0:
                flash("El contenido del reclamo esta vacio")
            else:
                reclamo = Reclamo(
                    contenido = request.form["contenido"],
                    fecha = date.today(),
                    estado = "pendiente",
                    user_id = current_user.id,
                    adheridos= current_user.id,
                )
                reclamo.filtrar_departamento()           
                db.session.add(reclamo)
                db.session.commit()
                return redirect(url_for("similares"))
    return render_template("add.html")

@app.route("/similares", methods=['GET', 'POST'])
@login_required
def similares():  
    ultimo_reclamo = Reclamo.query.filter_by(user_id=current_user.id).order_by(Reclamo.id.desc()).first()
    depto = ultimo_reclamo.departamento
    lista = Reclamo.query.filter_by(departamento = depto).all()

    if request.method == 'POST':

        valor=request.form["valor"]
        if valor == "confirmar":
            flash("Reclamo Creado")
            return redirect(url_for('mis_reclamos'))
    if request.method == 'GET':
        if request.args.get('add'):
            id = request.args.get('id')  #Id del reclamo al que se quiere adherir
            
            reclamo = Reclamo.query.filter_by(id= id).one()
            x=reclamo.adheridos
            z=current_user.id
            
            lista_elementos = x.split(",") if len(x) >= 2 else [x.strip()]

            if z in lista_elementos:
                pass
            else:
                y= x +", "+ str(z)
                reclamo.adheridos = y
                db.session.commit()
                flash("Se ha adherido al reclamo")
        if request.args.get('del'):
            ultimo_reclamo = Reclamo.query.filter_by(user_id=current_user.id).order_by(Reclamo.fecha.desc()).first()
            db.session.delete(ultimo_reclamo)
            db.session.commit()
            return redirect(url_for('mis_reclamos'))

            
    return render_template("similares.html", lista=lista)


@app.route("/edit", methods=['GET', 'POST'])
@login_required
def edit():
    if is_admin():
        key = "admin"
        if request.method == 'POST':
            id = request.form['id']
            reclamo_a_editar = db.session.query(Reclamo).get(id)
            reclamo_a_editar.estado = request.form["estado"]
            x=request.form["dpto"]
            if (x  == "limpieza") or (x == "alumnado") :
                reclamo_a_editar.departamento = request.form["dpto"]
            db.session.commit()
            return redirect(url_for('mis_reclamos'))   
    elif is_alumnado():
        key = "alumnado"
    elif is_limpieza():
        key = "limpieza"
    else:
        key = "usuario"

    if request.method == 'POST':
        id = request.form['id']
        reclamo_a_editar = db.session.query(Reclamo).get(id)
        reclamo_a_editar.estado = request.form["estado"]
        db.session.commit()
        return redirect(url_for('mis_reclamos'))       
    id = request.args.get('id')
    reclamo_a_editar = Reclamo.query.get(id)
    
    return render_template("edit.html", reclamo=reclamo_a_editar, key=key)

@app.route("/logout")
def logout():   
    print(current_user)  
    logout_user()      
    print(current_user)
    return redirect(url_for('home'))

@app.route("/ayuda", methods= ["GET", "POST"])
def ayuda():
    return render_template("ayuda.html")

if __name__ == "__main__":
    app.run(debug=True)