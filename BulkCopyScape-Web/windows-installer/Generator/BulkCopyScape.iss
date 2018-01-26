; BulkCopyScape.iss
; Generates install package for bulk copyscape on windows

; SEE INNO SETUP FOR DETAILS ON CREATING .ISS SCRIPT FILES!

[Setup]
AppName=Bulk CopyScape
AppVersion=1.0
DefaultDirName=c:\inetpub\wwwroot\BulkCopyScape
DefaultGroupName=Bulk CopyScape
Compression=lzma2
SolidCompression=yes
OutputDir=userdocs:Bulk Copyscape Install Output

[Files]
Source: "C:\InstallerFiles\BulkCopyScape\*"; DestDir: "{app}"
Source: "C:\InstallerFiles\BulkCopyScape\uploads\*"; DestDir: "{app}\uploads"

[Icons]
Name: "{group}\Setup API Access"; Filename: "http:\\localhost\BulkCopyScape\SetupForm.php"
Name: "{group}\Run Bulk CopyScape"; Filename: "http:\\localhost\BulkCopyScape\RunCopyscapeLoop.php"
