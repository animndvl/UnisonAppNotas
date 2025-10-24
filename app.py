from flask import Flask, render_template, request, redirect, url_for
from nota import ManejadorDeNotas

app = Flask(__name__)
manejador = ManejadorDeNotas()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/crear_nota', methods=['GET', 'POST'])
def crear_nota():
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        
        print(f"Título: {titulo}, Contenido: {contenido}")
        return redirect(url_for('index'))
    return render_template('crear_nota.html')

@app.route('/listar_notas')
def listar_notas():
    manejador = ManejadorDeNotas()
    notas = manejador.leer_notas()
    manejador.cerrar()
    return render_template('listar_notas.html', notas=notas)

if __name__ == '__main__':
    app.run(debug=True)
