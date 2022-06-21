<?php 
    // la SESSION démarre
    session_start();
?>


<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="styles/spectacle.css">
	<title>RÉSERVATION</title>
</head>
<body>

<h1>Vérification réservation </h1>

<?php
	// ICI il y a une différence avec le code de connexion au niveau de la boucle
	// tandisque lors de qu'ici on utilise $_POST['email'] pour vérifier la donnée qu'on insère,
	// Lors de la connexion, on utilise $donnees['email'] pour vérifier la données stockée dans table.

	// On défini les variables
	$preference = $_POST['preference'];
	$quantite = $_POST['quantite'];
	
	// D'ABORD ON EFFECTUE DES CONTRÔLES
 
	// si l'email a bien été saisi
	if(isset($_POST['preference']))
	{	
		// si les deux mots de passe ont bien été saisie
		if(isset($_POST['quantite']))
		{	
			// on se connecte dans la base de données
			require("../require/config.php");

			// Puis on sécurise les variables
			$preference = ($_POST['preference']);
			$quantite = htmlspecialchars($_POST['quantite']);

			//on recherche d'abord si l'utilisateur est déjà inscrit dans la base de données : si ce compte existe déjà (l'email)
			$utilisateur = $bdd->prepare("SELECT * FROM utilisateur WHERE email = ? AND password = ? LIMIT 1");
			// on exécute la requete pour le nombre de variables indiquées
			$utilisateur->execute(array(filter_var($_POST['email'], FILTER_VALIDATE_EMAIL), htmlspecialchars(sha1($_POST['password']))));
			// on va chercher tous les éléments de la table qu'on stocke dans une variable tableau
			$donnees = $utilisateur->fetchAll();
			// si la requête rencontre un email du genre et si le contenu de cet email est le même que celui de l'utilisateur

			// À SAVOIR : 

			// $donnees[0][0] == 'admin';
			// $donnees[0][1] == 'type' ;
			// $donnees[0][2] == 'nom';
			// $donnees[0][3] == 'email';

			// $_SESSION['id'] = $donnees[0][0];
			// $_SESSION['type'] = $donnees[0][1] ;
			// $_SESSION['nom'] = $donnees[0][2];
			// $_SESSION['email'] = $donnees[0][3];

			if(count($donnees) > 0 AND filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)==$email AND htmlspecialchars(sha1($_POST['password'])==$password))
			{
				//tout va bien

				// si la donnée de la deuxième colonne est de type 'admin' et si elle correspond à l'email et au mot de passe indiqué par l'utilisateur,
				if($donnees[0][1] == 'admin' AND filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)==$email AND htmlspecialchars(sha1($_POST['password'])==$password))
				{	
					// alors on ouvre (ou accède à) la SESSION
					// on transmet les données de l'utilisateur aux variables de SESSION
					// ne jamais transmettre le mot de passe
					$_SESSION['id'] = $donnees[0][0];
					$_SESSION['type'] = $donnees[0][1];
					$_SESSION['nom'] = $donnees[0][2];
					$_SESSION['email'] = $donnees[0][3]; 
					
					// l'utilisateur est redirigé vers la page indiquée
					header('Location: ../admin/espace_admin.php');
        			exit();

				}
				else
				{	
					// sinon, l'utilisateur est redirigé vers l'autre SESSION : l'espace membre
					// et on transmet ses données aux variables de SESSION
					$_SESSION['id'] = $donnees[0][0] ;
					$_SESSION['type'] = $donnees[0][1] ;
					$_SESSION['nom'] = $donnees[0][2];
					$_SESSION['email'] = $donnees[0][3];
					
					// l'utilisateur est redirigé vers la page indiquée
					header('Location: ../utilisateur/profil.php');
        			exit();
				}

			}
			else
			{
				// sinon on indique ques les identifiants sont incorrects
				echo '<meta http-equiv="refresh" content="2; ./connexion.php"/>';
				die("Identifiant ou mot de passe incorrect !");
			}

				// on ferme la requête
			$utilisateur->closeCursor();

			}
			else
			{		// sinon s'il manque un mot de passe
				echo '<meta http-equiv="refresh" content="2; ./reservation.php"/>';
				die("Veuillez choisir une quantité !");
			}
		}
		else
		{		// sinon s'il manque l'email
			echo '<meta http-equiv="refresh" content="2; ./reservation.php"/>';
			die("Veuillez choisir une préférence !");
		}

?>

	<script type="text/javascript" src="spectacle.js"></script>
</body>
<footer class="pied"></footer>
</html>