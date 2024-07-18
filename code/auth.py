# auth.py
from models import db, User, FileLocation, Login
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session


def register_user(nama, username, email, password, level=2):
    # Cek apakah username atau email sudah ada
    existing_user_by_username = User.query.filter_by(username=username).first()
    existing_user_by_email = User.query.filter_by(email=email).first()

    if existing_user_by_username or existing_user_by_email:
        return False  # User sudah ada berdasarkan username atau email

    # Buat entri baru di tabel User
    new_user = User(nama_lengkap=nama, username=username, email=email, level=level)
    db.session.add(new_user)
    db.session.commit()

    # Buat entri baru di tabel Login dengan password yang di-hash
    new_login = Login(username=username, password=generate_password_hash(password, method='scrypt'), user_id=new_user.id)
    db.session.add(new_login)
    db.session.commit()

    return True

def login_user_auth(username, password):
    # Mengambil user berdasarkan username dari tabel Login
    login = Login.query.filter_by(username=username).first()

    if login:
        # Mengambil user terkait dari tabel User
        user = User.query.get(login.user_id)

        # Verifikasi password
        if user and check_password_hash(login.password, password):
            # Set session data
            session['logged_in'] = True
            session['user_id'] = user.id  # Menyimpan user_id, bukan id dari tabel login
            session['username'] = user.username
            session['name'] = user.nama_lengkap
            session['level'] = user.level
            
            return True

    # Jika login gagal
    return False
