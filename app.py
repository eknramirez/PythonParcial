from flask import Flask, render_template, request

#from flask_debug import Debug
import mysql.connector
import json
import os
from werkzeug import secure_filename
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


app = Flask(__name__)
app.config['UPLOAD_FOLDER']='./static/import/'



@app.route("/")
def index():
	return render_template('index.html')


@app.route("/datos")
def Ingresar_datos():
	return render_template('cargar_datos.html')

#@app.route("/graficas")
#def graficas():
	#return render_template('graficas.html')


@app.route('/cargar_archivo', methods=['POST'])
def cargar_archivo():
    if request.method == 'POST':
        archivo = request.files['archivo']
        nombre = secure_filename(archivo.filename)
        archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre))

        return render_template('index.html', title = 'Proyecto')

@app.route('/graficos')
def graficos():
	ext = os.path.splitext(app.config['UPLOAD_FOLDER']+'AMBIENTE.csv')[1]
	if ext == '.csv':
		data = pd.read_csv(app.config['UPLOAD_FOLDER']+'AMBIENTE.csv', sep=',')
		return render_template('graficas.html', json=list(data))

@app.route('/generar_grafica', methods=['POST'])
def generar_grafica():
    #if ext == '.csv':
    data = pd.read_csv(app.config['UPLOAD_FOLDER']+'AMBIENTE.csv', sep=',')
    grafico = request.form['grafico']
    arreglo = request.form['columnas']
    arreglo = arreglo.split(',')
    equipos = data.loc[0:5,[arreglo[0], arreglo[1]]]

    ganador = equipos[arreglo[0]]
    goles = equipos[arreglo[1]]
    fig = plt.figure(figsize=(10, 6))

    if grafico == 'Columnas':
        plt.bar(ganador ,  goles, width=0.3, color='#3498db')
        plt.xticks(ganador)
        plt.ylabel(arreglo[1])
        plt.xlabel(arreglo[0])
        plt.title('Estadistica Graficas en '+grafico)
    if grafico == 'Barras':
        plt.barh(ganador,  goles, color='#3498db')
        plt.xticks(ganador)
        plt.ylabel(arreglo[1])
        plt.xlabel(arreglo[0])
        plt.title('Estadistica Graficas en '+grafico)

    fig.savefig("./static/temporales/1.png")
    route = "./static/temporales/1.png"

    return route


@app.route('/consultar')
def consultar():
	data = pd.read_csv(app.config['UPLOAD_FOLDER']+'AMBIENTE.csv', sep=',')

	return render_template('consultar.html',json=data)

	#table = dato.to_html(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, bold_rows=True, classes=None, escape=True, max_rows=None, max_cols=None, show_dimensions=False, notebook=False, decimal='.', border=None, table_id=None)
	#return table




if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=10000)