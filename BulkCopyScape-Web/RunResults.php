<html>
<head>

<script type="text/javascript" src="js/jquery-latest.min.js">
<script type="text/javascript" src="js/jquery-ui.js">
</script>
<!-- Toggle Panels
<script type="text/javascript">
	$(document).ready(function() {
		$(".flip").click(function() {
			$(".panel").slideToggle("slow");
		});
	});
	
	$(document).ready(function() {
		$(".flip2").click(function() {
			$(".panel2").slideToggle("slow");
		});
	});
</script> -->
 <script>
  jQuery(document).ready(function() {
    jQuery( document ).tooltip();
	jQuery( ".tabs" ).tabs();
  })
</script>
<LINK rel="stylesheet" href="style.css" type="text/css">
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/themes/smoothness/jquery-ui.css" />
<script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>
</head>

<body>
<?php

$debug = 0;

include_once('TextFunctions.php');
include_once('JsonFunctions.php');
include_once('CurlFunctions.php');

if($_FILES["element_1"]["name"]) 
{
	include('GetZip.php');
	
	$json = GetJson("c:\\inetpub\\wwwroot\\test1\\uploads\\BulkCSConfig.json", $debug);

	//extract data from the post
	extract($_POST);
	$url = 'http://www.copyscape.com/api/';

	//Check for extracted files
	$directory = "c:\\inetpub\\wwwroot\\test1\\uploads\\";
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
		
		//Buttons
		//echo "<br><div class=\"buttonOuter\"><div id=\"button\" class=\"flip\">Toggle Links</div><div id=\"button2\" class=\"flip2\">Toggle Descriptions</div></div></div>";
		
		foreach($files as $file)
		{
			$loc = $directory . $file;
			echo '<div class="wrap"><h1 style="clear:both;">'.$file.'</h1>';
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

			$result = CurlPost($url, $fields, $fields_string);
			
			$summaries = GetTextBetweenTags('title', $result);
			
			//for( $index = 0; $index < count($summaries); $index++ )
			//{
				echo '<h2>  --  '.$summaries[0].'</h2></div>';
			//}
			
			$headings = GetTextBetweenTags('a', $result);
			$textBlurbs = GetTextBetweenTags('font', $result);
			$links = GetHrefAttributes($result);
			
			echo <<<EOT
  <div id="tabs" class="tabs">
  <ul>
    <li><a href="#tabs-1">Headings</a></li>
    <li><a href="#tabs-2">Page Text Excerpts</a></li>
    <li><a href="#tabs-3">Full API Response</a></li>
  </ul>
  <div id="tabs-1">
EOT;

			echo "<h3>Headings</h3><div class=\"panelOuter\"><div class=\"panel\">";
				for( $index = 0; $index < count($headings); $index++ )
				{
					echo '<a href="'.$links[$index].'" title="'.$headings[$index].'" target="_blank">'.$index.'</a> ';
				} 
			echo "</div></div></div>";
			echo '<div id="tabs-2">';
			echo "<h3>Page Text Excerpts</h3><div class=\"panel2\">";
			for( $index = 0; $index < count($headings); $index++ )
			{
				echo '<a href="'.$links[$index].'" target="_blank" title="'.$textBlurbs[$index*3].$textBlurbs[$index*3 + 1].'">'.$index.'</a> ';
			}
			echo "</div></div>";
			echo '<div id="tabs-3">';
			echo "<h3>Full API Response</h3>";
			echo '<textarea rows="5">'. $result.'</textarea></div>';
			echo "</div>";

			curl_close($ch);
		}
	}
}

?>
</body>
</html>