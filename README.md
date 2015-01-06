Bulk CopyScape
=============

Bulk Copyscape is a script that utilizes Copyscape's API to by-pass the normal bulk upload queue, allowing you to quickly check websites for plagiarism or duplicate content in a matter of moments - for free!

This tool is great for busy SEO's and webmasters looking to protect their content from thieves or to clear up duplicate information from being found by Google.
Designed by redditor [http://reddit.com/u/angryrancor](/u/angryrancor). Words by [http://reddit.com/u/fearthejew](/u/fearthejew)

Install Instructions
=============

Requires [PHP](http://php.net) and [Curl](http://curl.haxx.se)

Windows Users:

* Give [the installer](https://github.com/angryrancor/BulkCopyscape/blob/master/windows-installer/Installer/InstallBulkCopyscape.exe) a try.
* Set {install dir}/uploads writeable by your webserver (or alternatively everyone)
* Make sure Curl is in your system PATH.

Other Platforms:

* Copy all files to a folder which can execute PHP.  
* Inside this folder, make a "./uploads" folder.
* Make sure you can upload to the uploads folder (e.g. run "chmod 0644 ./uploads" or similar permissions escalation).
* Browse to SetupForm.php on your web host or local webserver url.