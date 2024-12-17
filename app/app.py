from flask import Flask, render_template
from convertidor import convertir


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convertidor')
def combinar():
    
    # datos = []
    
    nombre_doc = "salida"
    contexto = { 'name' : 'Daniel' }
    plantilla = "plantilla"
    
    datos = [nombre_doc, contexto, plantilla]

    # Llamar a la función que realiza la conversión y genera el documento final
    convertir(nombre_doc, plantilla, contexto)
    
    return render_template('convertido.html', datos=datos)


if __name__ == '__main__':
    app.run(debug=True)




