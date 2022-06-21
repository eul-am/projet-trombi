<?php
	session_start();
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="../styles/spectacle.css">
	<title>ÉVÉNEMENTS</title>
</head>
<body>

    <?php require('../../admin/en-tete.php'); ?>

	    <h1>Gestion des événements</h1>

        <p>
            <?php

	            // D'ABORD ON EFFECTUE DES CONTRÔLES

		        // si l'année a bien été saisi et si le champ de saisi n'est pas vide
		        if(isset($_POST['ref_oeuvre']) AND isset($_POST['dateHeure']) AND isset($_POST['ref_saison']) /*AND isset($_POST['compositeur']) 
				AND isset($_POST['titre']) AND isset($_POST['interprete']) AND isset($_POST['id_saison']) AND isset($_POST['description'])*/)
		        {	
				 	// alors on se connecte dans la base de données
					require('../../require/config.php');

					// Puis on défini les variables et on les sécurise
					$genre = htmlspecialchars($_POST['ref_genre']);
					$dateHeure = htmlspecialchars($_POST['dateHeure']);
					$annee = htmlspecialchars($_POST['ref_saison']);
					// $titre = htmlspecialchars($_POST['titre']);
					// $interprete = htmlspecialchars($_POST['interprete']); 
					// $annee = htmlspecialchars($_POST['id_saison']);
					// $description = htmlspecialchars($_POST['description']);

					//on recherche d'abord si l'année existe déjà dans la base de données
					$variable = $bdd->prepare("SELECT * FROM evenement LIMIT 1");
					// on exécute la requête
					$variable->execute(array(
						htmlspecialchars($_POST['ref_oeuvre']),
						htmlspecialchars($_POST['dateHeure']),
						htmlspecialchars($_POST['ref_saison']),
						// htmlspecialchars($_POST['titre']),
						// htmlspecialchars($_POST['interprete']), 
						// htmlspecialchars($_POST['id_saison']),
						// htmlspecialchars($_POST['description'])
					));
					// on va chercher tous les éléments de la table qu'on stocke dans une variable tableau
					$donnee = $variable->fetchAll();

					// si la requête rencontre la même année et si le contenu de cette année est la même que celui de l'utilisateur
					if(count($donnee) > 0 
					AND htmlspecialchars($_POST['ref_oeuvre']) == $genre
					AND htmlspecialchars($_POST['dateHeure']) == $dateHeure
					AND htmlspecialchars($_POST['ref_saison']) == $annee
					// AND htmlspecialchars($_POST['titre']) == $titre
					// AND htmlspecialchars($_POST['interprete']) == $interprete
					// AND htmlspecialchars($_POST['id_saison']) == $annee
					// AND htmlspecialchars($_POST['description']) == $description
					)
					{  
                        //on déclare la variable de session si besoin
                        // $_SESSION['annee'] = $donnees[0][1];

						// signaler
						echo '<meta http-equiv="refresh" content="4; ./saison.php"/>';
						die("Cet événement existe déjà !");
                        // echo "Cette année existe déjà !";
                        // header('Location:saison.php');
                        // die();
					}
					else
					{  
						// sinon on prépare l'insertion des données dans la table
						$variable = $bdd->prepare("INSERT INTO evenement VALUES (?, ?, ?)");
						// on récupère les données des variables (dans un tableau) afin de les manipuler : on exécute la requête
						$variable->execute(array(
							htmlspecialchars($_POST['ref_oeuvre']),
							htmlspecialchars($_POST['dateHeure']),
							htmlspecialchars($_POST['ref_saison']),
							// htmlspecialchars($_POST['titre']),
							// htmlspecialchars($_POST['interprete']), 
							// htmlspecialchars($_POST['id_saison']),
							// htmlspecialchars($_POST['description'])
						));
					}
						
					// et on précise si tout s'est bien passé
					echo '<meta http-equiv="refresh" content="4; ../../admin/espace_admin.php"/>';
					die("La création du nouvel événement a été effectué !!!");

                    // echo 'La nouvelle saison a bien été ajouté !';
                    // header('Location: saison.php');
                    // die();

					// on ferme la requête
					$variable->closeCursor();
            }
		    else
		    {		// sinon on affiche le formulaire et on le traite dans la même page
			    ?>
                    <form method="POST" action="<?php echo $_SERVER['PHP_SELF']; ?>">
                        <h4>Créer un nouvel événement</h4>

		                <p><label>Genre</label>
						<input type="text" name="ref_oeuvre">

						<p><label>Date et Heure</label>
						<input type="datetime-local" name="dateHeure"></p>

						<p><label>Annee</label>
						<input type="text" name="ref_saison"></p>

						<!-- <p><label>Titre</label>
						<input type="text" name="id_genre"></p>

						<p><label>Interprete</label>
						<input type="text" name="id_interprete"></p>

						<p><label>Annee</label>
						<input type="text" name="id_saison"></p> -->
						
		                <p> <input type="submit" name="btn-envoie" value="Envoyer" required></p> 
                    </form>
                <?php
		    }
            
        ?>
	        <!-- </form> -->
        </p>

	<script type="text/javascript" src="../scripts/spectacle.js"></script>
	<footer class="pied"></footer>
</body>
</html>