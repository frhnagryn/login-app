import requests
from flask import session, redirect, url_for, flash
from functools import wraps
from datetime import datetime

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# Pemetaan nama bulan Bahasa Indonesia ke angka
bulan_map = {
    "Januari": 1, "Februari": 2, "Maret": 3, "April": 4, "Mei": 5, "Juni": 6,
    "Juli": 7, "Agustus": 8, "September": 9, "Oktober": 10, "November": 11, "Desember": 12
}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_date(date_str):
    # Pisahkan string tanggal ke dalam komponen hari, bulan, dan tahun
    hari, bulan_str, tahun = date_str.split()
    bulan = bulan_map[bulan_str]  # Dapatkan angka bulan dari nama bulan

    # Buat objek datetime dari komponen tanggal
    return datetime(day=int(hari), month=bulan, year=int(tahun))

def get_ocr_information(filename, file_path):
    # Lakukan request ke URL untuk mendapatkan status
    url = "http://103.31.39.44:5000/visionmodel/predict"
    files = [('image', (filename, open(file_path, 'rb'), 'image/jpeg'))]
    response = requests.request("POST", url, files=files)
    try:
        return response.json()
    except Exception as e:
        return f"Error : {str(e)}"

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Anda harus login terlebih dahulu", "warning")
            return redirect(url_for('login'))
    return wrap
