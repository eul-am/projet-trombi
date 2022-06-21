<?php
	session_start();

	// si on a un utilisateur connecté
	// if(!isset($_SESSION['utilisateur']))
	// {

	// 	// alors l'utilisateur est redirigé vers son espace membre
	// 	// l'idée étant que quand il est connecté, que le lien connexion ne soit pas visible
    //     header('Location: ../connexion/connexion.php');
    //     exit();
	// }
?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="../styles/spectacle.css">
	<title>CONNEXION</title>
</head>
<body>
	<header class="conteneur-entete">
		<a href="../index/index.php" class="logo"><img src="../images/logo.png"></a>

		<nav class="">
		</nav>
	</header>


    <h1>Connexion</h1>

    <form method="post" action="verification.php" name="connexion">
			<p>
				<label for="email">Email</label><br>
				<input type="email" name="email" required> <br>

				<label for="password">Mot de passe</label><br>
				<input type="password" name="password" required> <br> <br>

				<input type="checkbox" name="souvenir"> <label>Rester connecter</label> <br> <br>

				<input type="submit" name="btn_envoie" value="Envoyer" required>
			</p> 
	</form>

        <div><a href="#">Mot de passe oublié ?</a></div>
        <div><a href="../inscription/inscription.php">S'inscrire</a></div>

	<script type="text/javascript" src="../scripts/spectacle.js"></script>
    
</body>
</html>