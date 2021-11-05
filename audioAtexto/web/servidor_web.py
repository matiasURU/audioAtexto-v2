# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for
import os.path
import speech_recognition as sr
from werkzeug.utils import secure_filename
from web.servicios import autenticacion

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('inicio'))


app.config['UPLOAD_FOLDER'] = './Archivos'


@app.route("/upload")
def upload_file():
    return render_template('formulario.html')


@app.route("/upload", methods=['GET', 'POST'])
def uploader():
    text = ""
    if request.method == 'POST':
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        r = sr.Recognizer()
        with sr.AudioFile(f'./Archivos/{filename}') as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='es-ES')

            except:
                text = "¡Lo siento! Audio poco claro."
    return render_template("inicio.html", transcripcion=text)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        if not autenticacion.validar_credenciales(request.form['login'], request.form['correo'],
                                                  request.form['password']):
            error = 'Credenciales inválidas'
        else:
            return redirect(url_for('inicio'))
    return render_template('login.html', error=error)


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = ""
    if request.method == 'POST':
        if not autenticacion.crear_usuario(request.form['login'], request.form['correo'], request.form['password']):
            error = 'No se pudo crear el usuario'
        else:
            return redirect(url_for('inicio'))
    return render_template('registro.html', error=error)


@app.route('/inicio')
def inicio():
    usuarios = autenticacion.obtener_usuarios()
    return render_template('inicio.html', usuarios=usuarios, transcripcion="")


if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
