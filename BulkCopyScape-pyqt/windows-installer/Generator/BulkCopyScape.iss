; BulkCopyScape.iss
; Generates install package for bulk copyscape on windows

; SEE INNO SETUP FOR DETAILS ON CREATING .ISS SCRIPT FILES!

[Setup]
AppName=Bulk CopyScape win32
AppVersion=1.0
DefaultDirName={pf}\Bulk CopyScape
DefaultGroupName=Bulk CopyScape win32
Compression=lzma2
SolidCompression=yes
OutputDir=userdocs:Bulk CopyScape win32 Install Output

[Files]
Source: "C:\Users\Justin\Documents\BulkCopyscape\BulkCopyScape-pyqt\dist\bulkcopyscape\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\Bulk CopyScape win32"; Filename: "{app}\bulkcopyscape.exe"
