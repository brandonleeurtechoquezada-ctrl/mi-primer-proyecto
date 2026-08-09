from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/crear')
def crear():
    return render_template('crear.html')


@app.route('/editar')
def editar():
    return render_template('editar.html')


if __name__ == '__main__':
    app.run(debug=True)
