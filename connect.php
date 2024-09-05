<?php
    $name = $_POST['name'];
    $email = $_POST['email'];
    $Phone = $_POST['Phone'];
    $Subject = $_POST['Subject'];
    $Message = $_POST['Message'];
    


    // database connection
    $conn = new mysqli('localhost', 'root', '', 'dornan');

    if ($conn->connect_error) {
        die('Connection Failed: ' .$conn->connect_error);
    } else {
        // Prepare the SQL statement with the correct number of placeholders
        $stmt = $conn->prepare("insert into details (Name, Email , Phone , Subject , Message) values (?, ?, ?, ?, ?)");
        // Bind the parameters with the correct variable names and types
        $stmt->bind_param("ssiss", $name, $email, $Phone, $Subject, $Message);
        $stmt->execute();
        echo "Registered Successfully.";
        $stmt->close();
        $conn->close();
    }
    
?>
