<html>
<body>
<?
if($_FILES["element_1"]["name"]) 
{
	$filename = $_FILES["element_1"]["name"];
	$source = $_FILES["element_1"]["tmp_name"];
	$type = $_FILES["element_1"]["type"];
	
	$name = explode(".", $filename);
	$accepted_types = array('application/zip', 'application/x-zip-compressed', 'multipart/x-zip', 'application/x-compressed');
	foreach($accepted_types as $mime_type) {
		if($mime_type == $type) {
			$okay = true;
			break;
		} 
	}
	
	$continue = strtolower($name[1]) == 'zip' ? true : false;
	if(!$continue) {
		$message = "The file you are trying to upload is not a .zip file. Please try again.";
	}

	$target_path = "./uploads/".$filename;  // change this to the correct site path
	if(move_uploaded_file($source, $target_path)) 
	{
		$zip = new ZipArchive();
		$x = $zip->open($target_path);
		
		if ($x === true) 
		{
			$zip->extractTo("./uploads"); // change this to the correct site path
			$zip->close();
	
			unlink($target_path);
		}
		$message = "Your .zip file was uploaded and unpacked.";
	} else {	
		$message = "There was a problem with the upload. Please try again.";
	}
	
	if($message) echo "<p>$message</p>"; 
	
	//Get data in config.json
	$str = file_get_contents('./uploads/BulkCSConfig.json');
	$json = json_decode($str, true);

	echo "json data:<p />";
	echo '<pre>' . print_r($json, true) . '</pre>';

	//extract data from the post
	extract($_POST);

	//set POST variables
	$url = 'http://www.copyscape.com/api/';

	//Check for extracted files
	$directory = "./uploads";
    if (! is_dir($directory)) {
        echo('Upload directory does not exist.');
    }
	else
	{

		$files = array();

		foreach (scandir($directory) as $file) {
			if ('.' === $file) continue;
			if ('..' === $file) continue;

			$files[] = $file;
		}

		var_dump($files);
		
		foreach($files as $file)
		{
			$fields = array(
							'u' => urlencode($json['u']),
							'k' => urlencode($json['k']),
							'o' => urlencode('csearch'),
							'e' => urlencode('UTF-8'),
							't' => urlencode($file),
						);

			//url-ify the data for the POST
			foreach($fields as $key=>$value) { $fields_string .= $key.'='.$value.'&'; }
			rtrim($fields_string, '&');

			//open connection
			$ch = curl_init();

			//set the url, number of POST vars, POST data
			curl_setopt($ch,CURLOPT_URL, $url);
			curl_setopt($ch,CURLOPT_POST, count($fields));
			curl_setopt($ch,CURLOPT_POSTFIELDS, $fields_string);

			//execute post
			$result = curl_exec($ch);

			echo "Result: " + $result + "</p>";

			//close connection
			curl_close($ch);
		}
	}
}

?>
</body>
</html>
