<?php
	session_start();
?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="../styles/spectacle.css">
	<title>INSCRIPTION</title>
</head>
<body>
    <header class="conteneur-entete">
		<!-- <a href="#" class="logo"><img src="images/logo_spectacle.png"></a> -->

		<nav class="">
		</nav>
	</header>


	<h1>Inscription</h1>


	<form method="post" action="verification.php">

		<p><label>Type</label>
		<select name="type" required>
			<option disabled selected >---</option>
			<option value="particulier">Particulier</option>
			<option value="entreprise">Entreprise</option>
		</select>
		</p>

		<p> <label for="nom">Nom/Raison sociale</label> <input type="text" name="nom" required> </p>

		<p> <label for="email">Email</label> <input type="email" name="email" required> </p>

		<p> <label for="password_1">Mot de passe</label> <input type="password" name="password" required> </p>

		<p> <input type="submit" name="btn-envoie" value="Envoyer" required></p>

	</form>

	<script type="text/javascript" src="../scripts/spectacle.js"></script>
	<footer class="pied"></footer>
</body>
</html>