from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nama_lengkap = db.Column(db.String(80), nullable=False)
    level = db.Column(db.Integer, nullable=False, default=2)
    # One-to-one relationship dengan Login
    login = db.relationship('Login', backref='user', uselist=False)
    # One-to-many relationship dengan FileLocation
    file_locations = db.relationship('FileLocation', backref='user')

class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class FileLocation(db.Model):
    __tablename__ = 'file_locations'
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255), nullable=False)
    metaname = db.Column(db.String(255), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class BpomCertificate(db.Model):
    __tablename__ = 'bpom_certificates'
    id = db.Column(db.Integer, primary_key=True)
    alamat_produsen = db.Column(db.String(255), nullable=False)
    berlaku_dari = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    berlaku_sampai = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    jenis_kemasan = db.Column(db.String(100), nullable=False)
    nama_dagang = db.Column(db.String(100), nullable=False)
    nama_jenis_pangan = db.Column(db.String(100), nullable=False)
    nama_produsen = db.Column(db.String(100), nullable=False)
    no_izin = db.Column(db.String(100), nullable=False)
    uploader_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    file_location_id = db.Column(db.Integer, db.ForeignKey('file_locations.id'))
    # Relasi dengan FileLocation
    file_location = db.relationship('FileLocation', backref='bpom_certificate')

class HalalCertificate(db.Model):
    __tablename__ = 'halal_certificates'
    id = db.Column(db.Integer, primary_key=True)
    alamat_perusahaan = db.Column(db.String(255), nullable=False)
    berlaku_dari = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    berlaku_sampai = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    jenis_produk = db.Column(db.String(100), nullable=False)
    nama_perusahaan = db.Column(db.String(100), nullable=False)
    nama_produk = db.Column(db.String(100), nullable=False)
    no_halal = db.Column(db.String(100), nullable=False)
    uploader_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    file_location_id = db.Column(db.Integer, db.ForeignKey('file_locations.id'))
    # Relasi dengan FileLocation
    file_location = db.relationship('FileLocation', backref='halal_certificate')
