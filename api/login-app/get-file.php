<?php

include_once("connection.php");

$result = mysqli_query($mysqli, "SELECT * FROM files");

while($row = $result->fetch_assoc()) {
    $data[] = $row;
}

header('Content-type: application/json');
echo json_encode( $data );