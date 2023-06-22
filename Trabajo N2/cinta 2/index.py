from flask import Flask, render_template, request 
from modules.cajon import Cajon



app=Flask(__name__)

lista=[]

 

#ruta raiz 
@app.route('/', methods=['GET','POST'])
def hom():

    if request.method == 'POST':
        cantidad= request.form["cant"]
        
        
        lista.append(cantidad)

    return render_template('hom.html')

@app.route('/home', methods=['GET','POST'])
def home():

    cantidad =int( request.form.get('cant'))
    

    #instancio la clase 
    cajon = Cajon(cantidad)
    # accedo al metodo de la clase 

    aw_manzana,aw_kiwi,aw_papa,aw_zanahoria,  aw_fruta,aw_verdura,aw_alimento,  resp_k,resp_m,resp_p,resp_z=cajon.calcular_cajon()

    return render_template('home.html',aw_manzana=aw_manzana,aw_kiwi=aw_kiwi,aw_papa=aw_papa,aw_zanahoria=aw_zanahoria,aw_fruta=aw_fruta,aw_verdura=aw_verdura,aw_alimento=aw_alimento,resp_k=resp_k , resp_m=resp_m , resp_p=resp_p , resp_z=resp_z)
    #return "hola pag"#render_template('home.html')

    
if __name__=='__main__':
   
    app.run(debug=True)
    #cantidad=lista
    #print(cantidad)
    cantidad=10
    cajon=Cajon(cantidad)
    aw_manzana,aw_kiwi,aw_papa,aw_zanahoria,  aw_fruta,aw_verdura,aw_alimento,  resp_k,resp_m,resp_p,resp_z=cajon.calcular_cajon()
    print(aw_manzana,aw_kiwi,aw_papa,aw_zanahoria,  aw_fruta,aw_verdura,aw_alimento,  resp_k,resp_m,resp_p,resp_z)



