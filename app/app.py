from flask import Flask, render_template, send_from_directory, request
from convertidor import convertir


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/combinar')
def convert():
    # datos = []
    nombre_doc = "salida"
    contexto = { 'name' : 'Daniel' }
    plantilla = "plantilla"
    datos = [nombre_doc, contexto, plantilla]
    # Llamar a la función que realiza la conversión y genera el documento final
    convertir(nombre_doc, plantilla, contexto)
    # Devolver la plantilla con los datos del documento generado
    return render_template('convertido.html', datos=datos)

@app.route('/outputs/<nombre_archivo>')
def descargar_archivo (nombre_archivo):
    directorio = "outputs/"
    return send_from_directory(directorio, nombre_archivo, as_attachment = True)


# Ruta para crear cdp
@app.route('/crear-cdp', methods = ['GET', 'POST'])
def crear_cdp():
    if request.method == 'POST':
        # Obtener los datos del formulario
        
        consecutivo = request.form['consecutivo']
        fecha = request.form['fecha']
        objeto = request.form['objeto']
        vigencia = request.form['vigencia']
        fuente = request.form['fuente']
        rubro = request.form['rubro']
        valor = request.form['valor']
        
        cdp_creado = { 
                    'consecutivo' : consecutivo,
                    'fecha' : fecha,
                    'objeto' : objeto,
                    'vigencia' : vigencia,
                    'fuente' : fuente,
                    'rubro' : rubro,
                    'valor' : valor
                    }
        return render_template('cdp_creado.html', cdp_creado = cdp_creado)
    return render_template('generar_documento_cdp.html')

if __name__ == '__main__':
    app.run(debug=True)




