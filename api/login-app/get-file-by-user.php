<?php

include_once("connection.php");

$id_user = $_GET['id_user'];

$result = mysqli_query($mysqli, "SELECT * FROM files WHERE id_user=$id_user");

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $data[] = $row;
    }
    echo json_encode( $data );
}else{
    header('Content-type: application/json');
    echo json_encode( $result );
}