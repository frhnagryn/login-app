<?php

include_once("connection.php");

$email = $_POST['email'];
$password = hash('sha256', $_POST['password']);

$res = mysqli_query($mysqli, "SELECT * FROM users WHERE email='$email' AND password='$password'");

header('Content-type: application/json');

if ($res->num_rows > 0) {
    echo json_encode(['status'=>'success','data'=>mysqli_fetch_assoc($res)]);
}else{
    echo json_encode(['status'=>'error']);
}