<html>
<body>
<?php

$debug = 0;
    $str = file_get_contents("InstallConfig.json");
    $installjson = json_decode($str, true);

/**
 *
 * @get text between tags
 *
 * @param string $tag The tag name
 *
 * @param string $html The XML or XHTML string
 *
 * @param int $strict Whether to use strict mode
 *
 * @return array
 *
 */
function getTextBetweenTags($tag, $html, $strict=0)
{
    /*** a new dom object ***/
    $dom = new domDocument;

    /*** load the html into the object ***/
    if($strict==1)
    {
        $dom->loadXML($html);
    }
    else
    {
        $dom->loadHTML($html);
    }

    /*** discard white space ***/
    $dom->preserveWhiteSpace = false;

    /*** the tag by its tag name ***/
    $content = $dom->getElementsByTagname($tag);

    /*** the array to return ***/
    $out = array();
    foreach ($content as $item)
    {
        /*** add node value to the out array ***/
        $out[] = $item->nodeValue;
    }
    /*** return the results ***/
    return $out;
}

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
		$message = "Hooray! Your .zip file was uploaded and unpacked.";
	} 
	else 
	{	
		$message = "There was a problem with the upload. Please try again.";
	}
	
	if($message) echo "<p>$message</p>"; 
	
	//Get data in config.json
	$str = file_get_contents($installjson['UploadDir']."BulkCSConfig.json");
	$json = json_decode($str, true);

	if($debug)
	{
		echo "json data:<p />";
		echo '<pre>' . print_r($json, true) . '</pre>';
	}

	//extract data from the post
	extract($_POST);

	//set POST variables
	$url = 'http://www.copyscape.com/api/';

	//Check for extracted files
	$directory = $installjson['UploadDir'];
    if (!is_dir($directory)) {
        echo('Upload directory does not exist.');
    }
	else
	{

		$files = array();

		foreach (scandir($directory) as $file) {
			if ('.' === $file) continue;
			if ('..' === $file) continue;
			if (strpos($file,'BulkCSConfig.json') !== false) continue;
			$files[] = $file;
		}

		//var_dump($files);
		
		foreach($files as $file)
		{
			$loc = $directory . $file;
			echo $loc.'<br />';
			$myfile = fopen($loc, "r") or die("Unable to open file!");
			$contents =  fread($myfile,filesize($loc));
			fclose($myfile);
		
			$fields = array(
							'u' => urlencode($json['u']),
							'k' => urlencode($json['k']),
							'o' => urlencode('csearch'),
							'e' => urlencode('UTF-8'),
							't' => urlencode($contents),
							'f' => urlencode('html')
						);

			//url-ify the data for the POST
			foreach($fields as $key=>$value) { $fields_string .= $key.'='.$value.'&'; }
			rtrim($fields_string, '&');

			//open connection
			$ch = curl_init();

			//set the url, number of POST vars, POST data
			curl_setopt($ch,CURLOPT_URL, $url);
			curl_setopt($ch,CURLOPT_RETURNTRANSFER , 1);
			curl_setopt($ch,CURLOPT_POST, count($fields));
			curl_setopt($ch,CURLOPT_POSTFIELDS, $fields_string);

			//execute post
			$result = curl_exec($ch);
			
			$summaries = getTextBetweenTags('title', $result);
			foreach( $summaries as $item )
			{
				echo $item.'<br /><br />';
			}
			
			//echo "Result: ". $result . "</p>";

			if($debug)
			{
				//this is new debug output - standard output is simple number of results parsed from title tags
				echo "Result: ". $result . "</p>";
			}

			//close connection
			curl_close($ch);
		}
	}
}

?>
</body>
</html>