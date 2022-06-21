
<body>
<?php 
    // d'abord, on relie les tables à la base de données
	try 
	{  
	$bdd = new PDO('mysql:host=localhost;dbname=theatre;charset=utf8', 'root', '', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
	} 
	catch (Exception $e) 
	{
		die('Erreur : il y a un problème '.$e -> getMessage());
	}
?>
</body>