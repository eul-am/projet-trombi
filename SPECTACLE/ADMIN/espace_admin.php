<?php 
    // la SESSION démarre
    session_start();
 
?>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="../styles/spectacle.css">
	<title>ESPACE ADMIN</title>
</head>
<body>

<header class="conteneur-entete">
		<a href="espace_admin.php" class="logo"><img src="logo.png"></a>

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
				<div><a href="../connexion/connexion.php">Connexion</a></div>
			<?php
		}

		else
		{
			//sinon on affiche déconnexion
			?>
				<div>
					<div>Vous êtes connecté en tant qu'<?php echo htmlentities(trim($_SESSION['type'])); ?></div>
					<div>Votre nom est : <?php echo htmlentities(trim($_SESSION['nom'])); ?></div>
					<div><a href="../admin/espace_admin.php">Profil</a></div>
					<div><a href="../connexion/deconnexion.php">Déconnexion</a></div>
				</div>
			<?php
		}
		?>
	</header>

    <h1>Espace administrateur</h1>

	<?php if(!isset($_SESSION['id']) AND !isset($_SESSION['type']) AND !isset($_SESSION['nom']) AND !isset($_SESSION['email']))
		{

		}

		else
		{
			//sinon on affiche déconnexion
			?>
			<div>
				<div><a href="../admin/0_utilisateur/utilisateur.php">Gestion des utilisateurs</a></div>
				<div><a href="../admin/1_saison/saison.php">Gestion des saisons</a></div>
				<div><a href="../admin/2_artiste/artiste.php">Gestion des artistes</a></div>
				<div><a href="../admin/3_oeuvre/oeuvre.php">Gestion des oeuvres</a></div>
				<div><a href="../admin/4_evenement/evenement.php">Gestion des événements</a></div>
				<div><a href="../admin/5_tarif/tarif.php">Gestion des places et tarifs</a></div>
				<div><a href="../admin/6_affiche/affiche.php">Gestion des affiches</a></div>
				<div><a href="../admin/7_detail/detail.php">Gestion des détails</a></div>
				<div><a href="../admin/8_panier/panier.php">Gestion du panier</a></div>
			</div>
			<?php
		}
		?>

	<script type="text/javascript" src="../scripts/spectacle.js"></script>

</body>
</html>