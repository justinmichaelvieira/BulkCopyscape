<?php 
	
	//Return data in config.json
	function GetJson($file, $debug = 0)
	{	
		$str = file_get_contents($file);
		$json = json_decode($str, true);
		
		if($debug)
		{
			echo "json data:<p />";
			echo '<pre>' . print_r($json, true) . '</pre>';
		}
		
		return $json;
	}
?>