<?php
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
		$message = "<div class=\"green\">Your .zip file was uploaded and unpacked.</div>";
	} 
	else 
	{	
		$message = "<div class=\"red\">There was a problem with the upload. Please try again.</div>";
	}
	
	if($message) echo "<p>$message</p>"; 
	
?>