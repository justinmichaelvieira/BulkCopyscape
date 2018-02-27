Bulk CopyScape
=============

Bulk Copyscape is a script that utilizes Copyscape's API to by-pass the normal bulk upload queue, allowing you to quickly check websites for plagiarism or duplicate content in a matter of moments - for free!

This tool is great for busy SEO's and webmasters looking to protect their content from thieves or to clear up duplicate information from being found by Google.
Designed by redditor [http://reddit.com/u/angryrancor](/u/angryrancor) of [Rancorsoft](http://rancorsoft.com). Words by [http://reddit.com/u/fearthejew](/u/fearthejew)

![Screen 1](ss1.png)

![Screen 2](ss2.png)

![Screen 3](ss3.png)

![Screen 4](ss4.png)

Desktop/Mobile App - Install instructions
=============

Requires [Python3](https://www.python.org/downloads/) and [Qt](https://www.qt.io/download). The open source version of Qt is fine, and recommended - if you don't already have it.

* Install [Python3](https://www.python.org/downloads/) and [Qt](https://www.qt.io/download) if you don't already have them.
* Download the repository and open a shell prompt at the BulkCopyScape-pyqt folder.
* Type `pip install -r requirements.txt` to install the libraries used by the app.
* Type `python3 -m bulkcopyscape` to run the app!


Web app - Live Public Beta
=============

![Web app screenshot](http://rancorsoft.com/images/logos/bulkcopytools_sm.png)

Just want to give Bulk Copyscape a try, without installing it yourself?  [Bulk Copy Tools](https://bulkcopytools.com) has what you need.

Web App - Install Instructions
=============

Requires [PHP](http://php.net) and [Curl](http://curl.haxx.se)

Windows Users:

* Give [the installer](https://github.com/angryrancor/BulkCopyscape/blob/master/BulkCopyScape-Web/windows-installer/Installer/InstallBulkCopyscape.exe) a try.  MD5 (InstallBulkCopyscape.exe) = 3eca09855a18ff676a4c968b4a519e20
* Set {install dir}/uploads writeable by your webserver (or alternatively everyone)
* Make sure Curl is in your system PATH.

Other Platforms:

* Copy all files to a folder which can execute PHP.  
* Inside this folder, make a "./uploads" folder.
* Make sure you can upload to the uploads folder (e.g. run "chmod 0644 ./uploads" or similar permissions escalation).
* Browse to SetupForm.php on your web host or local webserver url.
* note - if there are problems with hard coded paths or configs, please email justin [at] rancorsoft.com or /u/angryrancor on reddit
