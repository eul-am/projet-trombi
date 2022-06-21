<?php 
    // on démarre la session
    session_start();

?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="spectacle.css">
	<title>ESPACE MEMBRE</title>
</head>
<body>

<!-- Début en-tête -->
<div class="en-tete">
		<!-- logo -->
		<img src="../images/logo.png">
		<!-- début BOUCLE, CONDITION pour masquer ou afficher un lien -->
		<?php	
			?>
				<!-- côté droit en-tête -->
				<div class="en-tete-droite">
					<?php 
					// si l'utilisateur n'est pas en ligne (si ses variables de session ne sont pas détectées par le serveur)
						if(!isset($_SESSION['id']) AND !isset($_SESSION['type']) AND !isset($_SESSION['nom']) AND !isset($_SESSION['email']))
						{
						// on affiche connexion
							?>
								<div><a href="../connexion/connexion.php">Connexion</a></div>
							<?php
						}

						else
						{
							// sinon on affiche déconnexion
							?>
								<div>Vous êtes connecté en tant que <?php echo htmlentities(trim($_SESSION['type'])); ?></div>
								<div>Votre nom est : <?php echo htmlentities(trim($_SESSION['nom'])); ?></div>
								<div><a href="profil.php">Profil</a></div>
								<div><a href="../connexion/deconnexion.php">Déconnexion</a></div>
							<?php
						}
					?>
				</div>
			<?php
		?>

		<div>
			<!-- liens de navigation -->
			<div>
				<div><a href="../index/index.php" class="actif">Home</a></div>
				<div><a href="../navigation/1_programmation/programmation.php">Programmation</a></div>
				<div><a href="../navigation/2_agenda/agenda.php">Agenda</a></div>
				<div><a href="../navigation/3_reservation/reservation.php">Réservation</a></div>
				<div><a href="../navigation/4_infos_pratiques/infos_pratiques.php">Infos pratiques</a></div>
			</div>
		</div>
	</div>
	<!-- FIN EN-TÊTE -->


    <h1>Bienvenu <?php echo htmlentities(trim($_SESSION['nom'])); ?> !<br /></h1>


	<script type="text/javascript" src="scripts/spectacle.js"></script>

    <footer class="pied"></footer>
</body>
</html>