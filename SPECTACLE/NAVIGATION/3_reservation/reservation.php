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
	<title>RÉSERVATION</title>

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
	<a href="reservation.php">Réservation</a>
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
		<h1 class="h1-ev">RÉSERVATION</h1>
		<!--   -->
		<div class="ligne">
			<div class="colonne categorie">
			<form>
		<table>
			<th>Catégorie</th>
			<th>Préférence</th>
			<th>Quantité</th>
			<th>Prix unitaire</th>
			<th>Sous-total</th>

			<tr>
				<td>Catégorie 1</td>
				<!-- préférence -->
				<td>
					<select name="preference" id="preference">
		  				<option value="">----</option>
		  				<option value="balcon">Balcon </option>
		  				<option value="corbeille">Corbeille</option>
		  				<option value="orchestre">Orchestre</option>
		  			</select>
				</td>

				<!-- quantité -->
				<td>
				<input type="text" id="quantite-1" oninput="reServation1(event)">
					<!-- <select name="quantite" id="quantite">
						<option value="0">0</option>
		  				<option value="1">1</option>
		  				<option value="2">2</option>
		  				<option value="3">3</option>
		  				<option value="4">4</option>
		  				<option value="5">5</option>
		  				<option value="6">6</option>
		  			</select> -->

					  <!-- javascript -->
					<script type='text/javascript'>
  						function reServation1(event) 
  						{
							//   ici on multiplie la propriété data par le prix unitaire
    						document.getElementById("sous-total-1").innerHTML = event.data * 2;
  						}
					</script>
				</td>

				<!-- prix unitaire -->
				<td id="prix-1"><input></td>

				<!-- sous-total -->
				<td id="sous-total-1"><input></span></td>
			</tr>

			<tr>
				<td>Catégorie 2</td>
				<!-- préférence -->
				<td>
					<select name="preference" id="preference">
		  				<option value="">----</option>
		  				<option value="balcon">Balcon </option>
		  				<option value="corbeille">Corbeille</option>
		  				<option value="orchestre">Orchestre</option>
		  			</select>
				</td>

				<!-- quantité 2 -->
				<td>
					<input type="text" id="quantite-2" oninput="reServation2(event)">
					<!-- javascript -->
					<script type='text/javascript'>
  						function reServation2(event) 
  						{
							//   ici on multiplie la propriété data par le prix unitaire
    						document.getElementById("sous-total-2").innerHTML = event.data;
  						}
					</script>
				</td>
				<!-- prix unitaire -->
				<td id="prix-2"><input></td>
				<!-- sous-total -->
				<td id="sous-total-2"><input></span></td>
			</tr>

			<tr>
				<td>Catégorie 3</td>
				<!-- préférence -->
				<td>
					<select name="preference" id="preference">
		  				<option value="">----</option>
		  				<option value="balcon">Balcon </option>
		  				<option value="corbeille">Corbeille</option>
		  				<option value="orchestre">Orchestre</option>
		  			</select>
				</td>

				<!-- quantité 3 -->
				<td>
					<input type="text" id="quantite-3" oninput="reServation3(event)">
					<!-- javascript	-->
					<script type='text/javascript'>
  						function reServation3(event) 
  						{
							//   ici on multiplie la propriété data par le prix unitaire
    						document.getElementById("sous-total-3").innerHTML = event.data;
  						}
					</script>
				</td>
				<!-- prix unitaire 3 -->
				<td id="prix-3"><input></td>
				<!-- sous-total 3 -->
				<td id="sous-total-3"><input></span></td>
			</tr>

			<tr>
				<td>Catégorie 4</td>

				<!-- préférence -->
				<td>
					<select name="preference" id="preference">
		  				<option value="">----</option>
		  				<option value="balcon">Balcon</option>
		  				<option value="corbeille">Corbeille</option>
		  				<option value="orchestre">Orchestre</option>
		  				<option value="galerie">Galerie</option>
		  			</select>
				</td>

				<!-- quantité 4 -->
				<td>
					<input type="text" id="quantite-4" oninput="reServation4(event)">
					<!-- javascript -->
					<script type='text/javascript'>
  						function reServation4(event) 
  						{
							//   ici on multiplie la propriété data par le prix unitaire
    						document.getElementById("sous-total-1").innerHTML = event.data;
  						}
					</script>
				</td>
				<!-- prix unitaire 4 -->
				<td id="prix-4"><input></td>
				<!-- sous-total 4 -->
				<td id="sous-total-4"><input></span></td>
			</tr>

			<tr>
				<td>Catégorie 5</td>

				<!-- préférence 5 -->
				<td>
					<select name="preference" id="preference">
		  				<option value="">----</option>
		  				<option value="balcon">Balcon </option>
		  				<option value="galerie">Galerie</option>
		  			</select>
				</td>

				<!-- quantité 5 -->
				<td>
					<input type="text" id="quantite-5" oninput="reServation5(event)">

					<!-- Fonction javascript -->
					<script type='text/javascript'>
  						function reServation5(event) 
  						{
							//   ici on multiplie la propriété data par le prix unitaire
    						document.getElementById("sous-total-5").innerHTML = event.data;
  						}
					</script>
				</td>
				<!-- prix unitaire 5-->
				<td id="prix-5"><input></td>
				<!-- sous-total 5-->
				<td id="sous-total-5"><input></span></td>

				<!-- prix total -->
				<table>
				<tr>
					<td>Total</td>
					<td><input type="value" name=""></td>
					<td><button type="submit">Ajouter au panier</button></td>
				</tr>
				</table>
			</tr>
		</table>
	</form>

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


	<section>
		<!-- CODE APRÈS LE MAIN -->
	</section>

	<script type="text/javascript" src="spectacle.js"></script>
</body>
<footer></footer>
</html>