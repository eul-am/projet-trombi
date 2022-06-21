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
	<title>DÉTAILS</title>

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
	<a href="../1_evenement/evenement.php">Événements</a>
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

<main>
	<!-- MAIN (Center website) -->
	<div class="main">
		<h1 class="h1-ev">AFFICHE DÉTAILLÉE </h1>
		<!--   -->
		<div class="ligne">
			<div class="colonne categorie">
				<!-- <div class="contenu"> -->
		  			<img src="../../images/ensemble.jpg" alt="opera" style="width:100%">
				<!-- </div> -->
			</div>
			<!-- fin colonne -->

			

			<!-- <div class="colonne boite-droite"> -->
				<!-- <div class="conteneur-droite"> -->
					<div class="agenda">
						<!-- <div class="contenu-panier"> -->
		    				<h3 class="h3-ev">Dates et heures</h3>
							<a href="panier.php">Nombre d'article dans le panier</a>
						<!-- </div> -->
					</div>

					<div class="tarifs">
						<!-- <div class="contenu-panier"> -->
		    				<h3 class="h3-ev">Tarifs</h3>
							<a href="panier.php">Nombre d'article dans le panier</a>
						<!-- </div> -->
					</div>

					<div class="reservation">
						<!-- <div class="contenu-panier"> -->
		    				<h3 class="h3-ev">Réservation</h3>
							<a href="reservation.php">Nombre d'article dans le pa</a>
						<!-- </div> -->
					</div>
				<!-- </div> -->
			<!-- </div> -->

			<div class="colonne programme">
				<!-- <div class="contenu-panier"> -->
		    		<h3 class="h3-ev">Programme</h3>
					<a href="panier.php">Nombre d'article dans le panier</a>
				<!-- </div> -->
			</div>
		</div>
		<!-- fin ligne -->
	</div>
	<!-- fin section -->
</main> 
<!-- fin main -->

	<section>
		<!-- CODE APRÈS LE MAIN -->
	</section>

	<script type="text/javascript" src="spectacle.js"></script>
</body>
<footer></footer>
</html>