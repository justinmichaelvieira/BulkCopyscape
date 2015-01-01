<html>
<body>
<? 

//Makes user dir for us if it doesn't exist
function file_force_contents($filename, $data, $flags = 0){
    if(!is_dir(dirname($filename)))
        mkdir(dirname($filename).'/', 0644, TRUE);
    return file_put_contents($filename, $data,$flags);
}

//Write config file
$wrote = file_force_contents('./uploads/BulkCSConfig.json', 'module.exports = {u: ' + $_POST['element_1'] +', k: ' + $_POST['element_2'] + '}');

//Display error or sucess message
if($wrote)
	echo "Saved api settings. Now you can go to " +  + " to use the tool.";
else 
	trigger_error("file_force_contents() : error writing file '$wrote'", E_USER_WARNING); 
?>
</body>
</html>
