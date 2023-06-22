from flask import Flask, render_template, request 

from modules import cintaTransportadora as Ct


app=Flask(__name__)

lista=[]
lista_alimento=[]

#ruta raiz  

@app.route('/', methods=['GET','POST'])
def home():

    if request.method == 'POST':
        cantidad = int(request.form["cantidad"])
        #lista.append(cantidad)
        
        cajon=Ct.Cinta_Transportadora
        aw_manzana,aw_kiwi,aw_papa,aw_zanahoria,aw_fruta,aw_verdura,aw_alimento= cajon.Cajon_alimentos(cantidad)

    return render_template('contador.html',aw_manzana=aw_manzana,aw_kiwi=aw_kiwi,aw_papa=aw_papa,aw_zanahoria=aw_zanahoria,aw_fruta=aw_fruta,aw_verdura=aw_verdura,aw_alimento=aw_alimento)


    
if __name__=='__main__':
   
   app.run(debug=True)



