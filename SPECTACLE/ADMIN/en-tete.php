<header class="conteneur-entete">
		<a href="../espace_admin.php" class="logo"><img src="../logo.png"></a>

		<nav class="">
			<!-- <a href="../navigation/programmation/programmation.php">Programmation</a>
			<a href="../navigation/agenda/agenda.php">Agenda</a>
			<a href="../navigation/reservation/reservation.php">Réservation</a>
			<a href="../navigation/infos_pratiques/infos_pratiques.php">Infos pratiques</a> -->
		</nav>
		
		<!-- si l'utilisateur n'est pas connecté -->
		<?php if(!isset($_SESSION['id']) AND !isset($_SESSION['type']) AND !isset($_SESSION['nom']) AND !isset($_SESSION['email']))
		{
			// on affiche connexion
			?>
				<a href="../connexion/connexion.php">Connexion</a>
			<?php
		}

		else
		{
			//sinon on affiche déconnexion
			?>
				<div>
					<div>Vous êtes connecté en tant qu'<?php echo htmlentities(trim($_SESSION['type'])); ?></div>
					<div>Votre nom est : <?php echo htmlentities(trim($_SESSION['nom'])); ?></div>
					<div><a href="../admin/espace_admin.php">Mon profil</a></div>
					<div><a href="../connexion/deconnexion.php">Déconnexion</a></div>
				</div>
			<?php
		}
		?>
	</header>