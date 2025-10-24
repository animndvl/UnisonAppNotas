from flask import Flask, render_template, request, redirect, url_for
from nota import ManejadorDeNotas

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/crear_nota', methods=['GET', 'POST'])
def crear_nota():
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        manejador = ManejadorDeNotas()
        manejador.crear_nota(titulo, contenido)
        manejador.cerrar()
        return redirect(url_for('listar_notas'))
    return render_template('crear_nota.html')

@app.route('/listar_notas')
def listar_notas():
    manejador = ManejadorDeNotas()
    notas = manejador.leer_notas()
    manejador.cerrar()
    return render_template('listar_notas.html', notas=notas)

@app.route('/modificar_nota/<int:id>', methods=['GET', 'POST'])
def modificar_nota(id):
    manejador = ManejadorDeNotas()
    nota = next((n for n in manejador.leer_notas() if n.id == id), None)
    if not nota:
        manejador.cerrar()
        return "Nota no encontrada", 404

    if request.method == 'POST':
        nuevo_titulo = request.form['titulo']
        nuevo_contenido = request.form['contenido']
        manejador.actualizar_nota(id, nuevo_titulo, nuevo_contenido)
        manejador.cerrar()
        return redirect(url_for('listar_notas'))

    manejador.cerrar()
    return render_template('modificar_nota.html', nota=nota)


@app.route('/eliminar_nota/<int:id>', methods=['GET', 'POST'])
def eliminar_nota(id):
    manejador = ManejadorDeNotas()

    nota = next((n for n in manejador.leer_notas() if n.id == id), None)
    if not nota:
        manejador.cerrar()
        return "Nota no encontrada", 404
    
    if request.method == 'POST':
        manejador.eliminar_nota(id)
        manejador.cerrar()
        return redirect(url_for('listar_notas'))
    
    manejador.cerrar()
    return render_template('eliminar_nota.html', nota=nota)
    
if __name__ == '__main__':
    app.run(debug=True)
