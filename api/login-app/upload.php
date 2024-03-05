<?php

include_once("connection.php");

$id_user = $_POST['id_user'];
$nama_user = $_POST['nama_user'];
$kategori = $_POST['kategori'];
$file = $_POST['file'];

$status = 'success';

$result = mysqli_query($mysqli, "INSERT INTO files(id_user, nama_user, kategori, file) VALUES('$id_user', '$nama_user', '$kategori', '$file')");

header('Content-type: application/json');
echo json_encode(['status'=>'success']);