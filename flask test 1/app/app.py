from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from models.hamburguesasql import Hamburguesasql
from config import config
app = Flask(__name__)

#config de base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'hamburgueseria'

conexion = MySQL(app)

@app.route('/')
def home():
    colores = ['azul','rojo','amarillo']
    data={
        
        'titulo':'index',
        'bienvenida':'hola mundo',
        'colores':colores,
        'cant_colores':len(colores)
    }
    return render_template('index.html',data= data)

@app.route('/carne')
def listar_hamburguesas_carne():
    data = {}
    try:
        data['hamburguesas'] = Hamburguesasql.leerListaDeHamburguesas(conexion)
        return render_template('hamburguesasDeCarne.html',data=data)
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

@app.route('/pollo')
def listar_hamburguesas_pollo():
    data = {}
    try:
        data['hamburguesas'] = Hamburguesasql.leerListaDeHamburguesas(conexion)
        return render_template('hamburguesasDePollo.html',data=data)
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

@app.route('/editarHamburguesaget/<id>', methods=['GET'])
def editarHamburguesaget(id):
    print(id)
    data = {}
    print(data)
    try:
        
        data['hamburguesa']=Hamburguesasql.leerHamburguesaEspecifica(conexion,id)
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})
    return render_template('editarHamburguesa.html',data=data)

@app.route('/editarHamburguesapost', methods=['POST'])
def editarHamburguesapost():
    id = request.form.get('id')
    nombre = request.form.get('nombre')
    precio = request.form.get('precio')
    stock = request.form.get('stock')
    tipoDeHamburguesa = "carne"
    print(f"{id},{nombre},{precio},{stock},{tipoDeHamburguesa}")
    try:
        Hamburguesasql.updateHamburguesa(conexion,id,nombre,precio,stock,tipoDeHamburguesa)
        return home()
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})



if __name__ == '__main__':
    app.run(debug=True)