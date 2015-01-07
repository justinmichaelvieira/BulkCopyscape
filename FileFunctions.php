<?php 
	function mk_file($filename) 
	{
		if(!is_file($filename)) {
			$handle = fopen($filename,"w"); //create the file
			$string = "{\"u\": \"" . $_POST['element_1'] . "\", \"k\": \"" . $_POST['element_2'] . "\"}";
			fwrite($handle, $string); 
			
			fclose($handle);
			
			return true;
		} else return false; //file already exists
	}
?>