<?php

include_once("connection.php");

$first_name = $_POST['first_name'];
$last_name = $_POST['last_name'];
$nik = $_POST['nik'];
$bpjs = $_POST['bpjs'];
$email = $_POST['email'];
$password = hash('sha256', $_POST['password']);

$alamat = $_POST['alamat'];
$kota = $_POST['kota'];
$provinsi = $_POST['provinsi'];
$kecamatan = $_POST['kecamatan'];
$kode_pos = $_POST['kode_pos'];

$nama_kbli = $_POST['nama_kbli'];
$kategori_kbli = $_POST['kategori_kbli'];
$ukuran_lahan = $_POST['ukuran_lahan'];
$kode_kbli = $_POST['kode_kbli'];

$cek = mysqli_query($mysqli, "SELECT * FROM users WHERE email='$email'");

header('Content-type: application/json');

if ($cek->num_rows > 0) {
    echo json_encode(['status'=>'error','message'=>'Ooops email sudah digunakan']);
}else{
    $result = mysqli_query($mysqli, "INSERT INTO users(first_name, last_name, nik, bpjs, email, password, alamat, provinsi, kota, kecamatan, kode_pos, nama_kbli, kategori_kbli, ukuran_lahan, kode_kbli) VALUES('$first_name', '$last_name', '$nik', '$bpjs', '$email','$password', '$alamat', '$provinsi', '$kota', '$kecamatan', '$kode_pos', '$nama_kbli', '$kategori_kbli', '$ukuran_lahan', '$kode_kbli')");
    echo json_encode(['status'=>'success']);
}