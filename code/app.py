from flask import Flask, request, render_template, session, url_for, redirect, json, flash, send_from_directory
from flask_json import FlaskJSON, JsonError, json_response, as_json
from werkzeug.utils import secure_filename
import requests
import bcrypt
import datetime
import shutil
import os

DOC_FOLDER = os.path.join('static', 'doc')

app = Flask(__name__)
app.config['SECRET_KEY'] = '^A%DJAJU^JJ123sdfdsfdsg'
json = FlaskJSON(app)

@app.route("/", methods=['GET', 'POST'])
def main():
    if session.get('id'):
        if session.get('level') == 'user':
            url = "http://localhost/login-app/get-file-by-user.php?id_user="+str(session.get('id'))
            response = requests.request("GET", url)
            res = response.json()

            return render_template('home.html', users = res, lusers = len(res))
        else:
            url = "http://localhost/login-app/get-file.php"
            response = requests.request("GET", url)
            res = response.json()

            return render_template('admin.html', users = res, lusers = len(res))
    else:
        return redirect(url_for('login'))


@app.route("/upload", methods=["POST"])
def bpom():
    if session.get('id'):
        file = request.files['filela']
        kategori = request.form['kategori']
        nama_user = session.get('first_name')+' '+session.get('last_name')
        if file :
            fn = file.filename
            fn, fe = os.path.splitext(fn)
            if fe == '.pdf' :
                filename = secure_filename(file.filename)

                a = str(datetime.datetime.now())
                b = a.replace(' ','_')
                c = b.replace('.','_')
                d = c.replace('-','_')
                e = d.replace(':','_')

                newfile = str(session['id'])+'_'+e+'_'+filename
                newfile2 = os.path.join(DOC_FOLDER, newfile)
                file.save(newfile2)

                url = "http://localhost/login-app/upload.php"
                payload={'file': newfile, 'id_user': session.get('id'), 'nama_user':nama_user, 'kategori': kategori}
                requests.request("POST", url, data=payload)

                flash('File berhasil diupload', 'success')
                return redirect(url_for('main'))
            else:
                flash('Data yang kamu masukan harus berupa pdf', 'error')
                return redirect(url_for('main'))
        else:
            flash('Kamu harus mengupload sesuatu', 'error')
            return redirect(url_for('main'))
    else:
        return redirect(url_for('login'))


@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory=DOC_FOLDER, path=filename)


#Ini Untuk Verifikasi OCR
@app.route("/verify")
def verify():
    if session.get('id'):

        data = {
            'message':'OCR Okey. Ini adalah contoh keluaran OCR nanti',
            'status':200
        }

        if data['status'] == 200:
            #Lakukan sesuatu jika berhasil disini
            return json_response(data=data,status=200)
        else:
            #Lakukan sesuatu jika gagal disini
            return json_response(data=data,status=200)
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=["GET", "POST"])
def login():
    if session.get('id'):return redirect(url_for('main'))
    else:
        if request.method == 'GET':
            return render_template('login.html')
        else:
            url = "http://localhost/login-app/login.php"
            response = requests.request("POST", url, data=request.form)
            res = response.json()

            if res['status'] == 'success':
                session['id'] = res['data']['id']
                session['level'] = res['data']['level']
                session['first_name'] = res['data']['first_name']
                session['last_name'] = res['data']['last_name']
                session['data'] = res['data']
                return redirect(url_for('main'))
            else:
                flash('Ooops akun kamu tidak ditemukan', 'error')
                return redirect(url_for('login'))


@app.route('/register', methods=["GET", "POST"])
def register():
    if session.get('id'):return redirect(url_for('main'))
    else:
        if request.method == 'GET':return render_template('register.html')
        else:
            url = "http://localhost/login-app/register.php"
            response = requests.request("POST", url, data=request.form)
            res = response.json()

            if res['status'] == 'success':
                flash('Selamat Akun Kamu Berhasil Dibuat!', 'success')
                return redirect(url_for('login'))
            else:
                flash(res['message'], 'error')
                return redirect(url_for('register'))


@app.route('/logout')
def sigout():
    session.clear()
    return redirect(url_for('main'))
