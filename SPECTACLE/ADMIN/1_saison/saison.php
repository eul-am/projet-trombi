<?php
	session_start();
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="../styles/spectacle.css">
	<title>SAISON</title>
</head>
<body>

    <?php require('../../admin/en-tete.php'); ?>

	    <h1>Gestion des saisons</h1>

        <p>
            <?php

	            // D'ABORD ON EFFECTUE DES CONTRÔLES

		        // si l'année a bien été saisi et si le champ de saisi n'est pas vide
		        if(isset($_POST['annee']) /*AND !empty($_POST['annee'])*/)
		        {	
				 	// alors on se connecte dans la base de données
					require('../../require/config.php');

					// Puis on défini les variables et on les sécurise
					$annee = htmlspecialchars($_POST['annee']);

					//on recherche d'abord si l'année existe déjà dans la base de données
					$variable = $bdd->prepare("SELECT id FROM saison WHERE annee = ? LIMIT 1");
					// on exécute la requête
					$variable->execute(array(htmlspecialchars($_POST['annee'])));
					// on va chercher tous les éléments de la table qu'on stocke dans une variable tableau
					$donnee = $variable->fetchAll();

					// si la requête rencontre la même année et si le contenu de cette année est la même que celui de l'utilisateur
					if(count($donnee) > 0 AND htmlspecialchars($_POST['annee']) == $annee)
					{  
                        //on déclare la variable de session si besoin
                        // $_SESSION['annee'] = $donnees[0][1];

						// signaler
						echo '<meta http-equiv="refresh" content="4; ./saison.php"/>';
						die("Cette saison existe déjà !");
                        // echo "Cette année existe déjà !";
                        // header('Location:saison.php');
                        // die();
					}
					else
					{  
						// sinon on prépare l'insertion des données dans la table
						$variable = $bdd->prepare("INSERT INTO saison (annee) VALUES (?)");
						// on récupère les données des variables (dans un tableau) afin de les manipuler : on exécute la requête
						$variable->execute(array(htmlspecialchars($_POST['annee'])));
					}
						
					// et on précise si tout s'est bien passé
					echo '<meta http-equiv="refresh" content="4; ../../admin/espace_admin.php"/>';
					die("Création d'une nouvelle saison avec succès !!!");

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
                        <h4>Créer une nouvelle saison</h4>
		                <p><label>Année</label></p>
                        <!-- Tout ce qui viens après l'attribut 'name' est facultatif -->
		                <input name="annee" <?php if(isset($_POST['annee'])){echo 'value="'.$_POST['annee'].'"';}else{echo 'placeholder="2022-2023"';}?> >
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