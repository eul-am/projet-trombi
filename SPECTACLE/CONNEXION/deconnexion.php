<?php
		session_start();
		// Détruit toutes les variables de session
		$_SESSION = array();
		// Finalement, on détruit la session.
		session_destroy();
		
		//redirige la déconnexion vers la page de connexion
        header('Location: ../connexion/connexion.php'); 
		exit();
	?>


<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="styles/spectacle.css">
	<title>DECONNEXION</title>
</head>
<body>

    <?php

	?>

    


<h1>Page de déconnexion </h1>


	<script type="text/javascript" src="scripts/spectacle.js"></script>

	<footer class="pied"></footer>
</body>
</html>