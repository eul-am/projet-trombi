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
	<title>AOÛT</title>

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
	<a href="agenda.php">Agenda</a>
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
	<div class="main">

		<h1 
			class="h1-ev">Août 2022
			<!-- <hr> -->
		</h1>

	
		<div class="conteneur-bouton">
  			<a href="septembre.php" class="se">Septembre</a>
  			<a href="octobre.php" class="oc">Octobre</a>
  			<a href="novembre.php" class="no">Novembre</a>
  			<a href="decembre.php" class="de">Décembre</a>
			<a href="janvier.php" class="ja">Janvier</a>
			<a href="fevrier.php" class="fe">Février</a>
			<a href="mars.php" class="ma">Mars</a>
			<a href="avril.php" class="av">Avril</a>
			<a href="mai.php" class="mai">Mai</a>
			<a href="juin.php" class="ju">Juin</a>
			<a href="juillet.php" class="jl">Juillet</a>
			<a href="aout.php" class="ao">Août</a>
		</div>

		<!--  NB : Ici ce sont les lignes qui se dupliquent. On fera la boucle sur une ligne -->
		<div class="ligne">
			<div class="colonne agenda">
				<!-- conteneur photo -->
				<div class="ph-ag">
					<!-- photo -->
					<img src="../../images/ensemble.jpg" alt="IMAGE" style="width: 100%">
				</div>
				<!-- conteneur texte -->
				<div class="conteneur-texte">
					<h5>Genre</h5> <br>
		      		<h3 class="h3-ev">Titre</h3>
		      		<p>Compositeur</p>
				</div>
				<!-- conteneur horaire -->
				<div class="horaire">
					<h4>Heure rond</h4>
				</div>
			</div>
		</div> 
		<!-- fin ligne -->
	</div> 
	<!-- fin main -->
</main>

	<section>
		<!-- CODE APRÈS LE MAIN -->
	</section>

	<script type="text/javascript" src="spectacle.js"></script>
</body>
<footer></footer>
</html>
