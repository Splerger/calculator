@echo off

pyinstaller --onefile --icon=icon.ico --add-data="icon.ico;." .\calculator.pyw

signtool sign /a /fd SHA256 /tr http://timestamp.digicert.com /td SHA256 dist/calculator.exe

start dist/calculator.exe