sudo pipenv run pyinstaller --onefile --windowed bulkcopyscape.spec
sudo cp -r dist/bulkcopyscape/* dist/BulkCopyScape.app/Contents/MacOS/