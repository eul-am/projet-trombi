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
	<title>INDEX</title>
</head>
<body>
	<!-- Début en-tête -->
	<div class="header">

		<!-- logo , côté gauche en-tête -->
		<div>
			<a href="#"><img src="../images/logo.png" class="logo"></a>
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
								<a href="../connexion/connexion.php" class="a-droite">Connexion</a>
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
									<a href="../utilisateur/profil.php" class="a-droite">Profil</a>
									<a href="../connexion/deconnexion.php" class="a-droite">Déconnexion</a>
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
			<a href="index.php" class="actif">Home</a>
			<a href="../navigation/1_evenement/evenement.php">Événements</a>
			<a href="../navigation/2_agenda/agenda.php">Agenda</a>
			<a href="../navigation/3_reservation/reservation.php">Réservation</a>
			<a href="../navigation/4_infos_pratiques/page4.htm">Infos pratiques</a>
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


	<!-- DÉBUT MAIN -->
	<!-- <div class="main">
		<h1>ACTUALITÉ</h1> -->

		<!-- DIAPO -->
		<!-- <div class="conteneur-diapo">
			<a href="">
				<div class="conteneur-photo">
					<img src="../images/ensemble.jpg" class="diapo" style="width:100%" height="600px">
					<div class="conteneur-texte">
 						<h2>Some Other Work</h2>
  						<p>Lorem ipsum dolor sit amet, tempor prodesset eos no. 
						Temporibus necessitatibus sea ei, at tantas oporteat nam. Lorem ipsum dolor sit amet, tempor prodesset eos no.
						Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptas nesciunt nobis quasi fuga qui possimus, 
						ex id! Numquam distinctio placeat error modi, accusantium, omnis totam eos temporibus soluta adipisci fugit?
						</p>
					</div>

  					<img src="../images/trio.jpg" class="diapo" style="width:100%" height="600px"> -->

  					<!-- <button class="w3-button w3-black w3-display-left" onclick="plusDivs(-1)">&#10094;</button>
  					<button class="w3-button w3-black w3-display-right" onclick="plusDivs(1)">&#10095;</button> -->
					<!-- <div class="conteneur-texte">
 							<h2>Some Other Work</h2>
  							<p>Lorem ipsum dolor sit amet, tempor prodesset eos no. 
							Temporibus necessitatibus sea ei, at tantas oporteat nam. Lorem ipsum dolor sit amet, tempor prodesset eos no.
							Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptas nesciunt nobis quasi fuga qui possimus, 
							ex id! Numquam distinctio placeat error modi, accusantium, omnis totam eos temporibus soluta adipisci fugit?
							</p>
					</div>

						<script>
							var slideIndex = 0;
							carousel();

							function carousel() 
							{
  								var i;
  								var x = document.getElementsByClassName("diapo");
  								for (i = 0; i < x.length; i++) 
						 		{
    								x[i].style.display = "none";
  								}
  								slideIndex++;

  								if (slideIndex > x.length) 
								{
								  	slideIndex = 1
								}
  								x[slideIndex-1].style.display = "block";

  								setTimeout(carousel, 2000); // Change image every 2 seconds
							}
						</script>
				  	</div>
				</div> 
			</a>
		</div>
	</div> -->
	<!-- FIN MAIN -->


	<script type="text/javascript" src="spectacle_3.js"></script>

    <!-- <footer class="pied"></footer> -->
</body>
</html>