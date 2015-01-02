<html>
<body>

<?php

$file1= "c:\\inetpub\\wwwroot\\test1\\uploads\\BulkCSConfig.json";
$debug = 0;

error_reporting(E_ALL | E_STRICT);
ini_set('display_errors', 0);
ini_set('log_errors', 1);
ini_set('error_log', "c:/php.log");

function mk_file($filename) {
    if(!is_file($filename)) {
		$handle = fopen($filename,"w"); //create the file
		$string = "{\"u\": \"" . $_POST['element_1'] . "\", \"k\": \"" . $_POST['element_2'] . "\"}";
		fwrite($handle, $string); 
		
        fclose($handle);
		
        return true;
    } else return false; //file already exists
}


if($debug)
{
	foreach ($_POST as $key => $value)
		echo "Field ".htmlspecialchars($key)." is ".htmlspecialchars($value)."<br>";
}

//Write config file
$wrote = mk_file($file1);

//Display error or success message
if($wrote)
	echo "Saved api settings. Now you can go to use the tool.  <a href='RunCopyscapeLoop.php'> Click here to continue...</a>";
else 
	echo "Error writing file - make sure BulkCSConfig.json does not already exist in the upload dir, and upload dir is writeable."; 
?>

</body>
</html>