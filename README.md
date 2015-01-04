Bulk CopyScape
=============

A bulk copyscape testing script.

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