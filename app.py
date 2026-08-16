from flask import Flask, request, render_template, url_for, redirect
from extensions import db
from models import Contacto


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

### ctrl + shift + o

@app.route('/') ### Esta es la ruta de visualización de todos los contactos
def inicio():
    ### Se guarda en una variable contactos
    ### De la tabla contactos, consulta a todos los contactos y los guarda en esa variable
    contactos = Contacto.query.all()   #### SELECT * FROM Contacto
    return render_template('index.html', contactos = contactos)


### Paso 1: Visualizar el formulario de la creación del contacto
@app.route('/crear', methods = ['GET']) ### Este es un método de tipo de GET
def ver_creacion_contacto():
    return render_template('crear.html') ### Renderizame esta plantilla -> "crear.html"

#### Tipos de métodos:
##### - Para visualización normalmente los métodos se les conoce como: métodos GET (obtener data)
##### - Para la creación normalmente los métodos se les conoce como: métodos POST (enviar data)

### Paso 2: Enviar el formulario
### Esto se va a ejecutar cuando de click en el botón "Crear contacto"
@app.route('/crear', methods = ['POST'])  ### Este es un método de tipo POST
def crear(): ### request = petición
    ### parte 1: Formar el objeto
    nuevo_contacto = Contacto(
        nombre = request.form['nombre'],
        telefono = request.form['telefono'],
        email = request.form['email'],
    )
    ### parte 2: guardarlo en la base de datos
    db.session.add(nuevo_contacto)
    db.session.commit()
    return redirect(url_for("inicio")) ### Aquí le estoy pidiendo que me redirija al listado de contactos, que es el inicio


@app.route('/editar')
def editar():
    return render_template('editar.html')




#### Data de prueba

## Aquí se van a cargar todos los datos iniciales al ejecutar el programa
def cargar_datos_iniciales():
    ### Si mi tabla Contactos tiene datos, entonces no ejecuta nada 
    if Contacto.query.count() > 0:
        ### Retorna vacío cuando hay contenido en la tabla
        return

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
