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
	<script type="text/javascript"></script>
	<title>INFOS PRATIQUES</title>
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
	<a href="infos_pratiques.php">Infos pratiques</a>
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
<div class="main">

<h1 
	class="h1-ev">INFOS PRATIQUES

</h1>

<div id="conteneur-bouton">
	  <!-- <button class="btn actif" onclick="filtrerPar('toute')"> Accès & Services</button> -->
	<button class="btn" onclick="filtrerPar('recital')"> Accès & Services</button>
	  <button class="btn" onclick="filtrerPar('opera')"> S'inscrire à la Newletter</button>
	  <button class="btn" onclick="filtrerPar('concert')"> Contact</button>
</div>

<div class="colonne recital">
	<div class="contenu">
		<div class="infos">
		<h3 class="h3-ev">VENIR A L'OPERA</h3>
			<div class="acces">
				<h5 class="">En Voiture</h5>
			</div>
			<div class="acces">
				<h5 class="">En Bus</h5>
			</div>
			<div class="acces">
				<h5 class="">En Métro</h5>
			</div>
		</div>
		<div class="infos">
			<h3 class="h3-ev">SERVICE</h3>

		</div>

	</div>
</div>

<div class="ligne">
	<div class="colonne opera">
		<div class="contenu">
			<div class="infos">
				<h3 class="h3-ev">S'INSCRIRE A LA NEWSLETTER</h3>
					<div class="acces">
						<h5 class="">En Voiture</h5>
					</div>
				</div>
				<div class="infos">
					<form action=""></form>
						  <input type="nom" class="form-control" name="nom" id="nom" placeholder="Enter nom">
						  <input type="prenom" class="form-control" name="prenom" id="prenom" placeholder="Enter prenom">
						  <input type="email" class="form-control" name="mail" id="mail" placeholder="Enter mail">
						  <button type="submit" name="login" class="btn btn-primary">Login</button>
					</form>
				</div>
		</div>
</div>

<div class="colonne concert">
	<div class="contenu">
		<div class="infos">
			<h3 class="h3-ev">VENIR A L'OPERA</h3>
					<div class="acces">
						<h5 class="">Informations billeterie</h5>
					</div>
					<div class="acces">
						<h5 class="">Téléphone</h5>
					</div>
					<div class="acces">
						<h5 class="">Contact Presse</h5>
					</div>
		</div>
	</div>
</div>

</div> <!-- FIN DIV ligne -->
</div> <!-- FIN MAIN -->

<script type="text/javascript" src="js/spectacle.js"></script>

</body>
</html>