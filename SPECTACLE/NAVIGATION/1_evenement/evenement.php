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
	<title>ÉVÉNEMENTS</title>

</head>
<body>
	<!-- Début en-tête -->
	<div class="header">

		<!-- logo , côté gauche en-tête -->
		<div>
			<a href="#"><img src="../../images/logo.png" class="logo"></a>
		</div>
		

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
							<div>
								<a href="../../connexion/connexion.php" class="a-droite">Connexion</a>
							</div>
							<?php
						}

						else
						{
							// sinon on affiche déconnexion
							?>
								<div>
									<!-- <a href="#"> êtes connecté en tant que <?php echo htmlentities(trim($_SESSION['type'])); ?></a>
									<a href="">Votre nom est : <?php echo htmlentities(trim($_SESSION['nom'])); ?></a> -->
									<a href="../../utilisateur/profil.php" class="a-droite">Profil</a>
									<a href="../../connexion/deconnexion.php" class="a-droite">Déconnexion</a>
								</div>
							<?php
						}
					?>
				</div>
				<!-- fin côté droit en-tête -->
			<?php
		?>

	</div>
	<div class="">
		<!-- liens de navigation -->
		<div class="liens-nav"> 
			<a href="../../index/index.php" class="actif">Home</a>
			<a href="evenement.php">Événements</a>
			<a href="../2_agenda/agenda.php">Agenda</a>
			<a href="../3_reservation/reservation.php">Réservation</a>
			<a href="../4_infos_pratiques/infos_pratiques.php">Infos pratiques</a>
		</div> 
		<!-- fin des liens de navigation -->
		<?php
			if(isset($_SESSION['id']) AND isset($_SESSION['type']) AND isset($_SESSION['nom']) AND isset($_SESSION['email']))
			{
				?>
					<div class="infos-compte">
						<a href="#"> Vous êtes connecté en tant que <b> <?php echo htmlentities(trim($_SESSION['type'])); ?></b></a>
						<a href="">Votre nom est : <b> <?php echo htmlentities(trim($_SESSION['nom'])); ?> </b></a>				
					</div>
				<?php
			}
		?>
	</div>
	<!-- FIN EN-TÊTE -->

	<!-- MAIN (Center website) -->
<main>
	<section class="section">

		<h1 
			class="h1-ev">ÉVÉNEMENTS
			<!-- <hr> -->
		</h1>

		<div class="conteneur-bouton">
			<h3 class="fi">Filtrer par genre</h3>
			<a href="evenement.php" class="ev"> Tous les événements</a>
  			<a href="opera.php" class="op"> Opéra</a>
  			<a href="concert.php" class="co"> Concert</a>
  			<a href="recital.php" class="re"> Récital</a>
  			<a href="danse.php" class="da"> Danse</a>
		</div>


		<!-- le sens horizontal (la ligne) -->
		<div class="ligne">

			<!-- 1ère colonne de la ligne ou grille verticale -->
			<div class="colonne opera">
				<div class="contenu">
					<!-- la photo -->
					<a href="../5_detail/detail.php"><img src="../../images/ensemble.jpg" alt="opera" style="width:100%"></a>

					<!-- les dates, heures, titre, compositeur, description -->
		    		<div class="conteneur-texte">
		   		   		<P>Date et heure</p><br>
						<a href="../5_detail/detail.php"><h1>Titre</h1></a>
						<h3>Compositeur</h3><br>
						<p>Description</p>
					</div>
					<!-- les boutons (liens) -->
					<a href="../5_detail/detail.php" class="colonne deta">Détail</a>
					<a href="../3_reservation/reservation.php" class="colonne resa">Réserver</a>
		    	</div>
			</div>

			<!-- 2ème colonne ou grille verticale -->
			<div class="colonne concert">
		    	<div class="contenu">
					<!-- la photo -->
		    		<a href="#"><img src="../../images/trio.jpg" alt="concert" style="width:100%" height="221px"></a>

					<!-- les dates, heures, titre, compositeur, description -->
					<div class="conteneur-texte">
		   		   		<P>Date et heure</p><br>
						<a href="../5_detail/detail.php"><h1>Titre</h1></a>
						<h3>Compositeur</h3><br>
						<p>Description</p>
					</div>

					<!-- les boutons (liens) -->
					<a href="#" class="colonne deta">Détail</a>
					<a href="../3_reservation/reservation.php" class="colonne resa">Réserver</a>
		    	</div>
			</div>

			<!-- 3ème colonne ou grille verticale -->
			<div class="colonne recital">
		    	<div class="contenu">
					<!-- la photo -->
		    		<a href="#"><img src="../../images/karine.jpg" alt="recital" style="width:100%" height="221px"></a>

					<!-- les dates, heures, titre, compositeur, description -->
					<div class="conteneur-texte">
		   		   		<P>Date et heure</p><br>
						<a href="../5_detail/detail.php"><h1>Titre</h1></a>
						<h3>Compositeur</h3><br>
						<p>Description</p>
					</div>

					<!-- les boutons (liens) -->
					<a href="#" class="colonne deta">Détail</a>
					<a href="../3_reservation/reservation.php" class="colonne resa">Réserver</a>
		    	</div>
			</div>
		
			<!-- 4ème colonne ou grille verticale -->
			<div class="colonne danse">
		    	<div class="contenu">
					<!-- la photo -->
		    		<a href="#"><img src="../../images/ballet.jpg" alt="danse" style="width:100%"></a>

					<!-- les dates, heures, titre, compositeur, description -->
					<div class="conteneur-texte">
		   		   		<P>Date et heure</p><br>
						<a href="../5_detail/detail.php"><h1>Titre</h1></a>
						<h3>Compositeur</h3><br>
						<p>Description</p>
					</div>

					<!-- les boutons (liens) -->
					<a href="#" class="colonne deta">Détail</a>
					<a href="../3_reservation/reservation.php" class="colonne resa">Réserver</a>
		    	</div>
			</div>
		</div> 
		<!-- fin de la ligne -->
	</section> 
	<!-- fin de la section -->
</main>
<!-- fin du main -->



	<script type="text/javascript" src="spectacle.js"></script>
</body>
<footer></footer>
</html>