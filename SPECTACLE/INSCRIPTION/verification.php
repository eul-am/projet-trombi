<?php
	// on démarre la session
	session_start();
?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="styles/spectacle.css">
	<title>INSCRIPTION</title>
</head>
<body>
    <header class="conteneur-entete">
		<!-- <a href="#" class="logo"><img src="images/logo_spectacle.png"></a> -->

		<nav class="">
		</nav>
	</header>


	<h1>Vérification d'inscription</h1>

	<?php

// ICI il y a une différence avec le code de connexion au niveau de la boucle
// tandisque lors de qu'ici on utilise $_POST['email'] pour vérifier la donnée qu'on insère,
// Lors de la connexion, on utilise $donnees['email'] pour vérifier la données stockée dans table.

	// On défini les variables sans les sécuriser
	$type = $_POST['type'];
	$nom = $_POST['nom'];
	$email = $_POST['email'];
	$password = $_POST['password'];

	// D'ABORD ON EFFECTUE DES CONTRÔLES

	// on vérifie si le nom a bien été saisi par l'utilisateur
if(isset($_POST['type']))
{
	if(isset($_POST['nom']))
	{	// si l'email a bien été saisi
		if(isset($_POST['email']))
		{	
			// si le mot de passe a bien été saisi
			if(isset($_POST['password']))
			{	
				// // si les deux mots de passe sont identiques. S'ils ne le sont pas
				// if($password_1 != $password_2)
				// {
				// 	// on le signale
				// 	echo '<meta http-equiv="refresh" content="2; ./inscription.php"/>';
				// 	die("Les deux mots de passe doivent être identiques !");
				// }
				// else
				// {	// si tout est bon,
				// 	// on se connecte dans la base de données
					require('../require/config.php');

					// Puis on défini les variables et on les sécurise
					$type = htmlspecialchars($_POST['type']);
					$nom = htmlspecialchars($_POST['nom']);
					$email = filter_var($_POST['email'], FILTER_VALIDATE_EMAIL);
					$password= htmlspecialchars(sha1($_POST['password']));

					//on recherche d'abord si l'utilisateur est déjà inscrit dans la base de données : si ce compte existe déjà (l'email)
					$utilisateur = $bdd->prepare("SELECT id FROM utilisateur WHERE email = ? LIMIT 1");
					// on exécute la requête
					$utilisateur->execute(array(filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)));
					// on va chercher tous les éléments de la table qu'on stocke dans une variable tableau
					$tableau = $utilisateur->fetchAll();
					// si la requête rencontre un email du même genre et si (que) le contenu de cet email est le même que celui de l'utilisateur
					if(count($tableau) > 0 AND filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)==$email)
					{
						// signaler
						echo '<meta http-equiv="refresh" content="2; ./inscription.php"/>';
						die("Ce compte existe déjà !");
					}
					else
					{  // NB : POUR CREER UN ADMIN, IL FAUT FAIRE CETTE requête : on désactive la variable 'type' envoyé par l'utilisateur. Et on se sert du 'type' par défaut proposé par mysql.
						// $variable = $bdd->prepare("INSERT INTO utilisateur (type, nom, email, password) VALUES ('admin', ?, ?, ?)");
						//$variable->execute(array(htmlspecialchars($_POST['nom']), filter_var($_POST['email'], FILTER_VALIDATE_EMAIL), htmlspecialchars(sha1($_POST['password']))));
						
						// sinon on prépare l'insertion des données dans la table
						$variable = $bdd->prepare("INSERT INTO utilisateur (type, nom, email, password) VALUES (?, ?, ?, ?)");
						// on récupère les données des variables (dans un tableau) afin de les manipuler : on exécute la requête
						$variable->execute(array(htmlspecialchars($_POST['type']), htmlspecialchars($_POST['nom']), filter_var($_POST['email'], FILTER_VALIDATE_EMAIL), 
						htmlspecialchars(sha1($_POST['password']))));
					}
						
					// et on précise si tout s'est bien passé
					echo '<meta http-equiv="refresh" content="2; ./../connexion/connexion.php"/>';
					die("Inscription réussie !");

					// on ferme la requête
					$utilisateur->closeCursor();
					
				// }

			}
			else
			{		// sinon s'il manque un mot de passe
				echo '<meta http-equiv="refresh" content="2; ./inscription.php"/>';
				die("Veuillez saisir le mot de passe !");
			}
		}
		else
		{		// sinon s'il manque l'email
			echo '<meta http-equiv="refresh" content="2; ./inscription.php"/>';
			die("Veuillez saisir l'email !");
		}
	}
	else
	{		// sinon s'il manque le nom
		echo '<meta http-equiv="refresh" content="2; ./inscription.php"/>';
		die("Veuillez saisir le nom !");
	}
}
else
{		// sinon s'il manque le nom
	echo '<meta http-equiv="refresh" content="2; ./inscription.php"/>';
	die("Veuillez veuillez choisir un type !");
}

?>

	<script type="text/javascript" src="scripts/spectacle.js"></script>
	<footer class="pied"></footer>
</body>
</html>