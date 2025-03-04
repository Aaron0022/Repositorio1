from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def calcular_promedio(datos):
    return sum(datos) / len(datos) 
"""Esto calcula el promedio de una lista de datos numéricos."""

def calcular_desviacion_estandar(datos):
    promedio = calcular_promedio(datos)
    varianza = sum((x - promedio) ** 2 for x in datos) / len(datos)
    return math.sqrt(varianza)
"""Esto calcula la desviación estándar de una lista de datos numéricos."""

@app.route('/procesar', methods=['POST'])
def procesar_datos():
    datos = request.json.get('datos')
    promedio = calcular_promedio(datos)
    desviacion = calcular_desviacion_estandar(datos)
    return jsonify({
        'promedio': promedio,
        'desviacion_estandar': desviacion
    })

if __name__ == "__main__":
    app.run(debug=True)