from flask import Flask, request, render_template, session, url_for, redirect, json, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from datetime import datetime
import os

from models import db, User, FileLocation, BpomCertificate, HalalCertificate
from auth import register_user, login_user_auth
from utils import login_required, allowed_file, get_ocr_information, parse_date

app = Flask(__name__)
app.config['SECRET_KEY'] = '^A%DJAJU^JJ123sdfdsfdsg'
app.config['UPLOAD_FOLDER'] = '/Users/afifai/work_stuff/side_project/login-app/code/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://afifai:050607341@127.0.0.1/halal_validation'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


with app.app_context():
    db.create_all()

@app.route("/", methods=['GET', 'POST'])
@login_required
def home():
    print(f"Session : {session}")
    if session.get('level') == 2:
        # uploaded_files = FileLocation.query.filter_by(user_id=session['user_id']).all()
        uploaded_files = [
        {'metaname': 'File1', 'status': 1, 'path': 'path/to/file1'},
        {'metaname': 'File2', 'status': 2, 'path': 'path/to/file2'},
        # Tambahkan data sesuai kebutuhan
    ]
        return render_template('home.html', file_uploaded = uploaded_files)
    elif session.get('level') == 1:
        return render_template('admin.html', users = 'afif', lusers = 47)

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'filela' not in request.files:
        flash('File tidak boleh kosong', 'error')
        return redirect(url_for('home'))
    file = request.files['filela']
    if file.filename == '':
        flash('File tidak tersedia', 'error')
        return redirect(url_for('home'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        a = str(datetime.now())
        b = a.replace(' ','_')
        c = b.replace('.','_')
        d = c.replace('-','_')
        e = d.replace(':','_')
        unique_filename = str(session['user_id'])+'_'+e+'_'+filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)

        response_ocr = get_ocr_information(filename, file_path)
        print(response_ocr)

        jenis = response_ocr.get('results', {}).get('jenis', '')
        if jenis == "Izin Edar BPOM":
            status = 1
        elif jenis == "Sertifikat Halal":
            status = 2
        else:
            status = 3


        try:
            with app.app_context():
                new_file_location = FileLocation(
                    path=file_path,
                    metaname=filename,
                    filename=unique_filename,
                    status=status,
                    user_id=session['user_id']
                )
                db.session.add(new_file_location)
                if status == 1:  # Izin Edar BPOM
                    new_bpom_certificate = BpomCertificate(
                        alamat_produsen=response_ocr["results"]["alamat_produsen"],
                        berlaku_dari=parse_date(response_ocr["results"]["berlaku_dari"]),
                        berlaku_sampai=parse_date(response_ocr["results"]["berlaku_sampai"]),
                        jenis_kemasan=response_ocr["results"]["jenis_kemasan"],
                        nama_dagang=response_ocr["results"]["nama_dagang"],
                        nama_jenis_pangan=response_ocr["results"]["nama_jenis_pangan"],
                        nama_produsen=response_ocr["results"]["nama_produsen"],
                        no_izin=response_ocr["results"]["no_izin"],
                        uploader_id=session['user_id'],
                        file_location_id=new_file_location.id
                    )
                    db.session.add(new_bpom_certificate)
                elif status == 2:  # Sertifikat Halal
                    new_halal_certificate = HalalCertificate(
                        alamat_perusahaan=response_ocr["results"]["alamat_perusahaan"],
                        berlaku_dari=parse_date(response_ocr["results"]["berlaku_dari"]),
                        berlaku_sampai=parse_date(response_ocr["results"]["berlaku_sampai"]),
                        jenis_produk=response_ocr["results"]["jenis_produk"],
                        nama_perusahaan=response_ocr["results"]["nama_perusahaan"],
                        nama_produk=", ".join(response_ocr["results"]["nama_produk"]),  # Menyimpan sebagai string
                        no_halal=response_ocr["results"]["no_halal"],
                        uploader_id=session['user_id'],
                        file_location_id=new_file_location.id
                    )
                    db.session.add(new_halal_certificate)
                
                db.session.commit()
        except Exception as e:
            flash(f'Gagal mengupload file: {e}', 'error')
            return redirect(url_for('home'))
        flash("File berhasil diupload")
        return redirect(url_for('home'))
    else:
        flash("File harus berupa gambar dengan format *.jpg, *.jpeg, atau *.png", "warning")
        return redirect(url_for('home'))


# @app.route('/download/<path:filename>', methods=['GET', 'POST'])
# def download(filename):
#     return send_from_directory(directory=DOC_FOLDER, path=filename)


#Ini Untuk Verifikasi OCR
@app.route("/verify")
@login_required
def verify():

    data = {
        'message':'OCR Okey. Ini adalah contoh keluaran OCR nanti',
        'status':200
    }
    
    if data['status'] == 200:
        #Lakukan sesuatu jika berhasil disini
        return json(data=data,status=200)
    else:
        #Lakukan sesuatu jika gagal disini
        return json(data=data,status=200)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if login_user_auth(username, password):
            return redirect(url_for('home'))
        else:
            flash('User tidak ditemukan atau password salah', 'error')
    return render_template('login.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        nama = request.form.get('nama_lengkap')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if register_user(nama, username, email, password):
            flash('Registrasi berhasil, silahkan login')
            return redirect(url_for('login'))
        else:
            flash('Username atau email sudah terdaftar, coba gunakan user lain', 'warning')
    return render_template('register.html')


@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash("Anda berhasil logout")
    return redirect(url_for('login'))

if __name__ == "__main__":
	app.run(debug=True)
