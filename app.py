from flask import Flask, render_template
from extensions import db
from models import Contacto


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)



@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/crear')
def crear():
    return render_template('crear.html')


@app.route('/editar')
def editar():
    return render_template('editar.html')




#### Data de prueba

def cargar_datos_iniciales():
    ## Aquí se van a cargar todos los datos iniciales al ejecutar el programa
    contactos = [
        Contacto(nombre='Ana Garcia', telefono='938283232', email='ana@email.com'),
        Contacto(nombre='Carlos Lopez', telefono='912345678', email='carlos@email.com'),
        Contacto(nombre='Maria Torres', telefono='923456789', email='maria@email.com'),
        Contacto(nombre='Jose Ramirez', telefono='934567890', email='jose@email.com'),
        Contacto(nombre='Lucia Mendoza', telefono='945678901', email='lucia@email.com'),
        Contacto(nombre='Pedro Sanchez', telefono='956789012', email='pedro@email.com'),
        Contacto(nombre='Sofia Herrera', telefono='967890123', email='sofia@email.com'),
        Contacto(nombre='Miguel Castro', telefono='978901234', email='miguel@email.com'),
        Contacto(nombre='Elena Vargas', telefono='989012345', email='elena@email.com'),
        Contacto(nombre='Diego Flores', telefono='990123456', email='diego@email.com')
    ]    
    db.session.add_all(contactos)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        cargar_datos_iniciales()
    app.run(debug=True)
