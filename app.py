from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def inicio():
    titulo = 'Mi aplicación ejemplo'
    items = [
        { 'titulo': 'Productos', 'descripcion': 'Explora nuestra variedad de productos y encuentra lo que necesitas' },
        { 'titulo': 'Ofertas', 'descripcion': 'Aprovecha nuestras ofertas exclusivas con precios especiales' },
        { 'titulo': 'Contacto', 'descripcion': 'Estamos aquí para ayudarte. No dudes en contactarnos' }
    ]
    return render_template('index.html', titulo=titulo, elementos=items)


@app.route('/crear')
def crear():
    return render_template('crear.html')


@app.route('/editar')
def editar():
    return render_template('editar.html')


if __name__ == '__main__':
    app.run(debug=True)
